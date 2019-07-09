with open('test.tsv','r') as fr:
	headerList = fr.readline().strip().split("\t")
	for line in fr:
		l =line.strip().splir("\t")
		print(l)
		id_ =l[0]
		seq =l[1]
		sepecies =1[2]
		if sepecies == "Herpes":
			print(line.strip())
#species가 herpes일때 출력

#	for line in fr:
#		print(line.strip().split(","))
