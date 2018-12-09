#!/usr/bin/env python

# sample loglines:
# [1518-03-25 00:01] Guard #743 begins shift
# [1518-09-15 00:34] falls asleep
# [1518-10-11 00:27] wakes up

import logging
import re

from collections import defaultdict
from collections import Counter


def parser(input_doc_path):
    with open(input_doc_path) as f:
        guard_log = f.readlines()

    guard_log = [logline[1:-1] for logline in guard_log]
    guard_log = sorted_nicely(guard_log)

    guard_duration_dict = defaultdict(int)
    guard_sleep_minutes_dict = defaultdict(int)

    guard_id = 0
    sleep_flag = False
    start_minutes = 00

    # build dictionary of guards and max sleep durations each
    for logline in guard_log:
        if logline is not None:
            chunked_logline = _chunk_line(logline)
            list_counts = Counter(chunked_logline)

            if list_counts['begins'] == 1:
                if sleep_flag is True:
                    end_minutes = _parse_minutes(chunked_logline)
                    sleep_range = range(start_minutes, end_minutes)
                    _create_or_update_guard(
                        guard_duration_dict, guard_sleep_minutes_dict, guard_id, sleep_duration, sleep_range) # noqa
                guard_id = _parse_guard(chunked_logline)
                sleep_flag = False

            if list_counts['asleep'] == 1:
                start_minutes = _parse_minutes(chunked_logline)
                sleep_flag = True

            if list_counts['wakes'] == 1:
                end_minutes = _parse_minutes(chunked_logline)
                sleep_range = range(start_minutes, end_minutes)
                sleep_duration = _calculate_duration(
                    start_minutes, end_minutes)
                _create_or_update_guard(
                    guard_duration_dict, guard_sleep_minutes_dict, guard_id, sleep_duration, sleep_range) # noqa
                sleep_flag = False

    # find upper limit in dictionary
    sleepiest_guard = max(guard_duration_dict, key=guard_duration_dict.get)
    duration = guard_duration_dict[sleepiest_guard]
    best_minute = _find_best_minute(sleepiest_guard, guard_sleep_minutes_dict)

    solution = sleepiest_guard * best_minute

    logging.warning("PROBLEM 1")
    logging.warning("***")
    logging.warning(sleepiest_guard)
    logging.warning(duration)
    logging.warning(best_minute)
    logging.warning(solution)
    logging.warning('***')
    logging.warning('')
    logging.warning('')

    _find_sleepiest_minute(guard_sleep_minutes_dict)
    return


def _find_best_minute(guard_id, guard_sleep_minutes_dict):
    sleep_range = guard_sleep_minutes_dict[guard_id]
    return max(sleep_range, key=sleep_range.count)


def _find_sleepiest_minute(guard_sleep_minutes_dict):
    guard_id = 0
    sleepiest_minute = 0
    sleep_times = 0

    for guard in guard_sleep_minutes_dict:
        guard_sleep_minutes_counter = Counter(guard_sleep_minutes_dict[guard])
        for k in guard_sleep_minutes_counter:
            if guard_sleep_minutes_counter[k] > sleep_times:
                guard_id = guard
                sleepiest_minute = k
                sleep_times = guard_sleep_minutes_counter[k]

    logging.warning("PROBLEM 2")
    logging.warning("***")
    logging.warning(guard_id)
    logging.warning(sleepiest_minute)
    logging.warning(guard_id * sleepiest_minute)
    logging.warning('***')
    return


def _create_or_update_guard(guard_duration_dict, guard_sleep_minutes_dict, guard_id, duration, sleep_range): # noqa
    if guard_duration_dict[guard_id]:
        guard_duration_dict[guard_id] += duration
        for minute in sleep_range:
            guard_sleep_minutes_dict[guard_id].append(minute)
    else:
        guard_duration_dict[guard_id] = duration
        guard_sleep_minutes_dict[guard_id] = sleep_range
    return


def _chunk_line(line):
    return line.split()


def _parse_guard(chunked_logline):
    return int(chunked_logline[3][1:])


def _parse_minutes(chunked_logline):
    return int(chunked_logline[1][3:-1])


def _calculate_duration(start_minutes, end_minutes):
    return end_minutes - start_minutes


def sorted_nicely(l):
    def convert(text): return int(text) if text.isdigit() else text

    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


parser('./04/input.txt')
