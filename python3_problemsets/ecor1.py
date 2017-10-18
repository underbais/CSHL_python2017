#!/usr/bin/env python3

#finding EcorI sites

seq = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

print('The position of EcoRI site is:\n',seq.find('GAATTC')+1)

fragments = seq.split('GAATTC')
fragment1 = fragments[0] + "G"
fragment2 = 'AATTC' + fragments[1]
print('First fragment is from 1 to', len(fragment1))
print('Second fragment is from', len(fragment1)+1, 'to', len(fragment1)+len(fragment2)+1)

#print('Fragment\tPosition\tLength\n',fragment1,'1',len(fragment1),'\n', fragment2, len(fragment1)+1, len(fragment1)+len(fragment2))

table = 'Fragment\tPosition\tLength\n{}\t{}\t{}\n{}\t{}\t{}'
report = table.format(fragment1,'1',len(fragment1),fragment2,len(fragment1)+1,len(fragment1)+len(fragment2))

print(report)

all_fragments = [fragment1,fragment2]
all_fragments_sorted = sorted(all_fragments, key=len)

print("Fragments list sorted by length:\n",all_fragments_sorted)
