seq1 = "ATGTTATAG"
'''
i = []
for i in seq1:
	print (seq1[::3])
'''
				#stop을 문자열길이 만큼줌 
for i in range(0,len(seq1),3):
	#print(i) 0,3,6
	print(seq1[i])#리스트 인덱싱	
