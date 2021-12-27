# 计算根号x的值
x = 2
# 在不引入虚数的前提下小于0的数没有平方根
if x < 0:
    print('ERROR')
else:
    # 设置精度要求
    wuqiongxiao = 0.001
    a = x / 2
    if a<wuqiongxiao:
        a = wuqiongxiao
    # 最多迭代40000次，防止陷入死循环
    for i in range(40000):
        b = x / a
        delta = a - b
        a = (a + b) /2
        if delta < 0:
            delta = -1*delta
        # 若满足误差条件，则退出循环
        if delta <= wuqiongxiao:
            break
# 输出最终结果
print(a)