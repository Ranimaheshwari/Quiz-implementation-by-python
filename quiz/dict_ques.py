import pickle
file=open("ques_for_quiz.txt","wb")
dict_ques={}
pickle.dump(dict_ques,file)
file.close()
f=open("user_info.txt","wb")
mydict={}
pickle.dump(mydict,f)
f.close()