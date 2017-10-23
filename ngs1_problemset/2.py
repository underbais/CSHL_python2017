#!/usr/bin/env python3


header=''
seq=''
comment=''
qual=''
#pfb_trimmed20 = =open("trimmed.fastq", "w")
with open("pfb.fastq", "r") as fastq:
	for index,line in enumerate(fastq):
		if index%4==0:
			header = line
		elif index%4==1:
			line = line.rstrip("\n")
			seq = line
		elif index%4==2:
			comment = line			
		elif index%4==3:
			for pos,base in enumerate(line):
				if ord(base) - 33 < 20:
					seq = seq[0:pos]
					line = line.strip("\n")
					qual = line[0:pos]
					print(header,seq, '\n',comment, '\n',qual)
					break
#		pfb_trimmed20.write(header,seq,"\n",comment,'\n',qual)
#pfb_trimmed20.close()
