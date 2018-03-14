class Circle1:
	def _init_(self, radius):
		self._radius = radius
	def setRadius(self, newValue)
		if newValue >=0:
			self._radius = newValue
		else: raise ValueError("Value must be positive")
	def area(self):
		return 3.14159 * (self._radius ** 2)

class Circle2:
	def _init_(self, radius):
		self._radius = radius

	def _setRadius(self, newValue):
		if newValue >=0:
			self._radius = newValue
		else: raise ValueError("Value must be positive")
	radius = property(None, _setRadius)