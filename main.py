from __future__ import print_function

import json
import argparse
import random

parser = argparse.ArgumentParser(description='randomly combine several attributes')
parser.add_argument('params', metavar='FILE', nargs=1, help='file containing generation parameters')
args = parser.parse_args()

with open(args.params[0]) as f:
    data = json.load(f)

print('generating "{}"'.format(data['name']))

generated_params = {name: random.choice(values) for name, values in data['parameters'].items()}
name_lengths = [len(name) for name in generated_params.keys()]
max_name_len = max(name_lengths)

for k, v in sorted(generated_params.items()):
    print('\t{} \t{}'.format(k.ljust(max_name_len + 1, ' '), v))
