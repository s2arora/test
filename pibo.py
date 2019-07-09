#피보나치 서열:

import sys
num =int(sys.argv[1])
def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-2) +fib(n-1)
print (fib(num))
#for i in range(1,11,1):
#	print(i,fib(i))
'''

li [0,1]
for i in range(998): #1000번째까지 나옴
	val = li[-2]+ li[-1]
	li.append()
print(li)
'''
