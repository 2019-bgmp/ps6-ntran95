#!/usr/bin/env python


file_name1= "/home/ntran2/bgmp/Bi621/PS6/800_3_PE5_interleaved.fq_1"
file_name2="/home/ntran2/bgmp/Bi621/PS6/800_3_PE5_interleaved.fq_2"
file_name3="/home/ntran2/bgmp/Bi621/PS6/800_3_PE5_interleaved.fq.unmatched"

fosmid_lib=50
fosmid_length= 40000
expected_genome_length= fosmid_lib * fosmid_length

#look through each file, go through the lines, calculate how many nucleotides in each line, sum them??
nucleotides_len_file1=[]
with open(file_name1, "r") as fh1:
    i = 0
    for line in fh1:
        i+=1
        line = line.strip('\n')
        if i % 4 == 2:
            #print(len(line))
            nucleotides_len_file1.append(len(line))
print(len(nucleotides_len_file1))

nucleotides_len_file2=[]
with open(file_name2, "r") as fh2:
    i = 0
    for line2 in fh2:
        i+=1
        line2 = line2.strip('\n')
        if i % 4 == 2:
            #print(len(line))
            nucleotides_len_file2.append(len(line2))
print(len(nucleotides_len_file2))

nucleotides_len_file3=[]
with open(file_name3, "r") as fh3:
    i = 0
    for line3 in fh3:
        i+=1
        line3 = line3.strip('\n')
        if i % 4 == 2:
            #print(len(line))
            nucleotides_len_file3.append(len(line3))
print(len(nucleotides_len_file3))


sum_of_nucleotides= sum(nucleotides_len_file1+nucleotides_len_file2+nucleotides_len_file3)
print(sum_of_nucleotides)


coverage=((sum_of_nucleotides)/expected_genome_length)
print(float(coverage))
