import string
import random
import re

class Password:

	def __init__(self):
		self.password_arr = []
		self.text = ""
		self.force = 0
		self.length = 0
		self.special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

	def test_password(self, password):
		self.password_arr = list(password)
		for i in range(len(self.password_arr)):
			if(self.password_arr[i].isdigit()):
				self.force = self.force + 2

			elif(self.special_char.search(self.password_arr[i]) != None):
				self.force = self.force + 6

			else:
				self.force = self.force + 4

	def get_force(self):
		if(self.force <= 40):
			self.force_name = "Très faible"

		if(self.force > 40 and self.force <= 60):
			self.force_name = "Faible"

		if(self.force > 60 and self.force <= 80):
			self.force_name = "Moyen"

		if(self.force > 80):
			self.force_name = "Fort"

		return str(self.force_name) + ": " + str(self.force) + " points"

	def generate_password(self, optionel_length):
		str_l = string.ascii_lowercase
		str_u = string.ascii_uppercase
		str_d = string.digits
		str_p = string.punctuation

		if(optionel_length != 0):
			self.length = optionel_length
		else:
			self.length = 30

		for i in range(self.length):
			n = random.randint(1, 4)
			if(n == 1):
				self.text = self.text + random.choice(str_l)
			if(n == 2):
				self.text = self.text + random.choice(str_u)
			if(n == 3):
				self.text = self.text + random.choice(str_d)
			if(n == 4):
				self.text = self.text + random.choice(str_p)

	def get_password(self):
		return self.text

while(True):
	password_class = Password()

	print("\n 1: Test Password")
	print(" 2: Generate Password")
	print(" 3: Quit \n")

	r = int(input(" Choice: "))

	print(" -------------------------")

	if(r == 1):
		password = input(" Your Password: ")
		password_class.test_password(password)

		print("\n Force:", password_class.get_force())

	elif(r == 2):
		password_length = int(input(" Password Length: "))
		password_class.generate_password(password_length)
		password_class.test_password(password_class.get_password())

		print("\n Password:", password_class.get_password())
		print("\n Force:", password_class.get_force())

	elif(r == 3):
		exit()