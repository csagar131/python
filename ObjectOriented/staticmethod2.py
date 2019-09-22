class FixedFloat:
    def __init__(self,amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount}>'

    @staticmethod
    def cur_sum(value1,value2):
        return FixedFloat(value1+value2)

new_number  = FixedFloat.cur_sum(12.90,1.10)
print(new_number)