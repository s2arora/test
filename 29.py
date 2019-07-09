Seq1 ="ATGTTATAG"
'''
import re
p = re.compile('C')
m = p.match(Seq1)

print (m)
'''

for s in Seq1:
	b = (s == "C")#불리언False나온걸 그냥 받아줌
	print (s, b)
	if b:
		break

'''대화형모드
"C" in Seq1 -> False로 나옴
"T" in Seq1 -> True
'''
	#index값 출력해줌
Seq1.find("C") -> -1 없으면 음수로 나옴
Seq1.find("T") -> 2

Seq1.index("C") -> 없으면 오류가남
Seq1.index("A") -> 




