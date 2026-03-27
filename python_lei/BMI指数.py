class Calculate_bmi:
    def __init__(self):#括号里带参数意味着：创建类的实例时必须提供对应的实际参数值，传参
        self.height = 0
        self.weight = 0
        self.bmi = 0

    def calculate_bmi(self):
        self.weight = input('请输入体重(kg):')
        self.height = input('请输入身高(m):')
        self.bmi = float(self.weight) / float(self.height) ** 2
        print(f'您的BMI指数是{self.bmi}')
        print(f'\n您的身体健康状况是{self.judgment()}')
    def judgment(self):
        if self.bmi < 18.5:
            return '偏瘦'
        elif self.bmi < 23.9 :
            return '正常'
        elif self.bmi < 27.9:
            return '超重'
        else:
            return '肥胖'


C_b = Calculate_bmi()
C_b.calculate_bmi()






