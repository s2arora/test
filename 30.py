Seq1 = "AGTTTATAG"
'''
import re
p = re.compile('TT')
m = p.findall(Seq1)

print (m)
'''

print(Seq1)
print("index",Seq1.index('TT'))
print("find",Seq1.find('TT'))#find는 한번 찾아버리면 끝남

#3개씩 읽지 말고 한개씩 읽기
for i in range(0,len(Seq1),1):
	print (i, Seq1[i]) #서열이 01234순으로감
	print (i, i+2, Seq1[i]) #하나씩 밀음
	if s == "TT":
		print(i)	# 2,3  나옴
