#import json
import bcrypt

from settings import Settings
from models.user import User

from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

#from json import load, dump

LabelBase.register(name="Roboto",
	fn_regular="assets/fonts/Roboto-Thin.ttf",
	fn_bold='assets/fonts/Roboto-Medium.ttf')

Window.clearcolor = get_color_from_hex("#101216")

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "My Kivy MD App"

		#self.users = self.load_data("data/users.json")
		self.settings = Settings()

		self.current_user = None
		self.dialog_box = None

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/register.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/search.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/edit.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/change_pw.kv"))

	# def load_data(self, file_location):
	# 	try:
	# 		with open(file_location) as file:
	# 			return json.load(file)
	# 	except:
	# 		return {}

	def find_user_by_username(self, username):
		with self.settings.conn:
			self.settings.cur.execute("""
					SELECT * FROM users WHERE username = :username
					""", {"username" : username})
		return self.settings.cur.fetchone()

	def logger(self):
		username_entry = self.root.screens[1].ids['username_entry'].text
		password_entry = self.root.screens[1].ids['password_entry'].text

		user = self.find_user_by_username(username_entry)

		if user:
			if bcrypt.checkpw(password_entry.encode("utf-8"), user[2]):
				self.root.screens[1].ids['msg'].text = ""
				self.root.screens[1].ids['username_entry'].text = ""
				self.root.screens[1].ids['password_entry'].text = ""

				self.current_user = User(user[1], user[3], user[4], user[5], user[6], user[7])
				self.current_user.id = user[0]
				self.current_user.pic = user[8]
				self.current_user.password = user[2]
				self.to_dashboard()
				return True
			else:
				print('not ok')

		self.root.screens[1].ids['msg'].text = "Login Gagal"
		self.root.screens[1].ids['username_entry'].text = ""
		self.root.screens[1].ids['password_entry'].text = ""

	def go_to_change_pw_page(self):
		self.screen_manager.current = "change_pw"

	def save_edited_pass(self):
		username = self.current_user.username
		old_pass = self.root.screens[6].ids['old_pass'].text
		new_pass = self.root.screens[6].ids['new_pass'].text
		retype = self.root.screens[6].ids['retype'].text

		if bcrypt.checkpw(old_pass.encode('utf-8'), self.current_user.password) and retype == new_pass:
			password = bcrypt.hashpw(new_pass.encode("utf-8"), bcrypt.gensalt())
			with self.settings.conn:
				self.settings.cur.execute("UPDATE users SET password=:password WHERE username=:username", {"password": password, "username": username})

			self.relog()

			self.root.screens[6].ids['old_pass'].text = ""
			self.root.screens[6].ids['new_pass'].text = ""
			self.root.screens[6].ids['retype'].text = ""
			self.root.screens[6].ids['warning'].text = ""

		else:
			self.root.screens[6].ids['warning'].text = "Please check old password and retype password"

	def go_to_edit_page(self):
		self.root.screens[5].ids['new_username_entry'].text = self.current_user.username
		self.root.screens[5].ids['first_name'].text = self.current_user.first
		self.root.screens[5].ids['last_name'].text = self.current_user.last
		self.root.screens[5].ids['birthday_day'].text = self.current_user.day

		if self.current_user.month == "January":
			self.root.screens[5].ids['birthday_month'].text = "1"
		elif self.current_user.month == "February":
			self.root.screens[5].ids['birthday_month'].text = "2"
		elif self.current_user.month == "March":
			self.root.screens[5].ids['birthday_month'].text = "3"
		elif self.current_user.month == "April":
			self.root.screens[5].ids['birthday_month'].text = "4"
		elif self.current_user.month == "May":
			self.root.screens[5].ids['birthday_month'].text = "5"
		elif self.current_user.month == "June":
			self.root.screens[5].ids['birthday_month'].text = "6"
		elif self.current_user.month == "July":
			self.root.screens[5].ids['birthday_month'].text = "7"
		elif self.current_user.month == "August":
			self.root.screens[5].ids['birthday_month'].text = "8"
		elif self.current_user.month == "September":
			self.root.screens[5].ids['birthday_month'].text = "9"
		elif self.current_user.month == "October":
			self.root.screens[5].ids['birthday_month'].text = "10"
		elif self.current_user.month == "November":
			self.root.screens[5].ids['birthday_month'].text = "11"
		elif self.current_user.month == "December":
			self.root.screens[5].ids['birthday_month'].text = "12"

		self.root.screens[5].ids['birthday_year'].text = self.current_user.year

		self.screen_manager.current = "edit"

	def save_edited_profile(self):
		username_before = self.current_user.username
		edited_username = self.root.screens[5].ids['new_username_entry'].text
		edited_first = self.root.screens[5].ids['first_name'].text
		edited_last = self.root.screens[5].ids['last_name'].text

		day_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
		month_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

		edited_day = self.root.screens[5].ids['birthday_day'].text
		edited_month = self.root.screens[5].ids['birthday_month'].text
		edited_year = self.root.screens[5].ids['birthday_year'].text

		if edited_username == "" or edited_first == "" or edited_last == "" or edited_day == "" or edited_month == "" or edited_year == "":
			self.root.screens[5].ids['warning'].text = "Please fullfil these data"

		elif edited_day not in day_list or edited_day.isalpha():
			self.screen_manager.screens[5].ids['warning'].text = "Please enter from 1 until 31 | ex: 1 / 31"

		elif len(edited_year) > 4 or edited_year.isalpha():
			self.screen_manager.screens[5].ids['warning'].text = "Please enter no more than 5 numbers | ex: 2000"

		elif edited_month.isalpha() or edited_month not in month_list:
			self.screen_manager.screens[5].ids['warning'].text = "Please enter from 1 - 12 | ex: 1 / 12"

		else:
			if edited_month == month_list[0]:
				edited_month = "January"
			elif edited_month == month_list[1]:
				edited_month = "February"
			elif edited_month == month_list[2]:
				edited_month = "March"
			elif edited_month == month_list[3]:
				edited_month = "April"
			elif edited_month == month_list[4]:
				edited_month = "May"
			elif edited_month == month_list[5]:
				edited_month = "June"
			elif edited_month == month_list[6]:
				edited_month = "July"
			elif edited_month == month_list[7]:
				edited_month = "August"
			elif edited_month == month_list[8]:
				edited_month = "September"
			elif edited_month == month_list[9]:
				edited_month = "October"
			elif edited_month == month_list[10]:
				edited_month = "November"
			elif edited_month == month_list[11]:
				edited_month = "December"

			with self.settings.conn:
				self.settings.cur.execute("UPDATE users SET first=:new_first WHERE username=:username", {"new_first": edited_first, "username": username_before})
				self.settings.cur.execute("UPDATE users SET last=:new_last WHERE username=:username", {"new_last": edited_last, "username": username_before})
				self.settings.cur.execute("UPDATE users SET day=:new_day WHERE username=:username", {"new_day": edited_day, "username": username_before})
				self.settings.cur.execute("UPDATE users SET month=:new_month WHERE username=:username", {"new_month": edited_month, "username": username_before})
				self.settings.cur.execute("UPDATE users SET year=:new_year WHERE username=:username", {"new_year": edited_year, "username": username_before})
				self.settings.cur.execute("UPDATE users SET username=:new_username WHERE username=:username", {"new_username": edited_username, "username": username_before})

			self.relog()

			self.root.screens[5].ids['new_username_entry'].text = self.current_user.username
			self.root.screens[5].ids['first_name'].text = self.current_user.first
			self.root.screens[5].ids['last_name'].text = self.current_user.last
			self.root.screens[5].ids['birthday_day'].text = self.current_user.day

			if self.current_user.month == "January":
				self.root.screens[5].ids['birthday_month'].text = "1"
			elif self.current_user.month == "February":
				self.root.screens[5].ids['birthday_month'].text = "2"
			elif self.current_user.month == "March":
				self.root.screens[5].ids['birthday_month'].text = "3"
			elif self.current_user.month == "April":
				self.root.screens[5].ids['birthday_month'].text = "4"
			elif self.current_user.month == "May":
				self.root.screens[5].ids['birthday_month'].text = "5"
			elif self.current_user.month == "June":
				self.root.screens[5].ids['birthday_month'].text = "6"
			elif self.current_user.month == "July":
				self.root.screens[5].ids['birthday_month'].text = "7"
			elif self.current_user.month == "August":
				self.root.screens[5].ids['birthday_month'].text = "8"
			elif self.current_user.month == "September":
				self.root.screens[5].ids['birthday_month'].text = "9"
			elif self.current_user.month == "October":
				self.root.screens[5].ids['birthday_month'].text = "10"
			elif self.current_user.month == "November":
				self.root.screens[5].ids['birthday_month'].text = "11"
			elif self.current_user.month == "December":
				self.root.screens[5].ids['birthday_month'].text = "12"

			self.root.screens[5].ids['birthday_year'].text = self.current_user.year

	def go_to_search_page(self):
		self.screen_manager.current = "search"

	def search(self):
		username = self.root.screens[4].ids['input'].text
		found = self.find_user_by_username(username)
		if found:
			if username == self.current_user.username:
				self.root.screens[4].ids['status'].text = "Can't find yourself"
			else:
				fullname = "Name     : "+found[3].title()+" "+found[4].title()
				pic = found[8]
				birthday = "Birthday : "+found[5]+" "+found[6]+" "+found[7]
				self.root.screens[4].ids['label_username'].text = username
				self.root.screens[4].ids['profile_pic'].source = pic
				self.root.screens[4].ids['label_name'].text = fullname
				self.root.screens[4].ids['label_birth'].text = birthday

		else:
			self.root.screens[4].ids['status'].text = f"No user with '{username}' username"

	def sign_up(self):
		self.screen_manager.current = "register"

	def register(self):
		username_entry = self.screen_manager.screens[3].ids['new_username_entry'].text
		password_entry = self.screen_manager.screens[3].ids['new_password_entry'].text
		first_name_entry = self.screen_manager.screens[3].ids['first_name'].text
		last_name_entry = self.screen_manager.screens[3].ids['last_name'].text
		day_entry = self.screen_manager.screens[3].ids['birthday_day'].text
		month_entry = self.screen_manager.screens[3].ids['birthday_month'].text
		year_entry = self.screen_manager.screens[3].ids['birthday_year'].text

		day_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
		month_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

		user = self.find_user_by_username(username_entry)

		if not user:
			if username_entry == "" or password_entry == "" or first_name_entry == "" or day_entry == "" or month_entry == "" or year_entry == "" or last_name_entry == "":
				self.screen_manager.screens[3].ids['taken'].text = "Please fulfill your data"
			elif day_entry not in day_list or day_entry.isalpha():
				self.screen_manager.screens[3].ids['taken'].text = "Please enter from 1 until 31 | ex: 1 / 31"
				self.screen_manager.screens[3].ids['birthday_day'].text = ""

			elif len(year_entry) > 4 or year_entry.isalpha():
				self.screen_manager.screens[3].ids['taken'].text = "Please enter no more than 5 numbers | ex: 2000"
				self.screen_manager.screens[3].ids['birthday_year'].text = ""

			elif month_entry.isalpha() or month_entry not in month_list:
				self.screen_manager.screens[3].ids['taken'].text = "Please enter from 1 - 12"
				self.screen_manager.screens[3].ids['birthday_month'].text = ""

			else:
				if month_entry == month_list[0]:
					month_entry = "January"
				elif month_entry == month_list[1]:
					month_entry = "February"
				elif month_entry == month_list[2]:
					month_entry = "March"
				elif month_entry == month_list[3]:
					month_entry = "April"
				elif month_entry == month_list[4]:
					month_entry = "May"
				elif month_entry == month_list[5]:
					month_entry = "June"
				elif month_entry == month_list[6]:
					month_entry = "July"
				elif month_entry == month_list[7]:
					month_entry = "August"
				elif month_entry == month_list[8]:
					month_entry = "September"
				elif month_entry == month_list[9]:
					month_entry = "October"
				elif month_entry == month_list[10]:
					month_entry = "November"
				elif month_entry == month_list[11]:
					month_entry = "December"

				new_user = User(username=username_entry, first=first_name_entry.title(), last=last_name_entry.title(), day=day_entry, month=month_entry, year=year_entry)
				new_user.password = bcrypt.hashpw(password_entry.encode("utf-8"), bcrypt.gensalt())
				self.settings.cur.execute("""
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
				self.settings.conn.commit()
				self.screen_manager.screens[3].ids['taken'].text = "Registered Successfully !"
				self.screen_manager.screens[3].ids['taken'].color = 0,1,0,1
				self.screen_manager.screens[3].ids['back_text'].text = "You can press 'Back' to go to login page"
		else:
			self.screen_manager.screens[3].ids['taken'].text = "Username had already been taken"

		self.screen_manager.screens[3].ids['new_username_entry'].text = ""
		self.screen_manager.screens[3].ids['new_password_entry'].text = ""
		self.screen_manager.screens[3].ids['first_name'].text = ""
		self.screen_manager.screens[3].ids['last_name'].text = ""
		self.screen_manager.screens[3].ids['birthday_day'].text = ""
		self.screen_manager.screens[3].ids['birthday_month'].text = ""
		self.screen_manager.screens[3].ids['birthday_year'].text = ""

	def build(self):
		self.screen_manager.current = "login"
		return self.screen_manager

	#def on_start(self):
		#Clock.schedule_once(self.to_login_page, 3)

	def to_login_page(self, *args):
		self.screen_manager.current = "login"

	def to_dashboard(self):
		fullname = "Name     : "+self.current_user.first.title()+" "+self.current_user.last.title()
		pic = self.current_user.pic
		birthday = "Birthday : "+self.current_user.day+" "+self.current_user.month+" "+self.current_user.year

		self.root.screens[2].ids['label_username'].text = self.current_user.username
		self.root.screens[2].ids['profile_pic'].source = pic

		self.root.screens[2].ids['full_name'].text = fullname
		self.root.screens[2].ids['birthday'].text = birthday

		self.root.current = "dashboard"

		self.root.screens[5].ids['new_username_entry'].text = self.current_user.username
		self.root.screens[5].ids['first_name'].text = self.current_user.first
		self.root.screens[5].ids['last_name'].text = self.current_user.last
		self.root.screens[5].ids['birthday_day'].text = self.current_user.day

		if self.current_user.month == "January":
			self.root.screens[5].ids['birthday_month'].text = "1"
		elif self.current_user.month == "February":
			self.root.screens[5].ids['birthday_month'].text = "2"
		elif self.current_user.month == "March":
			self.root.screens[5].ids['birthday_month'].text = "3"
		elif self.current_user.month == "April":
			self.root.screens[5].ids['birthday_month'].text = "4"
		elif self.current_user.month == "May":
			self.root.screens[5].ids['birthday_month'].text = "5"
		elif self.current_user.month == "June":
			self.root.screens[5].ids['birthday_month'].text = "6"
		elif self.current_user.month == "July":
			self.root.screens[5].ids['birthday_month'].text = "7"
		elif self.current_user.month == "August":
			self.root.screens[5].ids['birthday_month'].text = "8"
		elif self.current_user.month == "September":
			self.root.screens[5].ids['birthday_month'].text = "9"
		elif self.current_user.month == "October":
			self.root.screens[5].ids['birthday_month'].text = "10"
		elif self.current_user.month == "November":
			self.root.screens[5].ids['birthday_month'].text = "11"
		elif self.current_user.month == "December":
			self.root.screens[5].ids['birthday_month'].text = "12"

		self.root.screens[5].ids['birthday_year'].text = self.current_user.year

		self.root.screens[6].ids['old_pass'].text = ""
		self.root.screens[6].ids['new_pass'].text = ""
		self.root.screens[6].ids['retype'].text = ""
		self.root.screens[6].ids['warning'].text = ""

		self.root.screens[4].ids['input'].text = ""
		self.root.screens[4].ids['status'].text = "..."
		self.root.screens[4].ids['label_username'].text = "Username"
		self.root.screens[4].ids['label_name'].text = "Name"
		self.root.screens[4].ids['label_birth'].text = "Birthday"

		self.root.screens[2].ids['nav_drawer'].set_state('close')

	def close_dialog(self, *args):
		self.dialog_box.dismiss()
		self.root.screens[2].ids['nav_drawer'].set_state('close')

	def exit(self, *args):
		self.close_dialog()
		self.current_user = None
		self.root.current = "login"

	def exit_(self, *args):
		self.dialog_box.dismiss()
		self.current_user = None
		self.root.current = "login"

	def sign_out(self, *args):
		if not self.dialog_box:
			self.dialog_box = MDDialog(
				title="Konfirmasi Keluar",
				text="Apakah yakin keluar dari aplikasi?",
				buttons=[
					MDFlatButton(
						text="Batal",
						on_release= self.close_dialog
						),
					MDFlatButton(
						text="Ya",
						on_release= self.exit
						)
				]
				)
		
		self.dialog_box.open()

	def relog(self, *args):
		if not self.dialog_box:
			self.dialog_box = MDDialog(
				title="Relog Confirmation",
				text="Press 'Relog' button to refresh your changes",
				buttons=[
					MDFlatButton(
						text="Relog",
						on_release= self.exit_
						)
				]
				)
		
		self.dialog_box.open()

	def back_to_login_page(self):
		self.screen_manager.current = "login"
		self.screen_manager.screens[3].ids['new_username_entry'].text = ""
		self.screen_manager.screens[3].ids['new_password_entry'].text = ""
		self.screen_manager.screens[3].ids['first_name'].text = ""
		self.screen_manager.screens[3].ids['last_name'].text = ""
		self.screen_manager.screens[3].ids['birthday_day'].text = ""
		self.screen_manager.screens[3].ids['birthday_month'].text = ""
		self.screen_manager.screens[3].ids['birthday_year'].text = ""


if __name__ == "__main__":
	app = MyApp()
	app.run()