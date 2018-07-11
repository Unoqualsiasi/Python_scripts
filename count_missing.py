##Function to count the percentage of missing genotypes. It can be used to calculate specific occurencies. Line iterator. Can be used with large files

##USAGE : ./count_missing.py input_file

```
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*- 

import sys
import os

firstarg=sys.argv[1]



f = open(firstarg, "r")
g = open("file_culo", "w")

for line in f:
    if line.strip():
        g.write(" ".join(line.split()[1:]) + "\n")

f.close()
g.close()    

def perc_missing():
    file  = open('file_culo', 'r').read()
    missing  = input("Put the label for the missing values:")
    first = input("Put the label for the first  homo genotype:")
    second = input("Put the label for the second homo genotype:")
    third = input("Put the label for the hetero genotype:")

    count = file.count(missing)
    count1 = file.count(first)
    count2 = file.count(second)
    count3 = file.count(third)
    
    percentage_missing = float(count) / float(count + count1 + count2 + count3)
    
    print('The percentage of missing genotypes after the imputation is....',percentage_missing)

perc_missing()

os.remove('file_culo')
```

