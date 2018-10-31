import random
r = random.randint(1, 100)
while True:
	answer = input('请输入数字:')
	answer = int(answer)
	if answer == r:
		print('你猜中了!')
		break
	elif answer > r:
		print('中奖号码比', answer ,'要小')
	elif answer < r:
		print('中奖号码比', answer ,'要大')