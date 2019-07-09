Seq1 ="ATGTTATAG"
comqSeq = ""
compDic = {"A":"T",
		   "C":"G",
		   "G":"C",
		   "T":"A"}

for s in Seq1:
	compSeq += comDic[s]

print(Seq1)
print(compDic)
