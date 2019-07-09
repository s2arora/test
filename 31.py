Seq1 = "AA,AC,AG,AT"
Seq1List = Seq1.split(",")
print (Seq1List)	#리스트로 만듬
#반대로하는 법
#string.join(list)
s ="***".join(Seq1List)
	#"***"이문자를 기준으로 문자열을 합쳐줌
print (s)


s = "chr1	12345	A	C"
l = s.split("\t")
print (l)
