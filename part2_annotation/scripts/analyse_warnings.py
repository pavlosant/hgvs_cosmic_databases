"""
Pavlos Antoniou
08/08/2021
Annotation analysis for COSMIC vep annotation pipeline
"""

import pathlib
from pathlib import Path
import pprint as pp
import argparse
import re
import csv


DIAS_WARNING="DIAS_SYSTEM_ERROR"
INPUT_WARNING="INPUT_WARNING"

class Sample:
    """
    Class to hold information about a sample
    and its warning files
    """
    vep_out_path=""
    dias_path=""
   
    def __init__(self,sampleID,):
        self.sampleID=sampleID
                

        
    def extract_lines_related_error(self):
        print(self.warnings.warnings_text)
        with open(self.dias_path, 'r') as f:
            flines = f.readlines()
                #print(flines)


class Warning:
    """
    Class to hold information relating to  
    the warnings from the VEP run of a sample
    """
    def __init__(self, warning, warning_type):
        self.warning=warning
        self.warning_type=warning_type

    def __str__(self):
        return(f"{self.warning_type}: {self.warning}")

    def is_input_error(self):
        if self.warning_type==INPUT_WARNING:
            return True
        else: 
            return False

    def get_input_error_coordinates(self):
        """
        Extract 
        allele,
        start position,
        stop position
        and line number of the information
        from the warning object
        """
        allele_pattern=re.compile('(\w+) length')
        start_stop_pattern=re.compile('co-ordinates (\d+)-(\d+)')
        line_number_pattern=re.compile(' line (\d+)')
       
        allele=allele_pattern.search(self.warning).group(1)
        (start,stop)=start_stop_pattern.search(self.warning).group(1,2)
        line_number=line_number_pattern.search(self.warning).group(1)
        self.allele=allele
        self.stop=stop
        self.start=start
        self.line_number=line_number
                
               


def extract_sample_name(path):
    """
    Extracts and returns the sample ID 
    from the filename
    """
    sample=path.name.split(".") [0]
    return sample

def extract_warnings(pathname):
    """
    Reads and extrancts info from warning file
    checks if it is an input warning or a Dias system error warning
    saves the warning as a new Warning object
    saves the Warning (object) to its corresponding Sample (object)
    """
    warnings_list=[]
    warnings=[]
     
    with open(pathname,'r') as f:
        for line in f.readlines():
            if line.startswith("WARNING: Length of reference"):
                warning=line
                warning_type=INPUT_WARNING
                w=Warning(warning,warning_type)
                w.get_input_error_coordinates()
                warnings.append(w)
            else:
                warnings_list.append(line)

        if len(warnings)==0:
            warnings_text="\n".join(warnings_list)
            warning_type=DIAS_WARNING
            w=Warning(warnings_text,warning_type)
            warnings.append(w)
        return warnings

def match_line(filename,start,stop):
    """
    Matches start and stop coordinates with the 
    line in the filename (dias output file) that has these coordinates
    returns the line that has these start and stop positions
    """
    with open(filename, 'r') as csvfile:
        reader=csv.reader(csvfile, delimiter="\t")
        #headers = next(reader)[1:]
        for row in reader:
            if row[1]== start and row[2]==stop:
                #print("\t".join(row))
                return ("\t".join(row))
                

def main(args):
    sample_list=[]
    p=Path(args.vep_folder)
    
    #Get all warning file names
    warning_files=list(p.glob('*_warnings.txt'))
    for p in warning_files:
        # Extract sample name from filename
        sample=extract_sample_name(p)
        #Create a nee object of class Sample
        s=Sample(sampleID=sample)
        s.vep_out_path=p
        #Get all warnings related to sample s and save them to object s
        s.warnings=extract_warnings(p)
        #add sample to the global sample list to use later
        sample_list.append(s)

    with open(args.warnings_output_file1,'w') as outf:
        outf.write("Sample\tWarning_Type_from_VEP_output\tWarning_from_VEP_output\n")

        for s1 in sample_list:
           
            for w in s1.warnings:
                outf.write(f"{s1.sampleID}\t{w.warning_type}\t{w.warning}\n")

    '''
    Part 2
    '''
    #Get all the dias_extract files from folder
    dias=Path(args.dias_folder)
    dias_files=list(dias.glob('*.tsv'))
    #Associate each dias_extract file with its Sample object that it belongs to
    for f in dias_files:
        sampleID=extract_sample_name(f)
        for sample in sample_list:
            if sample.sampleID == sampleID:
                sample.dias_path=f
    #Find matching line in dias_extract file that refers to the VEP_output input warning for that Sample
    for s1 in sample_list:
        for w in s1.warnings:
            if w.warning_type == INPUT_WARNING:
                w.problem_line=match_line(s1.dias_path, w.start, w.stop)
    with open(args.warnings_output_file2,'w') as outf:
        outf.write(f'Sample\tWarning_from_VEP_output\tCorresponding_Line_from_Dias_extract_file\tVep_output_warning_file\tDias_extract_file\n')
        for s1 in sample_list:
            for w in s1.warnings:
                if w.warning_type == INPUT_WARNING:
                    outf.write(f"{s1.sampleID}\t{w.warning}\t{w.problem_line}\t{s1.vep_out_path}\t{s1.dias_path}\n")




if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    input_params = parser.add_argument_group("Input parameters")
    output_params=parser.add_argument_group("Output parameters")
    input_params.add_argument(
        "--vep_folder",
        help="Full path of vep_output folder.",
        default="part2_annotation/grch37_vep_output_sample_126",
        type=str,
    )
    input_params.add_argument(
        "--dias_folder",
        help="Full path of dias extract folder",
        default="part2_annotation/grch37_dias_extract_sample_126",
        type=str,
    )
    output_params.add_argument(
        "--warnings_output_file1",
        help="Full path of file to write the samples with warnings from vep_output and their warnings",
        default="part2_annotation/output_files/1.samples_with_warnings.tsv",
        type=str,
    )
    output_params.add_argument(
        "--warnings_output_file2",
        help="Full path of file to write the samples with INPUT_type warnings and the line from the dias_extract files that corresponds to the warning",
        default="part2_annotation/output_files/2.samples_with_input_warnings_and_dias_extracted_lines.tsv",
        type=str,
    )

    args = parser.parse_args()
    main(args)
