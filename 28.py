seq1 ="ATGTTATAG"
newseq1 =''

for s in seq1:
	if s == "A":
		newseq1 += "T"
	elif s == "T":
		newseq1 += "A"
	elif s == "C":
		newseq1 += "G"
	elif s == "G":
		newseq1 += "C"

print(seq1)
print(newseq1)
