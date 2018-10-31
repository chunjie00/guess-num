import random
start = input('请输入目标数字最小值:')
end = input('请输入目标数字最大值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	answer = input('请输入数字:')
	answer = int(answer)
	count += 1
	if answer == r:
		print('你猜中了!共猜了', count ,'次')
		break
	elif answer > r:
		print('中奖号码比', answer ,'要小')
	elif answer < r:
		print('中奖号码比', answer ,'要大') 
	print('你猜了', count , '次')