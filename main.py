##Supermarket Catelogue Management System
from time import sleep
from pprint import pprint

'''DEFINITION OF VARIABLES
'''
choice, status, status1, status2, status3, status4, status5, status6, status7, status8, status9, Flag, state, ATM_valid, ATM_flag, flag2, flag1, flag3, flag4, flag5 = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False
user_input, user_input1, user_input2, first_name, last_name, location, phone_no, supermarket, mart, user_name, password, back, gmail, supplier_input, supplier_id, remove_input, prompt1, prompt2, prompt3, prompt4, prompt5, prompt6, prompt7, user_input1, user_input2, supplier_info_dict, supplier_container,individual_cont, admin_dict, parent_dict, product_dict, cart_dict, parent_cart, super_cart, product_container, customer_dict, supplier_cart,supplier_super_cart, supplier_child_cart, sub_cart= "", "", "", "", "","", "", "", "", "", "", "","", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {}, {},{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
exit_kinds = ("exit", "Exit")
fresh_food_dict, drinks_dict, cooking_oil_dict, household_dict, snacks_dict, essentials_dict, f_dict, d_dict, c_dict, h_dict, s_dict, e_dict= {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
ID_number = ("20202019ab", "20182017bc")
go_back = ("back" "b")
food_input = 0

numbers = ("0803", "0703", "0903", "0806", "0706", "0813", "0810", "0814", "0816",  "0805", "0705", "0905", "0807", "0815", "0811", "0905", "0809", "0909", "0817", "0818", "0802", "0902", "0701", "0808", "0708", "0812")

#This creates a defualt product and price and quanty list for this system	
product_container = {'Cooking Oil': {'Coconut Oil': {'Price per units': 250, 'Quantity in Stock': 10}},
 'Drinks': {'Pepsi': {'Price per units': 250, 'Quantity in Stock': 10}},
 'Everyday Essentials': {'Black Soap': {'Price per units': 250, 'Quantity in Stock': 10}},
 'Fresh Food': {'Orange': {'Price per units': 250, 'Quantity in Stock': 10}},
 'Household Product': {'Indomie': {'Price per units': 250, 'Quantity in Stock': 10}},
 'Snacks': {'Eggroll': {'Price per units': 250, 'Quantity in Stock': 10}}}

def admin():
	'''this saves the admins default user name, gmail and password in the App database(User_details)
	'''
	global admin_name, admin_password, admin_gmail, customer_dict
	
	admin_name = "Jeremiah"
	
	admin_gmail = "ajohjerry@gmail.com"
	
	admin_password = "Jerryibk999120"
	# populating user_details
	admin_dict["User name"] = admin_name
	admin_dict["gmail"] = admin_gmail
	admin_dict["Password"] = admin_password
	#ShopMax is the Supermarket Name code for admin
	#This stores admins details in suppliers container for access to all suppliers system
	supplier_container["Shopmax"] = admin_dict
	#this also stores admins details in customers dictionary for access to customers system
	customer_dict["Admin User name"] = admin_name
	customer_dict["Admin gmail"] = admin_gmail
	customer_dict["Admin Password"] = admin_password
	
admin()

print("Supermarket-Catelogue-Management-System".upper().center(60, "*"))
print("ShopMax".center(60, "*"))
	
print( )
	
print("Shop Cheaper Online on the Biggest Online Supermarkets in Nigeria.")
print()

def interface():
	'''this function displays the hompage for suppliers and customers
	'''
	global user_input1, status1, status3, Flag
	
	print("Choose from the Options Below",
	         "1) Supplier",
	         "2) Customer",
	         "3) Exit", sep = "\n")
	         
	print()
	
	while status1 == False:
		try:
			user_input1= int(input("Enter either 1 or 2 to choose from the Above Options: "))
			if user_input1 == 1 or user_input1 == 2 or user_input1 == 3:
				status1 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid in")
	
	if user_input1 == 1:
		status3 = False
		supplier_menu()
	if user_input1 == 2:
		Flag = False
		customers_menu()	
	if user_input1 == 3:
		print()
				
		print("Thanks for using ShopMax....",                     "Good Bye....", sep = "\n")
		exit()
			
def supplier_menu():
	'''This is the homepage where a Supplier chooses a preferred option. 
	'''
	global user_input2, status3, status1
	
	print("--" * 30)
	
	print("Choose from the Options below.",
	          "1) Create an Account",
	          "2) Log-in", sep = "\n")
	          
	print()
	print("To return to Previous Page Enter 0")
	#this Handles ValueError Exception for user_input2
	while status3 == False:
		try:
			user_input2 = int(input("Enter 1 or 2 to select from the Options above: "))
			if user_input2 == 0 or user_input2 == 1 or user_input2 == 2:
				status3 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid Input!")
	
	print()
	
	if user_input2 == 0:
		print("--" * 30)
		status1 = False
		interface()
	if user_input2 == 1:
		print("--" * 30)
		
		supplier_id_prompt()
		
		if supplier_id in ID_number:
			create_account()
			sign_in()
			second_prompt()
			
	if user_input2 == 2:
		sign_in()
		second_prompt()
	
def customers_menu():
	'''This homepage where the customers chooses a preferred Option
	'''
	global prompt6, Flag, status1
	
	print("--" * 30)
	
	print("Choose from the Options below",
	          "1) Registered Customer",
	          "2) New Customer", sep = "\n")
	
	print("To return to previous menu Enter 0.")
	print()
	#This handles Value Exception for prompt6
	while Flag == False:
		try:
			prompt6 = int(input("Enter either 1 or 2 to select from the Above: "))
			if prompt6 == 0 or prompt6 == 1 or prompt6 == 2:
				Flag = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
			
			print()
			
	if prompt6 ==0:
		print("--" * 30)
		status1 = False
		interface()		
	if prompt6 == 1:
		login( )
		
		print( )
	if prompt6 ==2:
		
		sign_up( )

		print( )
		
		login( )
		
		food_list()
		
		print()   			
	          					
def user_name_prompt():
	global user_name
	
	user_name = input("Username: ").title()
	
	while user_name.isalpha() == False or len(user_name) <=2:
		print()
			
		print("Invalid input!")
			
		print()
			
		user_name = input("Username: ").title()
			
def user_password():
	global password
	
	password = input("Password: ")
	
	while len(password) < 8 or password.isalpha() == True or password.isnumeric() == True or password.istitle() == False:
	    print()
	    	
	    print("Invalid input!", "Make sure it is at least 8 characters, including a number,a lowercase and at least an uppercase at the beginning.", sep = "\n")
	    	
	    print()
	    	
	    password = input("Password: ")

def user_gmail():
	global gmail
	
	gmail = input("Gmail Address: ").lower()
	
	while gmail.endswith("gmail.com") == False or len(gmail) <= len("gmail.com"):
		print()
			
		print("Invalid input!", "Enter a valid Gmail address", sep ="\n")
			
		print()
			
		gmail = input("Gmail Address: ").lower()
		
def supplier_id_prompt():
	'''This Creates a restriction to An unregistered Supplier. Every Supplier is expected to Visit ShopMax Complex and Make payment for an ID number to Create an Account in order to use this facilities
	'''
	global supplier_id, status1, status3
	
	print("Note: All Suppliers must have gotten thier Identification Number directly from ShopMax Complex before Create an Account")
	print()
	
	supplier_id = input("ID-Number: ")
	
	while supplier_id not in ID_number:
		print()
		
		print("Unable to Identify this Number", "Ensure you acquire your ID number from ShopMax Complex", sep = "\n")
		print()
			
		print("Redirecting back to menu..... ...... ...... ........")
				
		sleep(1)
		status1 = False
		status3 = False
		supplier_menu()

def user_input1_prompt():
	global user_input1, status5, max_qty
	
	max_qty = product_container[product_type][food_input]["Quantity in Stock"]
	
	while status5 == False:
		try:
			user_input1 = int(input("Enter the Quantity: "))
			print()
			
			if user_input1 <= max_qty and user_input1 != 0:
				
				status5 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")

def remove_input_prompt():
	'''This function allows Supplier to remove an Order Summary after authenticating Delivery 
	'''
	global remove_input
	
	print("Note: Before Removing any Buyer's Order, You must authenticate Delivery.", 
	        "Enter the name of the Buyer you want to Remove.", sep ="\n")
	print()
	
	remove_input = input("Name: ").title()
	
	while remove_input not in supplier_cart:
		
		print()
		
		print("Invalid input!")
		
		print()
		
		remove_input = input("Name: ").title()
	
	if remove_input in supplier_cart:
		print()
		
		print("Your transaction is in Processs....... ..... .....")
		
		sleep(2)
		
		supplier_cart.pop(remove_input)
		
		print()
		
		print("Successfully Removed...... ......")
	
def supplier_input_prompt():
	global supplier_input
	
	supplier_input = input("To return to menu enter y /To remove an Order after Delivery enter n: ")
	while supplier_input != "y" and supplier_input != "n":
		print()
		
		print("Invalid input!")
		
		print()
		
		supplier_input = input("To return to menu enter y / To remove an Order after Delivery emter n: ")

def payment_prompt():
	global prompt7, flag5, state, ATM_valid, ATM_flag, flag2, status1, status4, status5, status6, status7
	
	while flag5 == False:
		try:
			prompt7 = int(input("Enter 1 to proceed to make Payment or 0 to go back>>> "))
			if prompt7 == 1:
				flag5 = True
				ATM_validity_checker()
			elif prompt7 == 0:
				flag5 = True
				status1, status4, status5, status6, status7 = False, False, False, False, False
				parent_cart = {}
				food_list()
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")	
				
def product_type_prompt():
	global product_type, flag3
	
	while flag3 == False:
		try:
			product_type = input("Product Type: ").title()
			
			if product_type in ("Fresh Food", "Drinks", "Snacks", "Cooking Oil", "Household Product", "Everyday Essentials"):
				flag3 = True
				
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!", "Hints: Enter the Product-Type written Above.", sep = "\n")

def supplier_cart_prompt():
	global supplier_cart, supplier_super_cart, supplier_child_cart
	
	supplier_child_cart = {}
	supplier_super_cart = {}
		
	supplier_child_cart["Buyer's' Address"] = location
	supplier_child_cart["Phone number"] = phone_no
	supplier_child_cart["Gmail Address"] = gmail
	supplier_child_cart["Total Amount Paid (Delivery fee inclusive)"] = total_cost
	
	supplier_super_cart.update(supplier_child_cart)
	supplier_super_cart.update(parent_cart)
	#This populates supplier's cart'
	supplier_cart[name] = supplier_super_cart		
							
def cart():
	global prompt4, status6, status7, price_units, status5, add_to_cart, status1, status4, product_type, product_price, new_qty, parent_cart
	
	print()
	while status6 == False:
		try:
			prompt4 = int(input("Enter 1 to proceed and Add to Cart: "))
			
			if prompt4 == 1 or prompt4 == 0:
				status6 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
			
	if prompt4 == 0:
		status1 = False
		status4 = False
		status5 = False
		status6 = False
		status7 = False
		food_list()
	
	if prompt4 ==1:
		print("--" * 30)
		
		print()
		
		max_qty = product_container[product_type][food_input]["Quantity in Stock"]
		
		if max_qty == 0:
			print(f"{product_type} Category is empty.")
			print()
			
			print("Redirecting back to menu..... ...... ...... ........")
				
			sleep(1)
				
			print()
			status1 = False
			status4 = False
			status5 = False
			status6 = False
			status7 = False
			food_list()
			
		else:
			status5 = False
			
			print(f"Product: {food_input}")
			
			price_units= product_container[product_type][food_input]["Price per units"]
			
			print("Price per units:", price_units)
			
			user_input1_prompt()
			
			cart_dict = {}
			
			product_price = price_units * user_input1
			
			cart_dict["Price"] = product_price
			cart_dict["Quantity"] = user_input1
			
			add_to_cart = input("Enter either y as yes or n as no to Add to Cart: ").lower()
			
			while add_to_cart not in ("yes", "y", "no", "n"):
				print()
				
				print("Invalid input")
				
				print()
				
				add_to_cart = input("Enter either y as yes or n as no to Add to Cart: ").lower()
			if add_to_cart in ("yes", "y"):
				if len(parent_cart) ==  5:
					print("Cart passed Limit..........", "Note: Cart can only Contain Maximum of Five (5) Products at once.")
					print()
					
					print("Redirecting back to menu..... ...... ...... ........")
					
					sleep(1)
					print()
					status1 = False
					status4 = False
					status5 = False
					status6 = False
					status7 = False
					food_list()
				elif len(parent_cart) <= 5:
					parent_cart[food_input] = cart_dict
					new_qty = max_qty - user_input1
					product_container[product_type][food_input]["Quantity in Stock"] = new_qty
					
					print()
					
					print(f"You added {food_input} to Shopping Cart")
					
					print()
					
					print("Redirecting back to menu..... ...... ...... ........")
					
					sleep(1)
					
					print()
					
					status1 = False
					status4 = False
					status5 = False
					food_list()
			elif add_to_cart in ("no", "n"):
				status1 = False
				status4 = False
				status5 = False
				status6 = False
				status7 = False
				food_list()	
	
def Main_cart_info():
	'''This allows Each Customers to enter all the Products to be Ordered and allows them to Provide other informations relevant for Product Delivery
	'''
	global main_cart, price, quantity, sub1_input, sub2_input, sub3_input, sub4_input, total_price, total_cost, status1, status4, delivery_fee, parent_cart, supplier_cart, supplier_super_cart, supplier_child_cart
	
	print("--" * 30)
	
	print("Shopping Cart".upper().center(60, " "))
	
	print()
	
	if len(parent_cart) != 0:
		pprint(parent_cart, width = 100)
		
		print()
		
		print("Delivery Address".upper())
		
		first_name_prompt()
		
		last_name_prompt()
		
		user_location()		
		
		user_phone_no()
		
		user_gmail()
		
		delivery_fee = 250
		
		print("Delivery fee: ", delivery_fee)
		
		name = first_name + " " + last_name
		
		price = []
		quantity = []
		
		for i in parent_cart.values():
			for j in i:
				price.append(i.get("Price"))
				break
				
		for e in parent_cart.values():
			for f in e:
				quantity.append(e.get("Quantity"))
				break
				
		total_price = sum(price)
		
		print("Product Price: ", total_price)
		
		total_cost = total_price + delivery_fee
		
		print("Total Cost: ", total_cost)
		
		
		
		print()
		
		payment_prompt()
		
		print("Redirecting back to menu..... ...... ...... ........")
		sleep(1)
		print()
		status1 = False
		status4 = False
		status5 = False
		status6 = False
		status7 = False
		parent_cart = {}
		food_list()
		
	else:
		print()
		
		print("Cart is Empty.", "Redirecting back to menu...... ....... ...... ..........", sep = "\n")
		
		sleep(1)
		print()
		status1 = False
		status4 = False
		food_list()
		

def food_input_prompt():
	global food_input, status7, max_qtyJ
	
	while status7 == False:
		try:
			food_input = input("Product: ").title()
			if food_input in food_list_prompt:
				status7 = True
			else:
				raise KeyError
		except:
			print()
			
			print("Food name does not Exist.....")
	
def first_name_prompt():
	global first_name
	
	first_name = input("First name: ").title()
	while first_name.isalpha() == False or len(first_name) <=2:
		print()
			
		print("Invalid input!")
			
		print()
			
		first_name = input("First name: ").title()
		
def last_name_prompt():
	global last_name
	
	last_name = input("Last name: ").title()
	
	while last_name.isalpha() == False or len(last_name) <=2:
		print()
			
		print("Invalid input!")
			
		print()
		
		last_name = input("Last name: ").title()
		
def user_location():
	global location
	
	location = input("Address: ").title()
	while location.isdigit() is True or len(location) < 2:
		print()
			
		print("Invalid input!")
			
		print()
			
		location = input("Address: ").title()
	
def user_phone_no():
	global phone_no
	
	phone_no = input("Phone number: ")
	
	while phone_no.isnumeric() == False or len(phone_no) != 11 or phone_no.startswith(numbers)== False:
		print()
			
		print("Invalid Phone number!")
			
		print()
			
		phone_no = input("Phone number: ")
		
def supermarket_name():
	global supermarket
	
	supermarket = input("Supermarket Name: ").title()
	if supermarket not in exit_kinds:
		while supermarket.isnumeric() == True or len(supermarket) < 4 :
			print()
			
			print("Invalid input!")
			
			print()
			
			supermarket = input("Supermarket Name: ").title()

def super_mart():
	global mart
	
	mart = input("Supermarket Name: ").title()
	
def previous_page():
	global back
	
	back = input("Enter 'back' or 'b' to go to the previous Option: ")
	
	while back != "back" and back != "b":
		print()
		
		print("Invalid input!")
		
		print()
		
		back = input("Enter 'back' or 'b' to go to the previous Option: ")
	

def product_name_prompt():
	global product_name
	
	product_name = input("Product Name: ").title()
	
	while product_name.isnumeric() == True and product_name.isalpha() == False or len(product_name) < 3:
		print()
		
		print("Invalid Product Name!")
		
		print()
		
		product_name = input("Product Name: ").title()
		
def product_price():
	global price, status9
	
	while status9 == False:
		try:
			price = int(input("Price per units: "))
			#this creates a limit to the maximum price for each products
			if price in range(1, 10000):
				status9 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
	
def product_qty():
	global quantity, status8
	
	while status8 == False:
		try:
			quantity = int(input("Quantity in Stock: "))
			#this creates a limit of 1000 to the quantity of each Products in store 
			if quantity in range(1, 1000):
				status8 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
		
def create_account():
	''' This function display the Create Account section for Adding suppliers details
	'''
	global first_name, last_name, gmail, user_name, location, phone_no, password, supermarket
	
	print("--" * 30)
	
	print("\tAll Suppliers are required to provide all Relevant details such as their Full name, Location, SuperMarket name and address, Gmail Address, etc.This is essential for Verification, smooth Access, Customer Complaint and regular Update.Thanks for your cooperation.")
	print()
	
	print("Create an Account>>>>")
	
	print()
	
	first_name_prompt()
			
	last_name_prompt()
			
	supermarket_name()
			
	user_location()
	
	user_name_prompt()
			
	user_phone_no()
			
	user_password()
	
	user_gmail()
		
	print()
	
	name = first_name + " " + last_name
	
	supplier_info_dict = {}# this emulates the clearing of the contents of the dictionary storing the previously saved Supplier since this dictionary is now in a super dictionary called suplier_container & also because the empty supplier_info_dict would be used for subsequent registration of new Suppliers
	supplier_info_dict["First name"] = first_name
	supplier_info_dict["Last name"] = last_name
	supplier_info_dict["Supermarket Name"] = supermarket
	supplier_info_dict["Supermarket Address"] = location
	supplier_info_dict["Phone Number"] = phone_no
	supplier_info_dict["User name"] = user_name
	supplier_info_dict["gmail"] = gmail
	supplier_info_dict["Password"] = password
	#individual_cont allows each suppliers details to be displayed
	individual_cont[supermarket] = supplier_info_dict
	#this stores all suppliers details in supplier_container
	supplier_container[supermarket] = supplier_info_dict
	
	print(individual_cont)
	
	print()
			
	print("Saved Successfully", "-" * 30)
	
	print()
	
	
	print("Redirecting to Signin page in 3secs>>>")
		
	print()
		
	sleep(3)
		
	print("--" * 30)

def sign_up():
	''' This allows Customer to Create Account
	'''
	global user_name, password, confirm_password, gmail, customer_dict, child_dict
	
	print("--" * 30)
	
	print("Create and Account>>>")
	
	print()
	
	user_name_prompt()
	
	user_password()
	
	confirm_password = input("Confirm password: ")
	#this checks if the passwords tally
	while confirm_password != password:
		print( )
			
		print("Invalid input!", "Password does not match.")
			
		print( )
			
		confirm_password = input("Confirm password: ")
		
	user_gmail()
	
	while gmail.endswith("gmail.com") == False or len(gmail) <= len("gmail.com"):
		print()
			
		print("Invalid input!", "Enter a valid Gmail address", sep ="\n")
			
		print()
			
		user_gmail()
		customer_dict = {}
		child_dict = {}
	#this stores customers user details in customer_dict
	customer_dict["User name"] = user_name
	customer_dict["Gmail Address"] = gmail
	customer_dict["Password"] = password
	
	print()
	
	print("Saved Successfully", "-" * 30)
	
	print()
	
	print("Redirecting to Signin page in 3secs>>>")
	
	sleep(3)
	
def sign_in():
	''' This is the sign in function for suppliers
	'''
	global user_name, password, gmail, name, admin_name, signin_password, mart
	
	print("--" * 30)
	print("Signin to Your ACCOUNT")
	
	print()
	
	super_mart()
	
	while mart not in supplier_container:
		print()
			
		print("Invalid input!", "Enter a registered Supermarket.", sep ="\n")
			
		print()
			
		super_mart()
		
	user_name_prompt()
	#This extract the User name from the dictionary
	name= (supplier_container[mart] ["User name"])
	
	while user_name != name:
		print()
			
		print("User name does not Exist", "Please Enter a Valid User name", sep = "\n")
		user_name_prompt()
	
	user_password()
	
	signin_password = (supplier_container[mart] ["Password"])
	#this checks if password exist in user details
	while password != signin_password:
		print()
			
		print("Invalid input!", "Make sure it is at least 8 characters, including a number,a lowercase and at least an uppercase at the beginning.", sep = "\n")
			
		print( )
			
		user_password()
			
def login():
	''' This is the Login section for the customers
	'''
	global password, name, user_pass1, user_pass2, status4, status1, Flag
	
	print("--" * 30)
	
	print("Sign-in to your ACCOUNT.")
	
	print()
	
	name = input("User name: ").title()
	password = input("Password: ").title()
	#This checks if User name and password exist in the customer_dict
	if (name == customer_dict.get("Admin User name") or name == customer_dict.get("User name")) and (password == customer_dict.get("Password") or password == customer_dict.get("Admin Password")):
		status4, status1= False, False
		food_list()
		
	else:
		Flag = False
		
		print()
		
		print("Incorrect data!!!", "Redirecting to menu.....  .....  ......  ...... ", sep = "\n")
		
		sleep(1)
		
		print()
			
		customers_menu()
	
def add_product_prompt():
	global add_product
	
	add_product = input("Do you Want to add another product? Yes or y/No or n: ").lower()
	while add_product not in ("yes", "y") and  add_product not in ("no", "n"):
		print()
		
		print("Invalid input!")
		
		add_product = input("Do you Want to add another product? Yes or y/No or n: ").lower()
	
def fresh_food_prompt():
	global product_name, choice, status8,status9
	
	print("--" * 30)
	
	print("Add Fresh Food to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	
	product_dict = {}

	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in f_dict.items():
		f_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	fresh_food_dict["Fresh Food"] = f_dict
	
	product_container.update(fresh_food_dict)
	
	print()
	
	add_product_prompt()
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()

	if add_product == "y" or add_product == "yes":
		print()
		status8 = False
		status9 = False
		
		fresh_food_prompt()
	
	print()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
			
		choice = False
		status8 = False
		status9 = False
		
		product_categories()
			
def drinks_prompt():
	global product_name, choice, status8, status9
	
	print("--" * 30)
	
	print("Add Drinks to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	
	product_dict = {}
	
	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in d_dict.items():
		d_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	drinks_dict["Drinks"] = d_dict
	
	product_container.update(drinks_dict)
	
	print()
	
	add_product_prompt()
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()
		
	if add_product == "y" or add_product == "yes":
		print()
		
		status8 = False
		status9 = False
		
		drinks_prompt()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
		status8 = False
		status9 = False
		choice = False
		product_categories()
		
def product_essentials():
	global product_name, choice, status8, status9
	
	print("--" * 30)
	
	print("Add Everyday Essentials to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	
	product_dict = {}
	
	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in e_dict.items():
		e_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	essentials_dict["Everyday Essentials"] = e_dict
	
	product_container.update(essentials_dict)
	
	print()
	
	add_product_prompt()
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()
		
	if add_product == "y" or add_product == "yes":
		print()
		status8 = False
		status9 = False
		
		product_essentials()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
		status8 = False
		status9 = False
		choice = False
		product_categories()
		
def snacks_prompt():
	global product_name, choice, status8, status9
	
	print("Add Snacks to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	
	product_dict = {}
	
	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in s_dict.items():
		s_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	snacks_dict["Snacks"] = s_dict
	
	product_container.update(snacks_dict)
	
	print()
	
	add_product_prompt()
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()
	
	if add_product == "y" or add_product == "yes":
		print()
		status8 = False
		status9 = False
		
		sneaks_prompt()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
		status8 = False
		status9 = False
		choice = False
		product_categories()
		
def oil_prompt():
	global product_name, choice, status8, status9
	
	print("--" * 30)
	
	print("Add Cooking Oil to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	
	product_dict = {}
	
	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in c_dict.items():
		c_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	cooking_oil_dict["Cooking Oil"] = c_dict
	
	product_container.update(cooking_oil_dict)
	
	print()
	
	add_product_prompt()
	
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()
		
	if add_product == "y" or add_product == "yes":
		print()
		status8 = False
		status9 = False
		oil_prompt()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
		status8 = False
		status9 = False
		choice = False
		product_categories()
		
def household_product():
	global product_name, choice, status8, status9
	
	print("--" * 30)
	
	print("Add Household Products to Product list.")
	
	print()
	
	product_name_prompt()
	
	product_price()
		
	product_qty()
	product_dict = {}
	
	product_dict["Price per units"] = price
	product_dict["Quantity in Stock"] = quantity
	
	if product_dict not in h_dict.items():
		h_dict[product_name] = product_dict	
	#this dictionary stores products under fresh food list
	household_dict["Household Product"] = h_dict
	
	product_container.update(household_dict)
	
	print()
	
	add_product_prompt()
	
	if add_product == "n" or add_product == "no":
		print()
		
		pprint(product_container, width = 100)
		print()
		
	if add_product == "y" or add_product == "yes":
		print()
		status8 = False
		status9 = False
		
		household_product()
	
	previous_page()
	
	if back == "back" or back == "b":
		print()
		status8 = False
		status9 = False
		choice = False
		product_categories()
			
def product_categories():
	'''This is the Homepage for Available Product type
	'''
	global product_type, price, quantity, product_input, choice, status2
	
	print("--" * 30)
	
	print("Select from the Categories below and Add your Products to the selected Category\n".upper(), 
	"1) Fresh Food", 
	"2) Drinks", 
	"3) Everyday Essential",
	"4) Snacks", 
	"5) Cooking Oil", 
	"6) Household", sep = "\n")
	
	print()
	
	print("To return to Previous Page Enter 0")
	
	product_dict = {}
	
	print()
	#This handles ValueError exception for product_input
	while choice == False:
		try:
			product_input = int(input("Enter 1-6 to Select from the Above Options: "))
			
			if product_input == 0 or product_input == 1 or product_input == 2 or product_input == 3 or product_input == 4 or product_input == 5 or product_input == 6:
				choice = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
			
	if product_input == 1:
		
		fresh_food_prompt()
	if product_input == 2:
		
		drinks_prompt()
	if product_input == 3:
		
		product_essentials()
	if product_input == 4:
		
		snacks_prompt()
	if product_input == 5:
		
		oil_prompt()
	if product_input == 6:
		
		household_product()
		
	if product_input == 0:
		status2 = False
		choice = False
		second_prompt()
		
def second_prompt():
	global prompt2, status2, status3, supplier_input, remove_input
	
	print("--" * 30)
	print("Choose from the Options below",         "1) Add Inventories to Store", 
	  "2) Customers Cart ", sep = "\n")
	
	print()
	
	print("To return to Previous Page Enter 0")
	
	print()
	
	while status2 == False:
		try:
			prompt2 = int(input("Press 1 or 2 to select from the Options Above: "))
			if prompt2 == 0 or prompt2 == 1 or prompt2 == 2:
				status2 = True
				
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
			
	if prompt2 == 0:
		print("--" * 30)
		status3 = False
		supplier_menu()
	if prompt2 == 1:
		product_categories()
	if prompt2 == 2:
		print("--" * 30)
		sleep(1)
		
		if len(supplier_cart) == 0:
			print("Cart is Empty.", "Redirecting back to menu...... ....... ...... ..........", sep = "\n")
			sleep(1)
			status2, status3 = False, False
			second_prompt()	
			
		elif len(supplier_cart) > 0:
			print("Order Summary.".upper())
			
			print()
			
			pprint(supplier_cart)
			
			print()
			
			supplier_input_prompt()
			
			if supplier_input == "y":
				status2, status3 = False, False
				second_prompt()
			if supplier_input == "n":
				print("--" * 30)
				
				remove_input_prompt()
				pass
						
def food_list():
	'''This function allows Customers to access Available Product types
	'''
	global prompt3, status4, status1, flag3, status7, status8, status5, status6
	print("--" * 30)
	
	print("Available Product Categories\n".upper(), 
	"Note: Shopping Cart can only contain Maximum of Five (5) Products per Transaction\n",
	"1) Fresh Food", 
	"2) Drinks", 
	"3) Everyday Essential",
	"4) Snacks", 
	"5) Cooking Oil", 
	"6) Household",
	"7) Cart", sep = "\n")
	print()
	
	print("To return to Previous Page Enter 0")
	print()
	#This Handles ValueError in prompt3
	while status4 == False:
		try:
			prompt3 = int(input("Enter 1 - 7 to select from the Above Options: "))
			if prompt3 in (0, 1, 2, 3, 4, 5, 6, 7):
				status4 = True
			else:
				raise ValueError
		except:
			print()
			
			print("Invalid input!")
	
	if prompt3 == 0:
		print("--" * 30)
		status1 = False
		interface()
	if prompt3 == 1:
		print("Product-Type: Fresh Food")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 2:
		print("Product-Type: Drinks")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 3:
		print("Product-Type: Everyday Essentials")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 4:
		print("Product-Type: Snacks")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 5:
		print("Product-Type: Cooking Oil")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 6:
		print("Product-Type: Household Product")
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		freshFood()
	if prompt3 == 7:
		flag3 = False
		status5 = False
		status6 = False
		status7 = False
		status8 = False
		Main_cart_info()

def freshFood():
	global food_input, food_list_prompt, user_input1, user_input2, product_details, max_qty, prompt4, status5, status6, status7, product_type
	
	print("--" * 30)
	
	print()
	
	print("Kindly Enter the Product Type written Above.")
	
	product_type_prompt()
	
	food_list_prompt = list( i for i in product_container[product_type])
	print()
	
	print(food_list_prompt)
	
	print()
	
	print("Enter the name of the Product")
	print()
	
	food_input_prompt()
	print()
	
	product_details = product_container[product_type][food_input]
	
	print(product_details)
	
	cart()

def child_ATM_validity_checker():
	''' This allows multiple trials of PAN input if invalid at previous check. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global ATM_flag, state, flag2, status1, status4, status5, status6, status7
	
	print("Would you like to try again?")
	
	while ATM_flag is False:
		try:
			print()
			intake = input("Enter y for 'yes' or n for 'no' : ").lower()
			print()
			if intake in ("yes", "y"):
				ATM_flag = True
				state = False
				ATM_validity_checker()
			elif intake in ("no", "n"): 
				print("--" * 30)
				
				status1, status4, status5, status6, status7 = False, False, False, False, False
				parent_cart = {}
				food_list()
			else:
				raise ValueError 
		except ValueError:
			print()
			print("Invalid input!", "Enter y for 'yes' or n for 'no'.")
	
def ATM_validity_checker():
	''' This uses Lunh's algorithm to validate an ATM card required for tuition payment by performing some calculations on the 15/16 long PAN digits on the front of the card.
			
	Args:
		N/A
	
	Returns:
		ATM_valid boolean state
		
	Raises:
		ValueError: if  user_input is incorrect 
	
	The variables lunh_step1a, lunh_step1b, lunh_step1c, lunh_step1_result, lunh_step2, lunh_ans are the results of the 3 action steps in Lunh's algorithm:
		
		step 1- starting from the penultimate digit (down to the first digit) multiply every second-placed digit by 2, then add all the individual digit found in the result obtained earlier together. 
		step 2- add the total sum obtained above to the sum of all PAN digits not multiplied by 2 in the above step.
		step 3- The ATM card is valid if the remainder of the division of the result obtained above by 10 is 0.
	''' 
	
	global card_digits, state, ATM_valid, ATM_flag, flag2
	print("--" * 30)
	
	while state is False:
		try:
			card_digits = input("Enter all the 15 or 16-digits long PAN located on the front of your ATM card: ")
			
			# deployment of Lunh's algorithm 
			if card_digits.isdigit() is True and len(card_digits) >= 15:
				state = True
				card_digits = [int(item) for item in card_digits]
				lunh_step1a = list(map(lambda digit: (digit * 2) , card_digits[-2::-2]))
				lunh_step1b = [str(digit) for digit in lunh_step1a]
				lunh_step1c = [list(digit) for digit in lunh_step1b]
				lunh_step1_result = sum([int(digit) for digit_string in lunh_step1c for digit in digit_string]) 
				card_digits2 = [card_digits.remove(digit) for digit in card_digits[-2::-2]]
				lunh_step2 = sum(card_digits)
				
				lunh_ans = lunh_step1_result + lunh_step2
				
				print() 
				
				print()
				
				print("Checking the validity of your ATM card... .....  .....  ....  .....")
					
				print()
			
				print("Please wait a bit.")
					
				print()
					
				sleep(3)
				
				if lunh_ans % 10 == 0:
					print("ATM card is Valid!")
					supplier_cart_prompt()
					ATM_valid = True 
				else:
					ATM_flag = False
					print("Invalid ATM card!!!")
					print()
					child_ATM_validity_checker()
			else:
				ATM_flag = False
				state = True
				print()
				print("Invalid PAN.", "Kindly re-enter your ATM's PAN.", sep = "\n")
				print()
				child_ATM_validity_checker() 
		except ValueError:
			print()
			
			print("Invalid PAN.", "Kindly re-enter your ATM's PAN.", sep = "\n")
			
			print()
	return ATM_valid 	
		
'''MAIN PROGRAM INVOCATION
'''	
interface()