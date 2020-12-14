# Generates activity block
# Inspired by https://github.com/athul/athul

import sys
import json
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
language_max_len = max(list(map(lambda x: len(x), times.keys())))

blocks = 30

print('```')
for key in sorted(times, key=times.get, reverse=True):
    value = times[key]
    print(f"{key:{language_max_len}}", "",
          "█" * int(value / total * blocks) + "▒" * int(blocks - value / total * blocks),
          "",
          f"{timedelta(seconds=value)}", "",
          f"{value / total * 100:5.2f}%")
print('```')
