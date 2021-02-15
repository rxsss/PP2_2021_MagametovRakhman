#Global variables
x = "rxsss"

def myFunc():
    print("My nickname is " + x)

myFunc()

def hisFunc():
    x = "rax1s" #x = "rax1s" only inside of this function
    print("My nickname is " + x)
hisFunc()
print("My nickname is " + x)




def herFunc():
    global x
    x = "kinwi" #now x is globally = "kinwi"
    print("My nickname is " + x)
herFunc()
print("My nickname is " + x)
