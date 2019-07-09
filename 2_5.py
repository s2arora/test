import myModule

with open('test.tsv','r') as fr:
	headerList = fr.readline().strip().split("\t")
	for line in fr:
		l =line.strip().split("\t")
		print(l)
		id_ =l[0]
		seq =l[1]
		sepecies =l[2]
		if sepecies == "Herpes":
			#print(line.strip())
			gc = myModule.calcGC(seq)
			print (gc)
#species가 herpes일때 출력

#	for line in fr:
#		print(line.strip().split(","))
