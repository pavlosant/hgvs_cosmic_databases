"""
Pavlos Antoniou
Part 2 functions
09/08/2021
"""
import pathlib
import re
import csv
from pathlib import Path
from annotation_classes import Sample
from annotation_classes import Warning
from part1_funtions import extract_sample_name

DIAS_WARNING = "DIAS_SYSTEM_ERROR"
INPUT_WARNING = "INPUT_WARNING"


def part2_analysis(samples, dias_folder, output_file):
    dias = Path(dias_folder)
    dias_files = list(dias.glob("*.tsv"))
    # Associate each dias_extract file with its Sample object that it belongs to
    samples_with_dias_info = get_sample_info_from_dias_files(samples, dias_files)
    # Find matching line in dias_extract file that refers to the VEP_output input warning for that Sample
    samples_with_problem_line = find_problem_line_from_dias_files(
        samples_with_dias_info
    )
    # Print to output file
    part2_print_to_file(output_file, samples_with_problem_line)


def get_sample_info_from_dias_files(sample_list, dias_files):
    # Associate each dias_extract file with its Sample object that it belongs to
    for f in dias_files:
        sampleID = extract_sample_name(f)
        for sample in sample_list:
            if sample.sampleID == sampleID:
                sample.dias_path = f
    return sample_list


def find_problem_line_from_dias_files(sample_list):
    for s in sample_list:
        for w in s.warnings:
            if w.warning_type == INPUT_WARNING:
                w.problem_line = match_line(s.dias_path, w.start, w.stop)
    return sample_list


def part2_print_to_file(output_file, samples):
    with open(output_file, "w") as outf:
        outf.write(
            f"Sample\tWarning_from_VEP_output\tCorresponding_Line_from_Dias_extract_file\tVep_output_warning_file\tDias_extract_file\n"
        )
        for s in samples:
            for w in s.warnings:
                if w.warning_type == INPUT_WARNING:
                    outf.write(
                        f"{s.sampleID}\t{w.warning}\t{w.problem_line}\t{s.vep_out_path}\t{s.dias_path}\n"
                    )


def match_line(filename, start, stop):
    """
    Matches start and stop coordinates with the
    line in the filename (dias output file) that has these coordinates
    returns the line that has these start and stop positions
    """
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            if row[1] == start and row[2] == stop:
                return "\t".join(row)
