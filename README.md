# hgvs_cosmic_databases
# Intoduction
This repository contains script sfor analysing the format of genomic annotations.
To obtain the code please type:
```
mkdir hgvs_cosmic_databases
git init
git pull https://github.com/pavlos-pa10/hgvs_cosmic_databases.git
``` 

# Part 1
Methods to create valid HCVS compliant mutation definitions.

# Part 2
# Annotation warnings from vep output
## Classes
I created two classes to help me analyze the folders with the files containing the vep_annotations and dias_extracts. 

![alt text](https://github.com/pavlos-pa10/hgvs_cosmic_databases/blob/main/part2_annotation/img/classes_cosmic_annotation.png?raw=true)
### Class Sample: 
sampleID : the sampleID take from the filename \
vep_out_path: path to the file from the vep_output_sample_* relating to this sample \
dias_path: path to the file from the dias_extract_sample_126 

### Class Warning
This class holds the information for all the warnings of each sample. \
Each sample can have zero or many warnings. \
warning: the text of the warning \
warning_type: if it is a DIAS_SYSTEM_ERROR or INPUT_WARNING \
allele: The allele that caused input warning (INPUT_WARNING only) \
start: The start position of the input warning (INPUT_WARNING only) \
stop: The stop position of the input warning (INPUT_WARNING only) \
line_number: The line number as recorded in the input warning message (INPUT_WARNING only)

## How to run 
### Input parameters 
The input is the path to the folder `vep_output_sample_*` and 
the path to the `dias_extract_sample_*` folder. 

Some default values related to the location in script are provided within the script ("part2_annotation/grch37_vep_output_sample_126" and "part2_annotation/grch37_dias_extract_sample_126") 
### Output parameters
The output of the script consists of two tsv files. 
The user can define the name and path of this output files. 
The default values are "part2_annotation/output_files/1.samples_with_warnings.tsv" and "part2_annotation/output_files/2.samples_with_input_warnings_and_dias_extracted_lines.tsv"
### Execution
```bash
python3 part2_annotation/scripts/analyse_warnings.py  --help
usage: analyse_warnings.py [-h] [--vep_folder VEP_FOLDER]
                           [--dias_folder DIAS_FOLDER]
                           [--warnings_output_file1 WARNINGS_OUTPUT_FILE1]
                           [--warnings_output_file2 WARNINGS_OUTPUT_FILE2]

optional arguments:
  -h, --help            show this help message and exit

Input parameters:
  --vep_folder VEP_FOLDER
                        Full path of vep_output folder.
  --dias_folder DIAS_FOLDER
                        Full path of dias extract folder

Output parameters:
  --warnings_output_file1 WARNINGS_OUTPUT_FILE1
                        Full path of file to write the samples with warnings
                        from vep_output and their warnings
  --warnings_output_file2 WARNINGS_OUTPUT_FILE2
                        Full path of file to write the samples with INPUT_type
                        warnings and the line from the dias_extract files that
                        corresponds to the warning

```
