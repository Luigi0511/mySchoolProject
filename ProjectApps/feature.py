from json import load, dump
from os import system
from getpass import getpass
import time
from datetime import datetime 

fileUser = 'user.json'
fileHistory = 'history.json'

user = {}
history = {}

today = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
user_session = ""

def loadData():
	global user, history

	with open(fileUser) as f:
		user = load(f)

	with open(fileHistory) as f:
		history = load(f)

	return True	

def login():
	print('\t Enter "LUIGI" as Username and enter "1234567890" as Password \n')
	time.sleep(1)
	counter = 1
	Username = input('Username : ')
	Password = getpass('Password : ')
	dataCheck = False
	passLogin = False  
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)
	else:
		dataCheck = False
		passLogin = False

	while not dataCheck or not passLogin:
		counter += 1
		if counter > 3:
			return False
		print('\tPlease Enter the correct Username or Password ! Try again !\n')
		Username = input('Username : ')
		Password = getpass('Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
		else:
			dataCheck = False
			passLogin = False
		
	else:
		print('\tLogin Passed ! \n')
		return True

def saveData():
	global history, user

	with open(fileUser, "w") as f:
		dump(user, f)

	with open(fileHistory, "w") as f:
		dump(history, f)

	return True

def introduce():
	global history, today, user_session

	print('Hi there')
	input('Say Hi : ')
	print('\nWhat is your name ? ')
	user_name = input('My name is ')

	if user_name not in history:
		data = {}

		print('\nHow old are you ? ')
		data['Age'] = input("I'm (Type in number) ")
		print('\nAre you a Boy or a girl ?')
		data['Gender'] = input("I'm a  ")
		data['Mood'] = {}
		data['Criticism'] = {}
		history[user_name] = data

		saveData()
		print('Saving data ...')
		time.sleep(1)
		print('Data Saved')

	else:
		print(f'\t\n Welcome back ! {user_name}\n')
		time.sleep(1)

		if today not in history[user_name]["Mood"]:

			list_user_mood = []

			print('How are you ? Long time no see !')
			user_mood = input('I am ')
			list_user_mood.append(user_mood)
			history[user_name]["Mood"][today] = list_user_mood


		else:
			user_mood = input(f'Are you still {history[user_name]["Mood"][today][0]} ? ')
			history[user_name]["Mood"][today].append(user_mood)

		print('\nHope you always cheerful and be a fortunate person.')
		user_session = user_name
		time.sleep(2)
		saveData()

def print_qs():
	print('Welcome to Message Apps')
	print('These are the Questions for the robot.')
	print('1. What is your name ?')
	print('2. How old are you ?')
	print('3. Who created you ?')
	print('4. Where do you live ?')
	print('5. What is your ambition ?')
	print('6. What is your hobby ?')
	print('7. Can you seduce me ?')
	print('8. Can you make a joke for me ?')
	print('9. What programming language your creator uses to make you ?')
	print('10. Who is your creator teacher ?')
	print('MATH. Calculating mathematics')
	print('DEL. DELETE USER ACCOUNT ')
	print('VIEW. View Username')
	print('ABOUT. About this application')
	print('Q. Quit')

def qs_1():
	print('My name is NewbieX-RoboPy.')

def qs_2():
	print('I was born at June / 26 / 2020. You can count my age.')

def qs_3():
	print('My creator is Luigi Emiliandra.')

def qs_4():
	print('I live anywhere.')

def qs_5():
	print('My ambition is I wanna serve the world and I benefit the world.')

def qs_6():
	print('My hobby is chatting with you.')

def qs_7():
	number_choice = input('Enter the number between 1 or 2 : ')

	if number_choice == '1':
		print('Since I know you, I want to keep learning, but learning to be the best for you.')
	elif number_choice == '2':
		print("If I become the people's representative, I will definitely fail. How do I want to think about the people, if only you always in mind.")
	else:
		print('Type number 1 or 2')

def qs_8():
	joke_choice = input('Enter the number between 1 or 2 : ')
	if joke_choice == '1':
		print('Setelah aku nonton film Avagers dengan seksama. Aku mengerti ada satu hero yang saigan dengan Aquaman')
		print('AIRonman')
	elif joke_choice == '2':
		print('Dulu aku nonton film azab. Bukannya malah tobat, eh malah hafal lagu Opick [:"(]')
	else:
		print('Type number 1 or 2')
		
def qs_9():
	print('My creator uses the Python Programming Language.')

def qs_10():
	print("My creator's teacher is Anas Azhar.")

def mathCount():
	math1 = int(input('Enter your 1st number : '))
	math2 = int(input('Enter your 2nd number : '))
	math_qs = ""
	time.sleep(1)
	
	while math_qs != 'q':
		system('cls')
		print('1. Addition (+)')
		print('2. Subtraction (-)')
		print('3. Remainder (Modulo) (%)')
		print('4. Division (/)')
		print('5. Integer Division (//)')
		print('6. Multiplication (*)')
		print('7. Power (Exponentiation) (^)')
		print('BACK. Exit from this tab, back to home')
		math_qs = input('Type in number 1 - 7 or BACK : ').upper()

		if math_qs == '1':
			print(f'{math1} + {math2} = ', math1 + math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '2':
			print(f'{math1} - {math2} = ', math1 - math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '3':
			print(f'{math1} % {math2} = ', math1 % math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '4':
			print(f'{math1} / {math2} = ', math1 / math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '5':
			print(f'{math1} // {math2} = ', math1 // math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '6':
			print(f'{math1} * {math2} = ', math1 * math2)
			input('\n[ENTER] to Exit')

		elif math_qs == '7':
			print(f'{math1} ^ {math2} = ', math1 ** math2)
			input('\n[ENTER] to Exit')

		elif math_qs == 'BACK':
			break
			print_qs()

		else:
			print('Please input the number 1 - 7 ! or BACK')
			input('\n[ENTER] to Exit')

def delUser():
	user_name = input('Enter the name that will be deleted : ')

	if user_name in history:
		del history[user_name]
		saveData()
		print('\nDeleting ...')
		time.sleep(1)
		print('Username deleted.')

	else:
		print(f'\n{user_name} never login to this app.')

def viewUser():
	if len(history) > 0:
		for info in history:
			print(f'Name : \t {info} \t Age : {history[info]["Age"]} \t Gender : {history[info]["Gender"]} \t Mood : {history[info]["Mood"]}')

	else:
		print('There is no user before or the previous user had been deleted his / her name in this application')

def about():
	print('Program atau Aplikasi ini resmi dipublikasikan pada tanggal 26 Juni 2020 dengan nama "Message Application". Program atau Aplikasi ini dibuat oleh Luigi Emiliandra dalam bimbingan Sr. Anas Azhar (Guru Python di sekolah SMP/SMA Ignatius Global School) dan juga selaku penasehat dalam program atau aplikasi ini. Program atau aplikasi ini juga tidak lepas dari dukungan dari teman teman sepeguruan dan juga saran saran atas fitur - fitur yang ada di dalam aplikasi ini sehingga berjalan dengan baik dan lancar. Saya mengucapkan terima kasih banyak kepada semua orang yan telah membantu saya dalam membuat aplikasi maupun mendukung proses pembuatan aplikasi ini.')

def satisfy():
	global today, user_session, history

	satisfy = input('Do you like this program ? (Y/N) ').upper()
				
	if satisfy == 'Y':
		print('Alhamdulilah')

	elif satisfy == 'N':
		criticism = input('\nDo you have any criticism to say ? (Y/N) ').upper()
		if criticism == 'Y':
			
			if today not in history[user_session]["Criticism"]:

				list_user_criticism = []

				user_critic = input('Input your criticism here : \n')
				
				list_user_criticism.append(user_critic)
				history[user_session]["Criticism"][today] = list_user_criticism


			else:
				user_critic = input('Input your more critic : \n')
				history[user_session]["Criticism"][today].append(user_critic)


		elif criticism == 'N':
			print('\nOK. You may go. Thanks for trying. Bye !')

		else:
			print('Type in letter Y or N !')

	else:
		print('Type in letter Y or N !')

	saveData()
	time.sleep(1)

