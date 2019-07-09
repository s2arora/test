#파일을 읽어서 GC_content구하기
def calcGC(s):
	num_c = s.count("C")
	num_g = s.count("G")
	float(num_c +num_g)/len(s) *100
	return gc

s = "" #더해주기 전에 S써줘 한줄로 넣어줘야함 
with open('sequence.txt','r') as fr: #일단은 먼저 읽어줌
	for line in fr: #한줄씩 해서 가는데
		s += line.strip() # 더해줘서 엔터날라감
print (s)
'''
def calcGC(s):
	num_c = s.count("C")
	num_g = s.count("G")
	float(num_c +num_g)/len(s) *100
	return gc
'''
gc = calcGC(s)
print(gc)	
