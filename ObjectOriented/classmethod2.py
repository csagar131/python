class FixedFloat:
    def __init__(self,amount):
        self.amount = amount
    
    def __repr__(self):
        return f'<FixedFloat {self.amount}>'

    @classmethod
    def cur_sum(cls,value1,value2):
        return cls(value1+value2)


class dollar(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = "$"
    
    def __repr__(self):
        return f'<dollar {self.symbol}{self.amount}>'

    


#new_number  = FixedFloat.cur_sum(12.90,1.10)
new_number = dollar.cur_sum(13.30,1.10)
print(new_number)