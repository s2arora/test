li = [3,1,1,2,0,0,2,3,3,]
#max_val = 0
#min_val = 10000000
for i in range(0,len(li),1):
	if i == 0:	#set max_val, min_val
		max_val =li[i]
		min_val =li[i]
	else:
		if max_val < li[i]:
			max_val = li[i] #max_val change
		if min_val > li[i]:
			min_val = li[i] #min_val change

print ("max: ", max_val)
print ("min: ", min_val)
print ("---")
#파이썬 내장함수 2줄이면 됨 변수내에서 가장 크고 작은 값을 골라줌
print ("max: ", max(li))
print ("min: ", min(li))
