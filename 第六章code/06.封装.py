class Rectangle:
	'''
	表示矩形的类
	'''
	def __init__(self,width,height):
		self.hidden_width=width
		self.hidden_height=height

	def get_width(self):
		return self.hidden_width

	def get_height(self):
		return self.hidden_height

	def set_width(self,width):
		self.hidden_width=width

	def set_height(self.height):
		self.hidden_height=height

	def get_area(self):
		return set_height*set_width