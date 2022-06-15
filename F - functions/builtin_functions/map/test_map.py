class A:
	pass
	# def __str__(self):
	# 	return "I am object of class A"

	def __repr__(self):
		return "I am object of class A"

p = A()

print(p)