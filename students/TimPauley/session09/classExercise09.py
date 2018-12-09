#Tim Pauley
#Class 9, class exercises


class A:
	def method(self):
		print("A's called")


class B:
	def method(self):
		print("B's called")	


class C(B,A):
	def method(self):
		print("C's is called")
		super()__init__()			