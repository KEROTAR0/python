class PhanSo:
    def __init__(self, tu_so, mau_so) -> None:
        self.tu = tu_so
        self.mau = mau_so
    
    def rutGon(self):
        pass
    
    def __add__(self, other):
        pass
    
    def __sun__(self, other):
        pass
    
    def __mul__(self, other):
        pass
    
    def __truediv__(self, other):
        pass
    
a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3,5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
