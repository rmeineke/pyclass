#!/usr/bin/env python
class Animal:
	says = 'Grrrr'

	def __init__(self):
		self.mobile = True

	def __str__(self):
		return self.says

	def __call__(self):
		print "run"
		
class Human(Animal):
	says = 'Hi'

class Plant:
	says = 'Sunshine'

	def __init__(self):
		self.mobile = False

	def __call__(self):
		print "flowering"
		
class Flower(Plant):
    says = 'Bloom'
    def __init__(self): 
        Human.__init__(self)

class FlowerChild(Flower, Human):
    says = 'Peace'


print FlowerChild()
print FlowerChild().mobile
