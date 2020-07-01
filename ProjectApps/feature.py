from json import load, dump
from os import system
from getpass import getpass
import time
from datetime import datetime 

fileUser = 'user.json'
fileHistory = 'history.json'
fileAdmin = 'admin.json'

user = {}
history = {}
admin = {}

today = str(datetime.now().year) + str(datetime.now().month) + str(datetime.now().day)
user_session = ""

def loadData():
	global user, history, admin

	with open(fileUser) as f:
		user = load(f)

	with open(fileHistory) as f:
		history = load(f)

	with open(fileAdmin) as f:
		admin = load(f)

	return True	

def login():
	print('\t Enter "Luigi" as Username and enter "1234567890" as Password \n')
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

def login_admin():
	print('Input Username and Password correctly')
	counter = 1
	Username = input('Username : ')
	Password = getpass('Password : ')
	dataCheck = False
	passLogin = False  
	if Username in admin:
		dataCheck = True
		passLogin = (admin[Username] == Password)
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
		if Username in admin:
			dataCheck = True
			passLogin = (admin[Username] == Password)
		else:
			dataCheck = False
			passLogin = False
		
	else:
		print('\tLogin Passed ! \n')
		time.sleep(2)
		return True

def saveData():
	global history, user, admin

	with open(fileUser, "w") as f:
		dump(user, f)

	with open(fileHistory, "w") as f:
		dump(history, f)

	with open(fileAdmin, "w") as f:
		dump(admin, f)
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
	print("10. Who is your creator's teacher ?")
	print('MATH. Calculating mathematics')
	print('ABOUT. About this application')
	print('Q. Quit')

