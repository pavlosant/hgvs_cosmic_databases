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

## Output files
The first tsv file 

```txt
Sample	Warning_Type_from_VEP_output	Warning_from_VEP_output
2910234	INPUT_WARNING	WARNING: Length of reference allele (TCAGA length 5) does not match co-ordinates 29447409-29447421 on line 1

2869929	INPUT_WARNING	WARNING: Length of reference allele (CC length 2) does not match co-ordinates 98218696-98218696 on line 149

1090880	DIAS_SYSTEM_ERROR	WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5a41a58)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5a41a58)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29080)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29080), HASH(0x430d9e0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29080), HASH(0x430d9e0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bcb860)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bcb860)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29320)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29320), HASH(0x5a399a8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29320), HASH(0x5a399a8), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bcbd70)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bcbd70)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a295a8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a295a8), HASH(0x5bcc040)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a295a8), HASH(0x5bcc040), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc0fd8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc0fd8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a247f0)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a247f0), HASH(0x5bc7110)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a247f0), HASH(0x5bc7110), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc6ac8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc6ac8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29830)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29830), HASH(0x5bc1068)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29830), HASH(0x5bc1068), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc05a0)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5bc05a0)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29ab8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x4446050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29ab8), HASH(0x5bc0fc0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5a29ab8), HASH(0x5bc0fc0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8), HASH(0x57c6150)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x57a6ea8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x57a4710), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5790d00), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x4423310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

907313	INPUT_WARNING	WARNING: Length of reference allele (GGCTCCCGGGTTCCCAGATCTCTTCAT length 27) does not match co-ordinates 17494914-17494944 on line 817

909698	INPUT_WARNING	WARNING: Length of reference allele (AA length 2) does not match co-ordinates 70747694-70747701 on line 2339

909698	INPUT_WARNING	WARNING: Length of reference allele (GCTCTGA length 7) does not match co-ordinates 38679764-38679787 on line 2902

910781	INPUT_WARNING	WARNING: Length of reference allele (AA length 2) does not match co-ordinates 70747694-70747701 on line 1972

909753	INPUT_WARNING	WARNING: Length of reference allele (AAGTGGGGCTGCAGGATTGCCCCAGTTTTCAGACCTGTTTCTAATCCAGAGAGGAGAGTCACAGTGCCACTGTCCCCAGGCAGGCAGCACAGTGATCTTTCTAGACATCTCCTCTTCCTTTTTTTTTTTTTTTTTTTTTGAGACAGAGTCTCGCTCTGTCGCCCAGACTAGGGTGCAATAGCACGATCTTGGCTTACTGCAACCTCCACCTCCCAGGTTCAAGCGATTCTCCGGCCTCAGCCTCTTGAGTAGCTGGGATTACAGGCACCCACCATCATGCCGAGCTAATTTCTGTATTTTTGTAGAGATGGGGTTTCACCGTGTTTGCCAGGCTGGTCTCGAACTCCTGACCTCAGGTGATCCACCCGCCTCAGCCTCCCAAAGTGCTGGCATTACAGGCGTGAGCCACCACGCCCAGCCTCCCCTTACTATTTTGTAAGAGGCTTTTGAGAAACAATCCAAGCCCTTACTACCTTAGTTCCTCCTAGAGTTGACTGCACCTCTCGGTTAATGTTGAAGTTTCTGTGGCTCGTCATCTCTGCCTAACTATGCAATTCATTCACTGTTGTATTGGGTTTTTCTGTTTCTTTGTCTATTTGTTTTAGGAAAAAATAGCCCAAAGCTCACTGTGTAATTAG length 638) does not match co-ordinates 62189926-62191454 on line 201

1201903	INPUT_WARNING	WARNING: Length of reference allele (GGAGGA length 6) does not match co-ordinates 170837553-170837557 on line 1

755421	DIAS_SYSTEM_ERROR	WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5b18fb8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5b18fb8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b063f8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b063f8), HASH(0x42f69e0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b063f8), HASH(0x42f69e0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88), HASH(0x57af6e8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5d9a578)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5d9a578)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b05f60)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b05f60), HASH(0x5b23d00)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b05f60), HASH(0x5b23d00), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88), HASH(0x57af6e8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5d8fce8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x5d8fce8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b06698)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x442f050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b06698), HASH(0x5d9a560)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x5b06698), HASH(0x5d9a560), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88), HASH(0x57af6e8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x578ff88)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x578d7f0), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x5779de0), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x440c310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

2824110	INPUT_WARNING	WARNING: Length of reference allele (AT length 2) does not match co-ordinates 128841502-128841508 on line 95

1076116	DIAS_SYSTEM_ERROR	WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x714cb28)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x714cb28)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x51f2050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ad0008)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x51f2050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ad0008), HASH(0x50b99e0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ad0008), HASH(0x50b99e0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08), HASH(0x715d9e8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x71db7c8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x71db7c8)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x51f2050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ce0f30)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x51f2050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ce0f30), HASH(0x71a5a38)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x6ce0f30), HASH(0x71a5a38), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08), HASH(0x715d9e8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x6572d08)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x6570570), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x653cb50), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x51cf310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

1196425	DIAS_SYSTEM_ERROR	WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x4f93438)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x4f93438)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x3258050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x4b2ee98)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x3258050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x4b2ee98), HASH(0x311f9e0)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x4b2ee98), HASH(0x311f9e0), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8), HASH(0x4f65480)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

WARNING: Plugin 'DIAS' went wrong: Attribute (ens_hgvs_notation) does not pass the type constraint because: Validation failed for 'HashRef' with value undef at reader Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation (defined at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 23) line 15, <__ANONIO__> line 1.

	Sanger::Cosmic::Dias::GenomeFormatter::ens_hgvs_notation(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x511d620)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/lib//Sanger/Cosmic/Dias/GenomeFormatter.pm line 209

	Sanger::Cosmic::Dias::GenomeFormatter::wt_allele(Sanger::Cosmic::Dias::GenomeFormatter=HASH(0x511d620)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 299

	DIAS::get_genomic_data(DIAS=HASH(0x3258050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x498bdd0)) called at /nfs/users/nfs_d/data-cosmic/pipeline/dias_annotate/VEP_plugins//DIAS.pm line 116

	DIAS::run(DIAS=HASH(0x3258050), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x498bdd0), HASH(0x4f93828)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1898

	eval {...} called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 1897

	Bio::EnsEMBL::VEP::OutputFactory::run_plugins(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::TranscriptVariationAllele=HASH(0x498bdd0), HASH(0x4f93828), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 356

	Bio::EnsEMBL::VEP::OutputFactory::get_all_VariationFeatureOverlapAllele_output_hashes(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8), HASH(0x4f65480)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 306

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_VariationFeature(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::Variation::VariationFeature=HASH(0x45d8cf8)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 278

	Bio::EnsEMBL::VEP::OutputFactory::get_all_output_hashes_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/OutputFactory.pm line 252

	Bio::EnsEMBL::VEP::OutputFactory::get_all_lines_by_InputBuffer(Bio::EnsEMBL::VEP::OutputFactory::Tab=HASH(0x45d6560), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 416

	Bio::EnsEMBL::VEP::Runner::_buffer_to_output(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310), Bio::EnsEMBL::VEP::InputBuffer=HASH(0x45a2b40), undef) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 364

	Bio::EnsEMBL::VEP::Runner::next_output_line(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310)) called at /software/cosmic/projects/ensembl-vep/modules/Bio/EnsEMBL/VEP/Runner.pm line 202

	Bio::EnsEMBL::VEP::Runner::run(Bio::EnsEMBL::VEP::Runner=HASH(0x3235310)) called at /software/cosmic/projects/ensembl-vep/vep line 224

....
```