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

		level_qs = ''

		while level_qs != 'q':

			system('cls')

			print('\tIf you are user, enter "USER" or if you are admin, input"ADMIN or if you want to Quit, type Q"\n')
			level_qs = input('Input here : ').upper()

			if level_qs == 'USER':

				system('cls')

				print("\tThis application was created to communicate with a robot and all questions that will be asked have been summarized by the creator as a general question. Therefore, please select the question number.\n")
				print('Before you go through to the main application, the creator want to know your profile.')
				time.sleep(10)
				
				feature.introduce()

				system('cls')
				
				qs_choice = ""

				while qs_choice != "q":
					system('cls')
					feature.print_qs()
					qs_choice = input('Type in number 1 - 10 or MATH or Q or ABOUT: ').upper()

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

					elif qs_choice == 'ABOUT':
						feature.about()
						input('\nENTER to Exit')

					elif qs_choice == 'Q':
						break

					else:
						print('\nPlease type in number 1 - 10 or Q or MATH or ABOUT')
						input('\nENTER to Exit')

			elif level_qs == 'ADMIN':
				
				system('cls')
				print('Welcome Admin')
				time.sleep(1)
				passLogin_admin = feature.login_admin()

				if passLogin_admin:

					system('cls')
					admin_cs = ''

					while admin_cs != 'q':
						system('cls')
						feature.admin_qs()
						admin_cs = input('Type in DEL or VIEW or Q : ').upper()

						if admin_cs == 'DEL':
							feature.delUser()
							input('\n[ENTER] to Exit')

						elif admin_cs == 'VIEW':
							feature.viewUser()
							input('\n[ENTER] to Exit')

						elif admin_cs == 'Q':
							break

						else:
							print('\nPlease type DEL or VIEW or Q')

				else:
					print('\t\n Your trial has exceeded the limit, please wait 30 seconds and then try again.')


			elif level_qs == 'Q':
				print('Before you exit this application, the creator wants to know your satisfaction.')
				feature.satisfy()
				break

			else:
				print('Please type in User or Admin or Q')
				input('\nENTER to Exit')

			
	else:
		print('\t\n Your trial has exceeded the limit, please wait 30 seconds and then try again.')
		time.sleep(30)

else:
	print('There was a problem in the application. Please check your coding !')