#Script that calculates the MAF from genotypes
#The scripts works out of core. The size of the input file is not a limitation.

##USAGE : ./maf_calculation.py input_file number_chromosome

#INPUT : file with genotypes (0,1,2) nrow == number of individuals ncols == number of snps. Missing values encoded as 9. The first column must contain the ID of the individual
#OUTPUT : file with a MAF value for each snp column


```
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 


#SCRIPT OUT OF CORE. NO FILESIZE LIMITS.
import sys
import os
import csv
import time

#Funzione per calcolare MAF e creare il plot dai dati imputati con AI. 
#Input dati imputati e vettore delle correlazioni e output plot MAF

#Dataset in and chr number
firstarg=sys.argv[1]
nchr = int(sys.argv[2])

#Calculate MAF and print out a temp file. Takes imputed as input give MAF as output (Ncolums, MAF) dove ncol è il numero di colonne -1 (ID)

start_time = time.time()

#Transpose out of core function. 
def transpose_csv_out_of_core(inputfile,output_csv='tmp_transposed',delimiter_in=' ',delimiter_out=' '):
    transposed_iterator = zip(*csv.reader(open(inputfile),delimiter=delimiter_in))
    with open(output_csv, 'w') as out:
        for row in transposed_iterator:
            out.write(delimiter_out.join(row) + '\n')

#transpose the file
transpose_csv_out_of_core(firstarg)

#transpose_csv_out_of_core('prova')



#Now...the freaking AI put some trailing spaces...this means that in the transposed file i am gonna have an header with those spaces
#Function to avoid blank lines. It maps only the line that are not empty. Generator to save memory.
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

#Calculate number of animals : read the first nonblank line (line2) and count everything except the spaces. This works only because we don't have double digits numbers
with open('tmp_transposed') as f:
    next(f)
    for i,line in enumerate(nonblank_lines(f)):
        if i ==1 :
            n_anim = sum(c != ' ' for c in line)
        elif i > 1:
            break
print("The number of animals is",n_anim)






#Main function . Iteratore per riga sul file transposto.Quindi itera per colonne. Skippo la prima riga (ID)
#Main function. Row iterator on the transposed file.

outfile = open("maf_ch%d" % nchr,'w')
print(outfile)

with open("tmp_transposed",'r') as f:
    for i,col in enumerate(nonblank_lines(f)):
        if i == 0 :
            pass
        else :
            count0 = col.count("0")
            count2 = col.count("2")
            count1 = col.count("1")
            #count also the missing values!!!
            count9 = col.count("9")
            #Calculate MAF
            n = float(count0+count1+count2)
            p = float((2*count0)+count1)/float(2*n)
            q = float(1 - p)
            maf = str(min(p,q))
            #maf = float(min(count0,count2)*2 + count1)/float(2*n_anim)

            maf = str(maf)
            #print("For the col",i, 'the minor allele freq is', maf)
            outfile.write(maf + " " + "\n")


outfile.close()

print('The number of animals in the file is',n_anim)

os.remove('tmp_transposed')



print("Time to execute the script--- %s seconds ---" % (time.time() - start_time))

```
