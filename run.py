#!/usr/bin/env python3

import subprocess
import argparse

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("scale", type=float)

args = ap.parse_args()


if args.ratio == 1.0:
    p = subprocess.run(['random_phase_noise', 'input_0.png', 'output.png'])
else:
    p = subprocess.run(['random_phase_noise', '-r', str(args.ratio), 'input_0.png', 'output.png'])
