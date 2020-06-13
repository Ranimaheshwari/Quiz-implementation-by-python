import random
import pickle
file=open("ques_for_quiz.txt","rb")
dict_ques=pickle.load(file)
file.close()
score=0
l1=dict_ques.keys()
l1=list(l1)
print(l1)
l3=[]
for i in range(10):
	while True:
		a=random.choice(l1)
		if a not in l3:
			l3.append(a)
			break
print(l3)