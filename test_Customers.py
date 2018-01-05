import unittest
from Customers import CustomerLocations

# Set up an object instantiation with some customer records 
class CustomerLocationsTestCase(unittest.TestCase):
	def setUp(self):
		customers = [	{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}, 
						{"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
						{"latitude": "-53.339450", "user_id": 99, "name": "Joe Shmoo", "longitude": "173.742287"}]	# anti-pode
						
		self.test_CL = CustomerLocations([53.339428,-6.257664], customers)
# -53.339450, 173.742287
# Test the behaviour of class CustomerLocations 
class test_CustomerLocations(CustomerLocationsTestCase):
	# Check that degrees are being correctly converted to radians 
	def test_converted_to_radians(self):
		self.assertAlmostEqual(self.test_CL.customers[0]['latitude'], 0.906330805537)
		self.assertAlmostEqual(self.test_CL.customers[0]['longitude'], -0.179367312694)
		self.assertAlmostEqual(self.test_CL.customers[1]['latitude'], 0.924786702446)
		self.assertAlmostEqual(self.test_CL.customers[1]['longitude'], -0.105482481456)
	# Check that customer records are sorted in order of ascending user_id
	def test_sorted_correctly(self):
		self.assertEqual(self.test_CL.customers[0]['name'], 'Alice Cahill')
		self.assertEqual(self.test_CL.customers[1]['name'], 'Christina McArdle')
	# Check that the computer customer distances from the office are as expected 
	def test_customer_distance(self):
		self.assertAlmostEqual(self.test_CL.customer_distance(self.test_CL.customers[0]), 313.255633781)
		self.assertAlmostEqual(self.test_CL.customer_distance(self.test_CL.customers[1]), 41.768725500)
		self.assertAlmostEqual(self.test_CL.customer_distance(self.test_CL.customers[2]), 20015.0827248567)
	# Check customers within range are being found
	# Distance <= 0 should raise exception 
	def test_within_distance(self):
		self.assertRaises(ValueError, self.test_CL.within_distance, self.test_CL.customers[0], 0)	
		self.assertEqual(self.test_CL.within_distance(self.test_CL.customers[0], 100), False)
		self.assertEqual(self.test_CL.within_distance(self.test_CL.customers[1], 100), True)
	# Check that we are finding the correct customers for a range value 
	def test_customers_in_range(self):
		custs = self.test_CL.customers_in_range(100)
		self.assertEqual(len(custs), 1)
		self.assertEqual(custs[0]['user_id'], 12)

def main():
	unittest.main()

if __name__ == "__main__":
	main()
