seq1 = "ATGTTATAG"

print (seq1[::-1])

revseq1 = "" #문자열 만들어놓고
for i in range(len(seq1)-1,-1,-1):
	print(i)
#stop이 -1이 되면 하나씩 빠짐
	revseq1 +=seq1[i]
print (revseq1)
