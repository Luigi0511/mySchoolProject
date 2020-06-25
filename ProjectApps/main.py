from json import load, dump
from os import system
import feature
import time
from os import system

statusLoading = feature.loadData()

if statusLoading :
	system('cls')
	print('\t The application is ready to run')
	time.sleep(1)
	system('cls')
	passLogin = feature.login()
	if passLogin:
		print('This application was created to communicate with a robot and all questions that will be asked have been summarized by the creator as a general question. Therefore, please select the question number.\n')
		print('\t Before you go through to the main application, the creator want to know your profile.\n')
		time.sleep(10)
		
		feature.introduce()

		system('cls')
		
		qs_choice = ""

		while qs_choice != "q":
			system('cls')
			feature.print_qs()
			qs_choice = input('Type in number 1 - 10 or MATH or DEL or VIEW or Q or ABOUT: ').upper()

			if qs_choice == '1':
				feature.qs_1()
				input('\nENTER to EXIT')

			elif qs_choice == '2':
				feature.qs_2()
				input('\nENTER to EXIT')

			elif qs_choice == '3':
				feature.qs_3()
				input('\nENTER to EXIT')

			elif qs_choice == '4':
				feature.qs_4()
				input('\nENTER to EXIT')

			elif qs_choice == '5':
				feature.qs_5()
				input('\nENTER to EXIT')

			elif qs_choice == '6':
				feature.qs_6()
				input('\nENTER to EXIT')

			elif qs_choice == '7':
				feature.qs_7()
				input('\nENTER to EXIT')

			elif qs_choice == '8':
				feature.qs_8()
				input('\nENTER to EXIT')

			elif qs_choice == '9':
				feature.qs_9()
				input('\nENTER to EXIT')

			elif qs_choice == '10':
				feature.qs_10()
				input('\nENTER to EXIT')

			elif qs_choice == 'MATH':
				feature.mathCount()
				input('\nENTER to Exit')

			elif qs_choice == 'DEL':
				feature.delUser()
				input('\nENTER to Exit')

			elif qs_choice == 'VIEW':
				feature.viewUser()
				input('\nENTER to Exit')

			elif qs_choice == 'ABOUT':
				feature.about()
				input('\nENTER to Exit')

			elif qs_choice == 'Q':
				print('Before you exit this application, the creator wants to know your satisfaction.')
				feature.satisfy()
				break

			else:
				print('\nPlease type in number 1 - 10 or DEL or VIEW or Q')
				input('\nENTER to Exit')
			
	else:
		print('\t\n Your trial has exceeded the limit, please wait 30 seconds and then try again.')
		time.sleep(30)

else:
	print('There was a problem in the application. Please check your coding !')