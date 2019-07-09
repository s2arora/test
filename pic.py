import pickle

with open("data.pikle","wb") as fw:
	with open("test.tsv") as fr:
		for line in fr:
			l = line.strip().split("\t")
			if l[2] == "Herpes":
				pickle.dump(l,fw)
