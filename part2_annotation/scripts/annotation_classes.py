"""
Pavlos Antoniou
Classes Sample and Warning
for the annotation analysis 
09/08/2021
"""

import re

DIAS_WARNING = "DIAS_SYSTEM_ERROR"
INPUT_WARNING = "INPUT_WARNING"


class Sample:
    """
    Class to hold information about a sample
    and its warning files
    """

    vep_out_path = ""
    dias_path = ""

    def __init__(
        self,
        sampleID,
    ):
        self.sampleID = sampleID

    def extract_lines_related_error(self):
        print(self.warnings.warnings_text)
        with open(self.dias_path, "r") as f:
            flines = f.readlines()
            # print(flines)


class Warning:
    """
    Class to hold information relating to
    the warnings from the VEP run of a sample
    """

    def __init__(self, warning, warning_type):
        self.warning = warning
        self.warning_type = warning_type

    def __str__(self):
        return f"{self.warning_type}: {self.warning}"

    def is_input_error(self):
        if self.warning_type == INPUT_WARNING:
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
        allele_pattern = re.compile("(\w+) length")
        start_stop_pattern = re.compile("co-ordinates (\d+)-(\d+)")
        line_number_pattern = re.compile(" line (\d+)")

        allele = allele_pattern.search(self.warning).group(1)
        (start, stop) = start_stop_pattern.search(self.warning).group(1, 2)
        line_number = line_number_pattern.search(self.warning).group(1)
        self.allele = allele
        self.stop = stop
        self.start = start
        self.line_number = line_number
