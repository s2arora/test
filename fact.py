def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)#다시 자기 자신을 호출

result = fact(5)
print(result)

#피보나치 서열:
def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n-2) +fib(n-1)

for i in range(1,11,1):
	print(i,fib(i))
