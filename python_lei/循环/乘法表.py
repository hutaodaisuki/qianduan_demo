for i in range(1,10):#行数
    for j in range(1,i+1):#列数
        print(f"{j}'*'{i}={i*j}   ",end='')
        '''Python 的 print() 函数默认自带换行，核心参数：
end：控制输出结尾的字符，默认值是 end='\n'（换行符）
只要你手动给 end 赋值（不管是什么内容），就会覆盖默认的换行符，所以：
end='' → 结尾什么都不加，不换行
end='\t' → 结尾加制表符（Tab 空格），也不换行'''

    else:
        print()
# break跳出循环，else不会执行
# continue 结束当前循环，进入下一循环