#!/usr/bin/env python

import logging


def first_double_frequency(input_doc_path):
    current_frequency = 0
    previous_frequencies = {0}

    with open(input_doc_path) as f:
        frequency_adjustments = f.readlines()

    # naive approach assuming text file with single value per line
    while True:
        for line in frequency_adjustments:
            current_frequency = current_frequency + int(line)
            if current_frequency in previous_frequencies:
                logging.warning(current_frequency)
                return
            previous_frequencies.add(current_frequency)

    return


first_double_frequency("./input.txt")
