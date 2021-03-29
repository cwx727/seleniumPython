import unittest
import ddt

@ddt.ddt
class DemoDdt(unittest.TestCase):
	def setUp(self):
		print("setup")
	def tearDown(self):
		print("tearDown")

	@ddt.data([1,2],[3,4])
	@ddt.unpack
	def test_add(self,a,b):
		print(a+b)

if __name__ == '__main__':
	unittest.main()

