from Customers import CustomerLocations
import json

# print name with user_id
def print_customers(customers):
	print("id", "\t", "name", "\n", "--------------------")
	for customer in customers:
		print(customer['user_id'], "\t", customer['name'])

# Load customer data from json file 
# Find list of customers withing 100km
def main():
	with open('customers.json', 'r') as file: 
		customers = json.load(file)
	office_location = [53.339428,-6.257664]
	CL = CustomerLocations(office_location, customers)
	customers_to_contact = CL.customers_in_range(100)
	print_customers(customers_to_contact)

if __name__ == "__main__":
	main()
