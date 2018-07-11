#Scripts that counts the pairwise match of 2 files line by line and column by column and prints out the %of agreement


#USAGE: ./count_matches.py filea fileb
#redirect to an output file if needed

###N.B. It skips the first field when working on lines and the first line when working on columns (the first line is the ID on the transposed file)

```
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 

import sys 
import os
import time
import numpy as np 
import csv

file1name=sys.argv[1]
file2name=sys.argv[2]

#The 2 files must have the same dimension
#USAGE: ./count_matches file1 file2


with open(file1name) as file1, open(file2name) as file2:
    for line1, line2 in zip(file1, file2):
        line1 = line1.strip().split(' ')[1:]
        line2 = line2.strip().split(' ')[1:]
        if len(line1) != len(line2):
            print('Rows does have not the same dimension')
            break
        #print(line1)
        common = 0
        for i in range (0,len(line1)):
            if line1[i] == line2[i] :
                common +=1
        print(float(common/float(len(line1))))



#This part transpose the file OUT OF CORE. The transposed file it's called 'tmp_transposed'. 

#Transpose out of core function. 
def transpose_csv_out_of_core(inputfile,output_csv,delimiter_in=' ',delimiter_out=' '):
    transposed_iterator = zip(*csv.reader(open(inputfile),delimiter=delimiter_in))
    with open(output_csv, 'w') as out:
        for row in transposed_iterator:
            out.write(delimiter_out.join(row) + '\n')

out="%s_tmp_transposed" % file1name
out1="%s_tmp_transposed" % file2name


transpose_csv_out_of_core(file1name,out)
transpose_csv_out_of_core(file2name,out1)

#######FROM HERE WE WORK WITH COLUMNS

print('From here we count the columns!!!!')

with open(out) as file1, open(out1) as file2:
    for line1, line2 in zip(file1, file2):
        next(file1)
        next(file2)
        line1 = line1.strip().split(' ')[0:]
        line2 = line2.strip().split(' ')[0:]
        if len(line1) != len(line2):
            print('Columns does have not the same dimension')
            sys.exit()
        common = 0
        for i in range (0,len(line1)):
            if line1[i] == line2[i] :
                common +=1
        print(float(common/float(len(line1))))

os.remove(out)
os.remove(out1)
```
