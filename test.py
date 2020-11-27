#coding=UTF-8 
print("Python Hello, World!")

list1 = ["a", "b", "c"]
print(list1)
list1.append('d')
print(list1)
# print('list = ',list)
print('长度' + str(len(list1)))
print('长度 = %d' % len(list1))

number = 34
'''
1、整数的输出
%o —— oct 八进制
%d —— dec 十进制
%x —— hex 十六进制

2、浮点数输出
%f ——保留小数点后面六位有效数字
　　%.3f，保留3位小数位
%e ——保留小数点后面六位有效数字，指数形式输出
　　%.3e，保留3位小数位，使用科学计数法
%g ——在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
　　%.3g，保留3位有效数字，使用小数或科学计数法
3、字符串输出

%s
%10s——右对齐，占位符10位
%-10s——左对齐，占位符10位
%.2s——截取2位字符串
%10.2s——10位占位符，截取两位字符串

'''
print('这个数是: %d %s' % (number, "A"))
print('右对齐，取20位，不够则补位%20s' % 'hello world')  # 右对齐，取20位，不够则补位
print('左对齐，取2位%-10.2s' % 'hello world')  # 左对齐，取2位
print('带数字编号{1} {0}'.format('hello', 'world'))  # 带数字编号
