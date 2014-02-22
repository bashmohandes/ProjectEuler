__author__ = "mohamed.elsherif"
from time import time

class AutoMeasure:
	def __init__(self, f):
		self.f = f		

	def __call__(self, *args, **kwargs):
		t1 = time()
		res = self.f(*args, **kwargs)
		t2 = time()
		print "Function %s took %.2f seconds" % (self.f.__name__, (t2 - t1))
		return res