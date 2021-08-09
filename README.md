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
`
`
