li = [3,1,1,2,0,0,2,3,3]
l="ATGCAAGTCATGGATC"
ll = "RKAAPLLOVV" #아미노산 서열ㅑ
# 딕셔너리 key를 등록을 하지않고도 사용가능할 수 있는 장점
d = {} #빈사전 KEY: number , VALUE: frequency

#d ["A"]=1
#>>>d
#{'A':1}
for i in li:
	print(i,d)
	if i in d:
		d[i] += 1
	else:	#if에서 없으면 else로 넘어감
		d[i] = 1	#1을 더해줌

print (d)

for k,v in d.items():
	print (k,v)
