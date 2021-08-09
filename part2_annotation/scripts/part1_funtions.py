"""
Pavlos Antoniou
Part 1 functions
09/08/2021
"""
import pathlib
import re
import csv
from pathlib import Path
from annotation_classes import Sample
from annotation_classes import Warning

DIAS_WARNING = "DIAS_SYSTEM_ERROR"
INPUT_WARNING = "INPUT_WARNING"


def extract_sample_name(path):
    """
    Extracts and returns the sample ID
    from the filename
    """
    sample = path.name.split(".")[0]
    return sample


def extract_warnings(pathname):
    """
    Reads and extrancts info from warning file
    checks if it is an input warning or a Dias system error warning
    saves the warning as a new Warning object
    saves the Warning (object) to its corresponding Sample (object)
    """
    warnings_list = []
    warnings = []

    with open(pathname, "r") as f:
        for line in f.readlines():
            if line.startswith("WARNING: Length of reference"):
                warning = line
                warning_type = INPUT_WARNING
                w = Warning(warning, warning_type)
                w.get_input_error_coordinates()
                warnings.append(w)
            else:
                warnings_list.append(line)

        if len(warnings) == 0:
            warnings_text = "\n".join(warnings_list)
            warning_type = DIAS_WARNING
            w = Warning(warnings_text, warning_type)
            warnings.append(w)
        return warnings


def part1_analysis(vep_folder, outfolder):

    p = Path(vep_folder)
    # Get all warning file names
    warning_files = list(p.glob("*_warnings.txt"))
    sample_list = get_sample_information_from_vep_files(warning_files)
    part1_print_to_file(outfolder, sample_list)
    return sample_list


def get_sample_information_from_vep_files(warning_files_list):
    sample_list = []
    for p in warning_files_list:
        # Extract sample name from filename
        sample = extract_sample_name(p)
        # Create a new object of class Sample
        s = Sample(sampleID=sample)
        s.vep_out_path = p
        # Get all warnings related to sample s and save them to object s
        s.warnings = extract_warnings(p)
        # add sample to the global sample list to use later
        sample_list.append(s)
    return sample_list


def part1_print_to_file(output_file, samples):
    with open(output_file, "w") as outf:
        outf.write("Sample\tWarning_Type_from_VEP_output\tWarning_from_VEP_output\n")
        for s in samples:
            for w in s.warnings:
                outf.write(f"{s.sampleID}\t{w.warning_type}\t{w.warning}\n")


def extract_sample_name(path):
    """
    Extracts and returns the sample ID
    from the filename
    """
    sample = path.name.split(".")[0]
    return sample


def extract_warnings(pathname):
    """
    Reads and extrancts info from warning file
    checks if it is an input warning or a Dias system error warning
    saves the warning as a new Warning object
    saves the Warning (object) to its corresponding Sample (object)
    """
    warnings_list = []
    warnings = []

    with open(pathname, "r") as f:
        for line in f.readlines():
            if line.startswith("WARNING: Length of reference"):
                warning = line
                warning_type = INPUT_WARNING
                w = Warning(warning, warning_type)
                w.get_input_error_coordinates()
                warnings.append(w)
            else:
                warnings_list.append(line)

        if len(warnings) == 0:
            warnings_text = "\n".join(warnings_list)
            warning_type = DIAS_WARNING
            w = Warning(warnings_text, warning_type)
            warnings.append(w)
        return warnings
