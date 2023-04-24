class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def get_nombre1(self):
        return self.nombre1

    def get_nombre2(self):
        return self.nombre2
    
op = Operation()
print(op.get_nombre1())  
print(op.get_nombre2())  

