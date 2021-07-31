import re
import csv

#NM_152263.2:r.-115_775::NM_002609.3:r.1580_*1924

class Fusion:

    def __init__(self,transcript1,location1,transcript2,location2):
        self.transcript1=transcript1
        self.location1=location1
        self.transcript2=transcript2
        self.location2=location2
        
    def __str__(self):
        return f"{self.transcript1}:r.{self.location1[0]}_{self.location1[1]}::{self.transcript2}:r.{self.location2[0]}_{self.location2[1]}"


def extract_genomic_coordinates(VEP_annotation_file):
    with open(VEP_annotation_file, 'r') as csvfile:
        reader=csv.reader(csvfile, delimiter="\t")

        headers = next(reader)[:1]
        #print(headers)
        for row in reader:
            if row[0].startswith("#"):
                continue
            variant=row[2]
            
            chromosome=row[0]
            start=row[1]
            ref=row[3]
            alt=row[4]
            stop=len(alt)+int(start)-1
        
            print("Variant\tChromosome\tStart\tStop\tREF\tALT")
            print(f"{variant}\t{chromosome}\t{start}\t{stop}\t{ref}\t{alt}\n")

        

def fusion_to_hgvs(annotation):
    transcript_pattern=re.compile('ENST(\d+)\.(\d+)\(')
    positions_pattern=re.compile('\:r.(\d+)_(\d+)(_*)')
    transcripts_list=[]
    positions_list=[]

    transcripts=transcript_pattern.findall(annotation)
    for transcript in transcripts:
        transcript_name=f"ENST{transcript[0]}.{transcript[1]}"
        transcripts_list.append(transcript_name)
    
    positions=positions_pattern.findall(annotation)
    for pos in positions:
        #print(pos)
        (pos1,pos2)=pos[0],pos[1]
        positions_list.append((pos1,pos2))

    f=Fusion(transcripts_list[0],positions_list[0],transcripts_list[1],positions_list[1])
    print(f)



def main():
    print("Part 1")
    print("**********************************")
    print("Case 1")
    non_hgvs_annotation="ENST00000318522.5(EML4):r.1_1751_ENST00000389048.3(ALK):r.4080_6220"
    
    print(f"Cosmic fusion syntax: {non_hgvs_annotation}:")
    print("HGVS annotation: ", end="")
    fusion_to_hgvs(non_hgvs_annotation)
    print("**********************************")
    print("Case 2")
    
    print("Run VEP at https://www.ensembl.org/Multi/Tools/VEP?db=core ")
    print("with HGVS accession: ENST00000540549.1:c.355_356insATGG")
    print("Genomic coordinates (build 38):")
    VEP_annotation="vep_results/zs5zkjDyQn8IM2ZB.vcf"
    extract_genomic_coordinates(VEP_annotation_file=VEP_annotation)
   
    print("**********************************")
    print("Case 3")
    print("Cosmic Deletion: ARID1B_ENST00000275248 c.1_6696del6696 ")
    print("_____________")
    my_text="""This mutation has been found using both DNA microarray and sequencing based analysis of pancreatic cancer genomes according to the study that reported it: 
https://cancer.sanger.ac.uk/cosmic/study/overview?paper_id=45519
Therefore if sequencing was performed the breakpoints are known exactly. 
I would therefore use the following HGVS standard for whole gene deletion:

NC_000023.11:g.(31060227_31100351)_(33274278_33417151)del (microarray example with its probe locations)
    """
    print(my_text)
    print("ENST00000275248.4:g.(1)_(6696)del")
if __name__ == "__main__":
    main()
