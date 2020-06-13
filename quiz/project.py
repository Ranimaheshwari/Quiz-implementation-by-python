import os
import pickle
import random
from prettytable import PrettyTable
import time

######################### MAIN MENU ######################
def menu():
	os.system('cls')
	print('''
		**** !! QUIZ !! ****

		(1) ADMIN LOG-IN
		(2) CREATE USER
		(3) USER LOGIN
		(4) HIGH SCORE
		(5) HELP
		(6) EXIT

		Note:press the key you want to choose.
		     like press 1 for Admin pannel.
		''')
	a=input("Enter your choice:")
	if(a=='1'):
		admin_login()
	elif(a=='2'):
		user()
	elif(a=='3'):
		login()
	elif(a=='4'):
		high_score()
	elif(a=='5'):
		help()
	elif(a=='6'):
		print("EXITTING ->>>>>")
		exit()
	else:
		print("PLEASE press valid key!!")
		input('Press Enter')
		os.system('cls')
		menu()


######################## ADMIN LOGIN ######################
def admin_login():
	os.system('cls')
	print("ADMIN LOG-IN PANNEL....")
	i=input("Enter USER NAME = ")
	j=input("Enter PASSWORD = ")
	if(i=='Maheshwarirani13' and j=='ranimaheshwari'):
		print("LOG IN SUCCESFULLY.. :)")
		input('Press Enter...')
		admin()
	else:
		print('THERE IS AN ERROR IN ADMIN DETAILS!!')
		input('Press Enter...')
		os.system('cls')
		menu()


######################## ADMIN MENU ######################
def admin():
	os.system('cls')
	print("ADMIN PANNEL....")
	k=input('''

		(1) ALL QUESTIONS
		(2) ADD QUESTION
		(3) DELETE QUESTION
		(4) SEE ALL USERS
		(5) LOG OUT

		Enter your choice:''')
	if(k=='1'):
		all_ques()
	elif(k=='2'):
		add_ques()
	elif(k=='3'):
		del_ques()
	elif(k=='4'):
		see_users()
	elif(k=='5'):
		menu()
	else:
		print("your choice is invalid!! PLEASE enter valid choice..")
		input('Press Enter...')
		os.system('cls')
		admin()



######################## SEE ALL QUES ######################
def all_ques():  
	os.system('cls')
	print("ALL QUESTIONS ARE:")
	f=open("ques_for_quiz.txt","rb")
	dict_ques=pickle.load(f)
	for i in dict_ques:
		print("Q",i,".) ",dict_ques[i][0])
		print('1) {:<20} 2) {}'.format(dict_ques[i][1],dict_ques[i][2]))
		print('3) {:<20} 4) {}'.format(dict_ques[i][3],dict_ques[i][4]))
		print("correct-> ",dict_ques[i][5])
	f.close()
	input('Press Enter...')
	os.system('cls')
	admin()


######################## ADD QUES ######################
def add_ques():
	os.system('cls')
	f=open("ques_for_quiz.txt","rb")
	dict_ques=pickle.load(f)
	f.close()
	f=open("ques_for_quiz.txt","wb")
	print("ADD QUESTION PANNEL...")
	ques=input("QUESTION : ")
	op1=input("OPTION (1) : ")
	op2=input("OPTION (2) : ")
	op3=input("OPTION (3) : ")
	op4=input("OPTION (4) : ")
	op=input("CORRECT OPTION : ")
	dict_ques[len(dict_ques)+1]=[ques,op1,op2,op3,op4,op]
	pickle.dump(dict_ques,f)
	print("Questions has added...")
	f.close()
	input('Press Enter...')
	os.system('cls')
	admin()



######################## DELETE QUES ######################
def del_ques():
	os.system('cls')
	print("Delete QUESTION PANNEL...")
	print("ALL QUESTIONS ARE:")
	f=open("ques_for_quiz.txt","rb")
	dict_ques=pickle.load(f)
	for i in dict_ques:
		print("Ques ->",i,dict_ques[i][0])
		print("(a.)",dict_ques[i][1])
		print("(b.)",dict_ques[i][2])
		print("(c.)",dict_ques[i][3])
		print("(d.)",dict_ques[i][4])
		print("correct-> ",dict_ques[i][5])
	f.close()
	f=open("ques_for_quiz.txt","wb")
	a=int(input("Enter the key to delete that question : "))
	dict_ques.pop(a)
	pickle.dump(dict_ques,f)
	print("Question has deleted...")
	f.close()
	input('Press Enter...')
	os.system('cls')
	admin()



######################## SEE USER ######################
def see_users():
	os.system('cls')
	print("ALL USERS ARE : ")
	f=open("user_info.txt","rb")
	mydict=pickle.load(f)
	f.close()
	x=PrettyTable()
	x.field_names=['USER ID','NAME','GENDER','DOB','PASSWORD','SCORE']
	for i in mydict:
		x.add_row(mydict[i])
	print(x)
	input('Press Enter to continue...')
	os.system('cls')
	admin()


######################## CREATE USER ######################
def user():
	os.system('cls')
	print("USER REGISTRATION PANNEL....")
	file=open("user_info.txt","rb")
	mydict=pickle.load(file)
	file.close()
	user_id=input("USER ID = ")
	for i in mydict:
		if mydict[i][0]==user_id:
			print("Please enter a unique user ID.")
			time.sleep(3)
			user()
	name=input("USER NAME = ")
	dob=input("DATE OF BIRTH = ")
	gen=input("GENDER = ")
	password=input("PASSWORD = ")
	mydict[len(mydict)+1]=[user_id,name,dob,gen,password,0]
	f=open("user_info.txt","wb")
	pickle.dump(mydict,f)
	f.close()
	print("REGISTRED SUCCESFLLY..")
	input('press enter ...')
	os.system('cls')
	call(user_id)

	
