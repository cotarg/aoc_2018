#!/usr/bin/env python

import logging


from collections import Counter


def checksum(input_doc_path):
    count_double_char = 0
    count_triple_char = 0

    with open(input_doc_path) as f:
        string_list = f.readlines()

    for line in string_list:
        doubles = False
        triples = False
        char_count = Counter(line.rstrip())
        char_set = set(line)

        for char in char_set:
            if doubles is False and triples is False:
                if char_count[char] == 2:
                    doubles = True
                elif char_count[char] == 3:
                    triples = True
            elif doubles is False:
                if char_count[char] == 2:
                    doubles = True
            elif triples is False:
                if char_count[char] == 3:
                    triples = True
            else:
                break

        if doubles is True:
            count_double_char += 1

        if triples is True:
            count_triple_char += 1

    checksum = count_double_char * count_triple_char

    logging.warning(count_double_char)
    logging.warning(count_triple_char)
    logging.warning(checksum)
    return


checksum("./input.txt")
