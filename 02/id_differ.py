#!/usr/bin/env python3

import logging
from itertools import combinations, compress


def id_differ(input_doc_path):

    with open(input_doc_path) as f:
        string_list = f.readlines()

    for id_one, id_two in combinations(string_list, 2):
        diff = [char_1 == char_2 for char_1, char_2 in zip(id_one, id_two)]
        if sum(diff) == (len(id_one) - 1):
            id_common_chars = ''.join(list(compress(id_one, diff)))
            break

    logging.warning(id_common_chars)
    return

id_differ("./input.txt")
