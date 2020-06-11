import random
start = input('請輸入隨機數字範圍上限: ')
end = input('請輸入隨機數字範圍下限: ')
start = int(start)
end = int(end)

r = random.randint(end, start)
count = 0
while True:
	count = count + 1
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
		print('再猜一次喔!! 數字比',num, '還',ans, '!', '(已猜', count, '遍)')