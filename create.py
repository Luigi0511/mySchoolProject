import bcrypt
from getpass import getpass

from settings import Settings
from models.user import User

def main():

	settings = Settings() #constraint NOT NULL = TIDAK BOLEH KOSONG, UNIQUE
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			username TEXT NOT NULL UNIQUE,
			password TEXT NOT NULL,
			first TEXT NOT NULL,
			last TEXT NOT NULL,
			day TEXT DEFAULT "" NOT NULL,
			month TEXT DEFAULT "" NOT NULL,
			year TEXT DEFAULT "" NOT NULL,
			pic TEXT DEFAULT "assets/img/default.png" NOT NULL)
		""") #doc string / comment, multiplelines comment
	settings.cur.execute("""SELECT * FROM users WHERE username = "admin" """)
	user = settings.cur.fetchone()

	if not user:
		admin = User(username="admin", first="super", last="admin", day=1, month="January", year=2000)
		password = getpass("Input New Password for Admin\npassword : ")
		retype_password = getpass("Retype\nPassword : ")
		attempts = 0

		while retype_password != password:
			if attempts == 3:
				print("limit exceeded, please try again.")
				break 

			print("Password doesn't match")
			attempts += 1
			retype_password = getpass("Retype\nPassword : ")

		else:
			admin.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			settings.cur.execute("""
				INSERT INTO users (username, password, first, last, day, month, year)
				VALUES (:username, :password, :first, :last, :day, :month, :year)
				""", {
				"username" : admin.username,
				"password" : admin.password,
				"first" : admin.first,
				"last" : admin.last,
				"day" : admin.day,
				"month" : admin.month,
				"year" : admin.year
				})
			settings.conn.commit()
			print("Done")

	else:
		print("admin already exists.")
		confirm = input("Do you want to make an account as a user (y/n)? ").lower()

		if confirm == "y":
			day_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
			month_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
			attempts = 0

			print("Okay, Please fullfil this data")
			user_username = input("Username : ")
			user_password = getpass("Password : ")
			user_firstname = input("First Name : ")
			user_lastname = input("Last Name : ")
			user_daybirth = input("Day of Birth : ")
			while user_daybirth not in day_list or user_daybirth.isalpha():
				print("Please input in number and no more than 31 | ex: '1' '20'")
				user_daybirth = input("Day of Birth : ")
			else:
				user_monthbirth = input("Month of Birth : ")
				while user_monthbirth.isalpha() or user_monthbirth not in month_list:
					print("Please Input in number and no more than 12 | ex: '1' '12'")
					user_monthbirth = input("Month of Birth : ")
				else:
					if user_monthbirth == month_list[0]:
						user_monthbirth = "January"
					elif user_monthbirth == month_list[1]:
						user_monthbirth = "February"
					elif user_monthbirth == month_list[2]:
						user_monthbirth = "March"
					elif user_monthbirth == month_list[3]:
						user_monthbirth = "April"
					elif user_monthbirth == month_list[4]:
						user_monthbirth = "May"
					elif user_monthbirth == month_list[5]:
						user_monthbirth = "June"
					elif user_monthbirth == month_list[6]:
						user_monthbirth = "July"
					elif user_monthbirth == month_list[7]:
						user_monthbirth = "August"
					elif user_monthbirth == month_list[8]:
						user_monthbirth = "September"
					elif user_monthbirth == month_list[9]:
						user_monthbirth = "October"
					elif user_monthbirth == month_list[10]:
						user_monthbirth = "November"
					elif user_monthbirth == month_list[11]:
						user_monthbirth = "December"
					user_yearbirth = input("Year of Birth : ")
					while len(user_yearbirth) > 4 or user_yearbirth.isalpha():
						print("Please input in number and no more than 5 numbers | ex: '2000' '700'")
						user_yearbirth = input("Year of Birth : ")
					else:
						new_user = User(username=user_username, first=user_firstname, last=user_lastname, day=user_daybirth, month=user_monthbirth, year=user_yearbirth)
						new_user.password = bcrypt.hashpw(user_password.encode("utf-8"), bcrypt.gensalt())

						settings.cur.execute("""
							INSERT INTO users (username, password, first, last, day, month, year)
							VALUES (:username, :password, :first, :last, :day, :month, :year)
							""", {
							"username" : new_user.username,
							"password" : new_user.password,
							"first" : new_user.first,
							"last" : new_user.last,
							"day" : new_user.day,
							"month" : new_user.month,
							"year" : new_user.year
							})
						settings.conn.commit()
						print("Done, now you can login to your dashboard with this username")

		elif confirm == "n":
			print("Okay, BYE!")

		else:
			print("Please type either 'y' or 'n'")


if __name__ == "__main__":
	main()