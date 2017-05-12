print('===============冒泡排序=============')
n = int(input('数组元素个数: '))
l = []
for i in range(n):
	a = int(input('输入第%d 个元素: ' % (i + 1)))
	l.append(a)

for i in range(n):
	j = 0
	while j + i < n - 1:
		if l[j] > l[j + 1]:
			l[j], l[j + 1] = l[j + 1], l[j]
		j += 1

print('排序后列表:', l)

print('===============插入排序=============')
