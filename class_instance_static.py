
# instance method\concreate method

class Math:
    def add(self,a:int,b:int):
        print(a + b)
c = Math()
c.add(20,50)


# static method

class math:
    def add(a:int,b:int):
        print(a * b)
math.add(5,6)

# stati variable

class math():
    a:int = 10
    def getval(self):
        return self.a
m = math()
m.a = 66
print(m.getval())

math.a=68
print(m.getval())

m = math()
print(m.getval())
