import random

r = random.randint(1, 10)
while True:
	num = input('請猜一個數字(1~10): ')
	num = int(num)
	if  r - num < 0 :
		ans = '小'
	else:
		ans = '大'
	if num == r:
		print('猜對了喔! ')
		break
	else:
		print('再猜一次喔!! 數字比',num, '還',ans, '!')

