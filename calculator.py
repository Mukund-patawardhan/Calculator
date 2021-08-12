class Calculator(object):
    def __init__(self,modal,color,price):
        self.modal = modal
        self.color = color
        self.price = price

    def addition(self,num1,num2):
        sum = num1 + num2
        print(sum)
    def subtraction(self,num1,num2):
        difference = num1 - num2
        print(difference)
    def multiplication(self,num1,num2):
        product = num1 * num2
        print(product)
    def division(self,num1,num2):
        quotient = num1 / num2
        print(quotient)

calc1 = Calculator("Samsung","Black",500)
calc2 = Calculator("Nokia","Black",200)

calc1.addition(2,3)
calc1.subtraction(2,3)
calc1.division(2,3)
calc1.multiplication(2,3)