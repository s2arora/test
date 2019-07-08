num1=int(input('num1 ='))
'''
if num1 % 7 == 0:
	print ('num1은 7의배수입니다.')
elif num1 % 3 == 0:
	print ('num1은 3의배수입니다.')
else:
	print ('num1은 3과 7 모두의 배수입니다.')
'''

if num1 % 3 ==0 and num1 % 7 == 0:
	print(num1, "은 3과 7의 배수다.")
elif num1 % 3 == 0:
	print(num1, "은 3의 배수다.")
elif num1 % 7 == 0:
	print(num1, "은 7의 배수다.")
else:
	print(num1, "은 3 또는 7의 배수가 아니다.")

