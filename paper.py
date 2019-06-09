import random
a=["paper","sisor","rock"]
list_computer=(random.choice(a))
user=raw_input("enter input")
if(user==list_computer):
    print "yes"