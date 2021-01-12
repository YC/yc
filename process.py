# Generates activity block
# Inspired by https://github.com/athul/athul

import sys
from collections import defaultdict
from datetime import timedelta

# dict for storing times
times = defaultdict(int)

# determine/merge times
for line in sys.stdin:
    line_split = line.split(',')
    language = line_split[0]
    time = int(line_split[1])

    # less than 15 minutes
    if time < 60 * 15:
        times['other'] += time
        continue

    # unknown
    if language == 'unknown':
        times['other'] += time
        continue

    # set time
    times[language] = time

total = sum(times.values())
max_time = max(times.values())
language_max_len = max(list(map(lambda x: len(x), times.keys())))

blocks = 25

print('```')
for key in sorted(times, key=times.get, reverse=True):
    # get value
    value = times[key]

    # determine number of blocks
    num_blocks = value / max_time * blocks
    (whole_blocks, rem) = (int(num_blocks // 1), num_blocks % 1)

    # fractional
    medium_blocks = 0
    light_blocks = 0
    if rem > 0.66:
        medium_blocks = 1
    elif rem > 0.33:
        light_blocks = 1

    print(f"{key:{language_max_len}}", "",
          "▓" * whole_blocks
          + " " * medium_blocks
          + " " * light_blocks
          + " " * (blocks - whole_blocks - medium_blocks - light_blocks),
          "",
          # f"{timedelta(seconds=value)}", "",
          f"{value / total * 100:5.2f}%")
print('```')
