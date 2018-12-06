#!/usr/bin/env python

import logging


def resulting_frequency(input_doc_path):
    current_frequency = 0

    # naive approach assuming text file with single value per line
    with open(input_doc_path) as f:
        for line in f.readlines():
            current_frequency = current_frequency + int(line)

    logging.warning(current_frequency)
    return

resulting_frequency("./input.txt")
