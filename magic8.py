from random import *
question = input("ask me a question and I will answer")
value = randint(0, 4)
if value == 0:
    print("ofcourse")
elif value == 1:
    print("doubt it")
elif value == 2:
    print("duh!")
else:
    print("ask me later")