def admin_qs():
	print('DEL. DELETE USER ACCOUNT ')
	print('VIEW. View Username')

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
			ans1 = math1 + math2
			print(f'{math1} + {math2} = {ans1}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					print('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans1} + {math3} = ', ans1 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans1} - {math3} = ', ans1 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans1} % {math3} = ', ans1 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans1} / {math3} = ', ans1 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans1} // {math3} = ', ans1 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans1} * {math3} = ', ans1 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans1} ^ {math3} = ', ans1 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\n[ENTER] to Exit')

		elif math_qs == '2':
			ans2 = math1 - math2
			print(f'{math1} - {math2} = {ans2}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					print('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans2} + {math3} = ', ans2 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans2} - {math3} = ', ans2 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans2} % {math3} = ', ans2 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans2} / {math3} = ', ans2 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans2} // {math3} = ', ans2 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans2} * {math3} = ', ans2 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans2} ^ {math3} = ', ans2 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\nENTER to Exit')

		elif math_qs == '3':
			ans3 = math1 % math2
			print(f'{math1} % {math2} = {ans3}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					print('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans3} + {math3} = ', ans3 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans3} - {math3} = ', ans3 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans3} % {math3} = ', ans3 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans3} / {math3} = ', ans3 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans3} // {math3} = ', ans3 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans3} * {math3} = ', ans3 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans3} ^ {math3} = ', ans3 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\nENTER to Exit')


		elif math_qs == '4':
			ans4 = math1 / math2
			print(f'{math1} / {math2} = {ans4}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					print('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans4} + {math3} = ', ans4 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans4} - {math3} = ', ans4 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans4} % {math3} = ', ans4 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans4} / {math3} = ', ans4 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans4} // {math3} = ', ans4 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans4} * {math3} = ', ans4 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans4} ^ {math3} = ', ans4 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\nENTER to Exit')


		elif math_qs == '5':
			ans5 = math1 // math2
			print(f'{math1} // {math2} = {ans5}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					prinnt('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans5} + {math3} = ', ans5 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans5} - {math3} = ', ans5 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans5} % {math3} = ', ans5 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans5} / {math3} = ', ans5 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans5} // {math3} = ', ans5 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans5} * {math3} = ', ans5 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans5} ^ {math3} = ', ans5 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\n[ENTER] to Exit')


		elif math_qs == '6':
			ans6 = math1 * math2
			print(f'{math1} * {math2} = {ans6}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					prinnt('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans6} + {math3} = ', ans6 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans6} - {math3} = ', ans6 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans6} % {math3} = ', ans6 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans6} / {math3} = ', ans6 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans6} // {math3} = ', ans6 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans6} * {math3} = ', ans6 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans6} ^ {math3} = ', ans6 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
				input('\n[ENTER] to Exit')


		elif math_qs == '7':
			ans7 = math1 ** math2
			print(f'{math1} ^ {math2} = {ans7}')
			thirdNum_qs = input('Do you want to Enter your 3rd number (Y/N) : ').upper()

			if thirdNum_qs == 'Y':
				math3 = int(input('Enter your 3rd number : '))
				math3_qs = ''
				while math3_qs != 'q':
					system('cls')
					prinnt('Enter your choice so the robot will count your qs from the previous one with the third number')
					print('1. Addition (+)')
					print('2. Subtraction (-)')
					print('3. Remainder (Modulo) (%)')
					print('4. Division (/)')
					print('5. Integer Division (//)')
					print('6. Multiplication (*)')
					print('7. Power (Exponentiation) (^)')
					print('BACK. Exit from this tab, back to home')
					math_qs_2nd = input('Type in number 1 - 7 or BACK : ').upper()

					if math_qs_2nd == '1':
						print(f'{ans7} + {math3} = ', ans7 + math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '2':
						print(f'{ans7} - {math3} = ', ans7 - math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '3':
						print(f'{ans7} % {math3} = ', ans7 % math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '4':
						print(f'{ans7} / {math3} = ', ans7 / math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '5':
						print(f'{ans7} // {math3} = ', ans7 // math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '6':
						print(f'{ans7} * {math3} = ', ans7 * math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == '7':
						print(f'{ans7} ^ {math3} = ', ans7 ** math3)
						input('\n[ENTER] to Exit')

					elif math_qs_2nd == 'BACK':
						break
						print_qs()

					else:
						print('Please type in 1-7 or Back')
						input('\n[ENTER] to Exit')
						
			elif thirdNum_qs == 'N':
				print('Okay, No problem')
				input('\n[ENTER] to Exit')

			else:
				print('Please input letter Y or N')
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
	print('Indonesian \t : Program atau Aplikasi ini resmi dipublikasikan pada tanggal 26 Juni 2020 dengan nama "Message Application". Program atau Aplikasi ini dibuat oleh Luigi Emiliandra dalam bimbingan Sr. Anas Azhar (Guru Python di sekolah SMP/SMA Ignatius Global School) dan juga selaku penasehat dalam program atau aplikasi ini. Program atau aplikasi ini juga tidak lepas dari dukungan dari teman teman sepeguruan dan juga saran saran atas fitur - fitur yang ada di dalam aplikasi ini sehingga berjalan dengan baik dan lancar. Saya mengucapkan terima kasih banyak kepada semua orang yan telah membantu saya dalam membuat aplikasi maupun mendukung proses pembuatan aplikasi ini.')
	print('\nEnglish \t : This program or application was officially published on June 26, 2020 under the name "Message Application". This program or application was made by Luigi Emiliandra in the guidance of Sr. Anas Azhar (Python teacher at Ignatius Global School Middle School / High School) and also as an advisor in this program or application. This program or application is also inseparable from the support of fellow peers and also suggestions for features in this application so that it runs well and smoothly. I would like to thank everyone who helped me in making the application and supporting the process of making this application.')
	print('\nJapanese (Nihongo) \t : Kono puroguramu matawa apurikēshon wa,`messējiapurikēshon` to iu namae de 2020-nen 6 tsuki 26-nichi ni seishiki ni kōkai sa remashita. Kono puroguramu matawa apurikēshon wa, Lrigi Emiliandra ga Sr no shidō de sakusei shita monodesu. Anas Azhar (Ignatius gurōbarusukūru chūgakkō/ kōkō no paison kyōshi). Mata, kono puroguramu matawa apurikēshon no adobaizā to shite mo. Kono puroguramu matawa apurikēshon wa, hoka no Pia no sapōto ya, kono apurikēshon no kinō no teian to kirihanasu koto mo dekinai tame, tekisetsu katsu sumūzu ni jikkō sa remasu. Apurikēshon no sakusei to, kono apurikēshon no sakusei purosesu no sapōto de watashi o tasukete kureta subete no hito ni kansha shimasu.')
	print('\nChinese(Simplified)(Zhōngwén) \t : Gāi chéngxù huò yìngyòng chéngxù yú 2020 nián 6 yuè 26 rì yǐ “xiāoxī yìngyòng chéngxù” de míngchēng zhèngshì fǎ bù. Gāi chéngxù huò yìngyòng chéngxù shì yóu Luigi Emiliandra zài Sr. Anas Azhar(Ignatius quánqiú xuéxiào chūzhōng/gāozhōng de Python lǎoshī), yěshì gāi chéngxù huò yìngyòng chéngxù de gùwèn. Gāi chéngxù huò yìngyòng chéngxù yě lì bù kāi tóngxué de zhīchí yǐjí duì gāi yìngyòng chéngxù gōngnéng de jiànyì, yīncǐ tā yùnxíng liánghǎo qiě liúchàng. Wǒ yào gǎnxiè bāngzhù wǒ zhìzuò yìngyòng chéngxù bìng zhīchí gāi yìngyòng chéngxù zhìzuò guòchéng de měi gèrén.')
	print('\nMelayu \t : Program atau aplikasi ini secara rasmi diterbitkan pada 26 Jun 2020 dengan nama "Aplikasi Permesejan". Program atau aplikasi ini dibuat oleh Luigi Emiliandra dalam bimbingan Sr. Anas Azhar (guru Python di Ignatius Global School Middle School / High School) dan juga sebagai penasihat dalam program atau aplikasi ini. Program atau aplikasi ini juga tidak dapat dipisahkan dari sokongan rakan sebaya dan juga cadangan ciri-ciri dalam aplikasi ini agar dapat berjalan dengan baik dan lancar. Saya ingin mengucapkan terima kasih kepada semua orang yang membantu saya dalam membuat permohonan dan menyokong proses pembuatan aplikasi ini.')
	print("\nArabic \t : tama nashr hdha albarnamaj 'aw altatbiq rsmyana fi 26 yuniu 2020 taht aism 'ttabiq alrsayl'. tam taqdim hdha albarnamaj 'aw altatbiq bwastt Luigi Emiliandra bitawjih min Sr. 'anas 'azhar (mdirs Python fi madrasat Ignatius Global School al'iiedadiat / almadrasat althaanawiata) waydana kamustashar fi hadha albarnamaj 'aw altatbiqi. la yumkin fasl hdha albarnamaj 'aw altatbiq ean daem zumalayih waydana aiqtirahat lilmayzat fi hadha altatbiq bihayth yaemal bishakl jayid wasahli. 'awadu 'an 'ashkur kl min saeidni fi taqdim altalab wadaem eamaliat taqdim hdha altalab.")
	print('\nThai \t : Porkærm h̄rụ̄x xæpphlikhechạn nī̂ p̄heyphær̀ xỳāng pĕn thāngkār meụ̄̀x wạn thī̀ 26 mit̄hunāyn 2020 p̣hāy tı̂ chụ̄̀x"xæpphlikhechạn k̄ĥxkhwām" porkærm h̄rụ̄x xæpphlikhechạn nī̂ cạd thả doy Luigi Emiliandra tām khả næanả k̄hxng Sr. Anas Azhar (xācāry̒ Python thī̀ Ignatius Global School Middle School/ High School) læa pĕn thī̀ prụks̄ʹā nı porkærm h̄rụ̄x xæpphlikhechạn nī̂ porkærm h̄rụ̄x xæpphlikhechạn nī̂ yæk xxk cāk kār s̄nạbs̄nun k̄hxng pheụ̄̀xn r̀wm ngān læa khả næanả s̄ảh̄rạb khuṇs̄mbạti nı xæpphlikhechạn nī̂ pheụ̄̀x h̄ı̂ thảngān dị̂ dī læa rābrụ̄̀n c̄hạn k̄hx k̄hxbkhuṇ thuk khn thī̀ ch̀wy c̄hạn thả bı s̄mạkhr læa s̄nạbs̄nun krabwnkār s̄r̂āng bı s̄mạkhr nī̂')
	print("\nRussian \t : Eta programma ili prilozheniye bylo ofitsial'no opublikovano 26 iyunya 2020 goda pod nazvaniyem «Soobshcheniye prilozheniya». Eta programma ili prilozheniye bylo sdelano Luidzhi Emiliandroy pod rukovodstvom starshego. Anas Azar (uchitel' Python v sredney shkole / gimnazii Ignatius Global School), a takzhe v kachestve konsul'tanta v etoy programme ili prilozhenii. Eta programma ili prilozheniye takzhe neotdelimy ot podderzhki kolleg, a takzhe predlozheniy po funktsiyam v etom prilozhenii, chtoby ono rabotalo khorosho i bez sboyev. YA khotel by poblagodarit' vsekh, kto pomog mne v sozdanii zayavki i podderzhal protsess yeye sozdaniya")
	
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