######################## CALL ######################
def call(user_id):
	os.system('cls')
	a=(input('''
		USER PANNEL->>>

		   (1) VIEW DETAILS
		   (2) MODIFY DETAILS
		   (3) DELETE ACCOUNT
		   (4) PLAY
		   (5) LOG OUT

		      Enter your choice : '''))
	if(a=='1'):
		details(user_id)
	elif (a=='2'):
		modify(user_id)
	elif (a=='3'):
		del_acc(user_id)
	elif (a=='4'):
		play(user_id)
	elif (a=='5'):
		menu()
	else:
		print("Invalid choice..")
		input('Press Enter')
		os.system('cls')
		call(user_id)


######################## LOG-IN ######################
def login():
	os.system('cls')
	print("USER_LOGIN PANNEL....")
	user_info=open("user_info.txt","rb")
	mydict=pickle.load(user_info)
	user_info.close()
	user_id=input("USER ID = ")
	pswd=input("PASSWORD = ")
	for i in mydict:
		if (mydict[i][0]==user_id and mydict[i][4]==pswd):
			print("LOG-IN SUCCESFULLY...")
			input('press enter to continue...')
			os.system('cls')
			call(user_id)
		else:
			print("WRONG DETAILS!!")
			input('Press Enter')
			os.system('cls')
			menu()


######################## DETAILS ######################
def details(user_id):
	os.system('cls')
	print("USER DETAILS")
	f=open("user_info.txt","rb")
	mydict=pickle.load(f)
	f.close()
	x=PrettyTable()
	x.field_names=['USER ID','NAME','GENDER','DOB','PASSWORD','SCORE']
	for i in mydict:
		if mydict[i][0]==user_id:
			x.add_row(mydict[i])
	print(x)
	input('Press Enter to continue...')
	call(user_id)



######################## MODIFY ######################
def modify(x):
	os.system('cls')
	file=open("user_info.txt","rb")
	mydict=pickle.load(file)
	file.close()
	
	name=input("Enter new name:")
	gen=input("Enter new gen:")
	dob=input("Enter new dob:")
	pswd=input("Enter new password:")
	for i in mydict:
		if mydict[i][0]==x:
			mydict[i][1]=name
			mydict[i][2]=gen
			mydict[i][3]=dob
			mydict[i][4]=pswd
	file=open("user_info.txt",'wb')
	pickle.dump(mydict,file)
	file.close()
	input('Press Enter...')
	os.system('cls')
	call(x)


######################### DELETE ACCOUNT ######################
def del_acc(user_id):
	os.system('cls')
	print("DELETE_ACCOUNT PANNEL....")
	user_info=open("user_info.txt","rb")
	mydict=pickle.load(user_info)
	user_info.close()
	for i in mydict:
		if (mydict[i][0]==user_id):
			mydict.pop(i)
			break
	file=open("user_info.txt",'wb')
	pickle.dump(mydict,file)
	file.close()
	print("DELETED SUCCESSFULLY ...")
	input('Press Enter to continue...')
	os.system('cls')
	menu()

######################### PLAY ######################
def play(user_id):
	os.system('cls')
	file=open("ques_for_quiz.txt","rb")
	dict_ques=pickle.load(file)
	file.close()
	score=0
	l1=dict_ques.keys()
	l1=list(l1)
	l3=[]
	for i in range(10):
		while True:
			a=random.choice(l1)
			if a not in l3:
				l3.append(a)
				break
	for a in l3:
		os.system('cls')
		print('\t\t\tQUIZ GAME')
		print(dict_ques[a][0])
		print('1) {:<20} 2) {}'.format(dict_ques[a][1],dict_ques[a][2]))
		print('3) {:<20} 4) {}'.format(dict_ques[a][3],dict_ques[a][4]))
		ch=input('Enter correct option : ')
		if ch==dict_ques[a][5]:
			score+=1
			print('Your answer is Correct :)')
		else:
			print('your answer is wrong!!')
		input('Press Enter...')
	print("\n\n\nTOTAL SCORE :",score*10," out of 100")
	file=open("user_info.txt","rb")
	mydict=pickle.load(file)
	file.close()
	for i in mydict:
		if mydict[i][0]==user_id:
			mydict[i][5]=score*10
	file=open("user_info.txt",'wb')
	pickle.dump(mydict,file)
	file.close()
	input('Press Enter to continue...')
	call(user_id)

######################### HIGH SCORE ######################
def high_score():
	os.system('cls')
	print('HIGH SCORE PANNEL ->>')
	file=open("user_info.txt","rb")
	mydict=pickle.load(file)
	file.close()
	l=[]
	for i in mydict:
		l.append(mydict[i][5])
	h=max(l)
	for i in mydict:
		if h==mydict[i][5]:
			print(mydict[i][1],"having highest score : ",h)
	input('Press Enter to continue...')
	menu()

######################### HELP ######################
def help():
	os.system('cls')
	print("HELP PANNEL....")
	print('''
		-> This QUIZ consist of 10 multiple-choice questions.
		-> To start the QUIZ you have to create your user account.
		-> If you have already registerd yourself then you have to login only.
		-> After creating your account,you can update your details.
		-> To be succesful in this compitition you have to read question carefully.
		-> You will have 4 options, and you have to write the correct option (NOT ANSWER).
		-> After submitting all the answers you will be able to see your result.
		-> If you still can't understand this game then try once.I am sure you will be able to understand the process.
		      !! THANK YOU !!''')
	input('Press Enter to continue...')
	menu()


menu()


