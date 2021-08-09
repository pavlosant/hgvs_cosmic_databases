"""
Pavlos Antoniou
08/08/2021
Annotation analysis for COSMIC vep annotation pipeline
"""

import pathlib
from pathlib import Path
import argparse
import part1_funtions as part1_functions
import part2_funtions as part2_functions


def main(args):
    """
    Part 1
    """
    samples_with_warnings = part1_functions.part1_analysis(
        args.vep_folder, args.warnings_output_file1
    )

    """
    Part 2
    """
    part2_functions.part2_analysis(
        samples_with_warnings, args.dias_folder, args.warnings_output_file2
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    input_params = parser.add_argument_group("Input parameters")
    output_params = parser.add_argument_group("Output parameters")
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
