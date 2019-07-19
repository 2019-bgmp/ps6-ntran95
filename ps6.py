#!/usr/bin/env python
import re
import argparse
#importing reg ex to look through the header pattern

def get_arguements():
    parser = argparse.ArgumentParser(description="reading in different files")
    parser.add_argument("-f", "--file_name", help="this argument specifies the filename", type =str, required=True)
    return parser.parse_args()

args=get_arguements()
f=args.file_name

list_of_physical_contig=[]
list_of_coverge_in_blue = []
contigs_n50=[]
number_of_contigs=0
#f = "/Users/GioiTran/Documents/shell/ps6-ntran95/contigs.fa"
with open(f, "r") as fh:
    i=1
    for line in fh:
        #look through the contig file and parse for the following:
        #>NODE_11_length_3717_cov_19.315845
        pattern = r'^>NODE_\d+_length_(\d+)_cov_(\d+\.\d+)$'
        pattern = re.findall(pattern, line)
        #pattern = re.match(pattern, line) #creates tuple, want only the tuples with numbers
        i+=1

        #print(pattern)

        header_counter =0
        for char in pattern:
        #look at the kmer length in the pattern
            kmer_length= char[0]
            kmer_length = int(kmer_length)
        #printing coverage length
            cov = char[1]
            cov = float(cov)
            list_of_coverge_in_blue.append(cov)
            #print(list_of_coverge_in_blue)

            physical_length= kmer_length + 48

            list_of_physical_contig.append(physical_length)
            list_of_physical_contig.sort()


            contigs_n50.append(physical_length)
            contigs_n50.sort(reverse=True)


            header_counter +=1
            number_of_contigs+=1

'''  Adjust the k-mer length to represent the physical length. Calculate the number of
contigs, the maximum contig length, the mean contig length, and the total length of the
genome assembly across the contigs. Calculate the mean depth of coverage for the   '''

#print("The list of physical contig is:", list_of_physical_contig)
print("The maximum length of the contigs is:", list_of_physical_contig[-1])
print("The mean contig length is:", sum(list_of_physical_contig)/ number_of_contigs)
genome_length= sum(list_of_physical_contig)
coverage_depth = (sum(list_of_coverge_in_blue)/number_of_contigs)

#print(genome_length)
print("The total length of the genome assembly across the contigs is:", sum(list_of_physical_contig))
print("The mean depth of coverage for the contigs is:", coverage_depth)

print("Number of contigs is:" ,number_of_contigs)

''' Calculate the N50 value of your assembly, use list contigs_n50  '''
#print(contigs_n50)
total = 0
for contigs in contigs_n50:

    total+=contigs
    #print(total)
    #print(contigs)
    if total >= sum(contigs_n50)/2:
        N50=contigs
        break
print("The N50 is:", contigs)

'''  Calculate the distribution of contig lengths and bucket the contig lengths into groups of
100bp. So, all contigs with lengths between 0 and 99 would be in the 0 bucket, those
with lengths between 100 and 199 would be in the 100 bucket, etc.  '''

bucket_dict={}

for values in range(0, 50000, 100):
    bucket_dict.setdefault(values, 0)

for x in list_of_physical_contig:
    if (x//100)*100 in bucket_dict:
        bucket_dict[(x//100)*100]+=1

#print(bucket_dict)

''' Print out the distribution. '''
print("# Contig length" +"\t"+ "Number of contigs in this category")
for keys in sorted(bucket_dict):
     print("%d%s%d" %(keys, "\t", bucket_dict[keys]))
