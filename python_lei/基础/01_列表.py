list1 = [ 1,1 , 2, 3]#索引从左往右从0开始
list1.append(4)#向列表的尾部追加元素
print(list1)
list1.remove(4)#删除列表中第一个匹到的值
print(list1)
list1.pop(0)#删除列表中指定索引位置元素，若无索引，默认删除最后一个
print(list1)
list1.insert(3,4)#在指定索引前插入元素
print(list1)
list1.reverse()#反转列表元素
print(list1)
list1.sort()#对列表进行排序，要求元素数据类型一致
print(list1)