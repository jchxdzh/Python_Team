#作业一：编写程序计算100以内整数的平方根，保留小数点后2位。

def my_sqrt(x):
	
	#定义两个浮点型变量分别存放 可能取得的最小值和最大值
	low=1.0
	high=x

	#使用二分法进行猜测
	guess = (low + high) / 2
	
	#循环判断guess是否为目标x的保留两位小数的平方根
	while 1:
		if round(guess*guess, 2) == x:
			break
		elif round(guess*guess, 2) > x:
			high = guess
			guess = (low + high) / 2
			continue
		elif round(guess*guess, 2) < x:
			low = guess
			guess = (low + high) / 2
			continue
		else:
			print("出错")
			break
	return guess

x=1.0
result=0.0
while x<=100:
	result=my_sqrt(x)
	print(x,"的平方根为：",round(result, 2), "  ",end="")
	if x%5==0:
		print("")
		x=x+1.0
	else:
		x=x+1.0
