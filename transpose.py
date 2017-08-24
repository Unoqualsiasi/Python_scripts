##Script to transpose out of core. TO be used when the file doesn't fit in memory.

## USAGE : ./transpose.py input_file output_file

#!/usr/bin/env python3.6

import csv
import sys
import os


input=sys.argv[1]
output=sys.argv[2]


def transpose_csv_out_of_core(csv_path=input, output_csv_path=output,delimiter_in=' ',delimiter_out=' '):
	transposed_iterator = zip(*csv.reader(open(csv_path),delimiter=delimiter_in))
	with open(output_csv_path, 'w') as out:
		for row in transposed_iterator:
			out.write(delimiter_out.join(row) + '\n')


transpose_csv_out_of_core()
