class calculator:
	
	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb

	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a * self.b


class scientific(calculator):
	def power(self):
		return pow(self.a, self.b)

newcalculation = calculator(10,20)

print 'a+b: %d'%newcalculation.add()

print 'a*b: %d'%newcalculation.mul()

newpower = scientific(4,3)

print 'a+b: %d'%newpower.add()

print 'a*b: %d'%newpower.mul()

print 'a Power b: %d'%newpower.power()