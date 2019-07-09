with open ('test.txt', 'r') as fr:
	#l = fr.readlines() #이렇게 하면 l에 다 올라가 버림  -비효율적인 램사용
	for line in fr:		#for문으로 한줄씩 객체를 넘겨줌
		print(line.strip())
