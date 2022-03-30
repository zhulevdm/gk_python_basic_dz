class Complex:
    
    def __init__(self, real_num, imag_num):
        self.real_num = real_num
        self.imag_num = imag_num
        self.comp = self.real_num + self.imag_num
    
    def __add__(self, other):
        self.new_comp = self.comp + other.comp
        return self.new_comp
    
    def __mul__(self, other):
        self.new_comp = self.comp * other.comp
        return self.new_comp
    

c1 = Complex(4, 2j)
c2 = Complex(5, 3j)
print(c1 + c2)
print(c1 * c2)
