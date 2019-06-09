import random
a=["paper","sisor","rock"]
list_computer=(random.choice(a))
while True:
    user=raw_input("enter input")
    if(user=="paper" and list_computer=="rock"):

        print  "paper win"
    elif(user=="sisores" and list_computer=="paper"):  
        print "sisores win"

    elif(user=="rock" and list_computer=="sisores"):
        print "rock win"    

    elif(user=="rock" and list_computer=="paper"):
        print "rock loose"    
    
    elif(user=="paper" and list_computer=="sisores"):
        print "paper loose"  

    elif(user=="sisores" and list_computer=="rock"):
        print "sisores loose"  
    elif(user==list_computer):
        print "drow"    
      
      

