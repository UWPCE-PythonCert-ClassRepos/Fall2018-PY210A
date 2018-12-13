#Tim Pauley
#Class 9, class exercises


class A:
	def __init__(self):
		print("A's called")
		#super().__init__()

class D:
	def __init__(self):
		print("D's is called")
		super().__init__()


class B:
	def __init__(self):
		print("B's called")	
		super().__init__()

class C(B,A):
	def __init__(self):
		print("C's is called")
		super().__init__()			