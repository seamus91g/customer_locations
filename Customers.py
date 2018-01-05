import math 
# Data structure which stores customer details for a business in a specific location (HQ_lat & HQ_lon)
# Customer distances from the office location can be queried
# Can check if customers are within a specific range or find a list of customers within a range 
class CustomerLocations: 
	def __init__(self, HQ, customers):
		# Latitude/Longitude of office location. Customers will be found relative to this location
		# Convert degrees to radians for office/customers and sort customer by ascending user_id. 
		self.HQ_lat = math.radians(HQ[0])
		self.HQ_lon = math.radians(HQ[1])
		self.__deg_to_rad(customers)		
		customers = self.__sort(customers)
		self.customers = customers
		self.earth_radius = 6371		# Earth radius, km
	# Returns a list of all customers within a specified range 
	def customers_in_range(self, valid_range):
		customers_to_contact = []
		for customer in self.customers:
			if(self.within_distance(customer, valid_range)):
				customers_to_contact.append(customer)
		return customers_to_contact
	# Check if customer is within a specific range.  
	def within_distance(self, customer, distance):
		if (distance <= 0):
			raise ValueError("Distance to check must be greater than zero!")
		dist = self.customer_distance(customer)
		if (dist < distance):
			return True
		else:
			return False
	# Find the distance from the office to the customer 
	def customer_distance(self, customer):
		center_ang = self.__find_center_angle(customer)
		dist = self.earth_radius*center_ang
		return dist
	# Sort in order of ascending user_id
	def __sort(self, unsorted_customers):
		sorted_customers = sorted(unsorted_customers, key=lambda k: k['user_id'])
		return sorted_customers
	# Convert degrees to radians for each customer 
	def __deg_to_rad(self, customers):
		for customer in customers:
			lat = float(customer['latitude'])
			lon = float(customer['longitude'])
			customer['latitude'] = math.radians(lat)
			customer['longitude'] = math.radians(lon)
	# Find center angle between office and customer 
	def __find_center_angle(self, customer):
		customer_lat = float(customer['latitude'])
		customer_lon = float(customer['longitude'])
		theta_lat = self.HQ_lat - customer_lat
		theta_lon = self.HQ_lon - customer_lon
		cent_angle = math.acos(
								math.sin(self.HQ_lat)*math.sin(customer_lat) 
								+ math.cos(self.HQ_lat)*math.cos(customer_lat)*math.cos(theta_lon)
								)
		return cent_angle
