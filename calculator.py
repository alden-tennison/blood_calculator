def interface():
    print("My Program")
    while True:
        print("Options for you:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
        elif choice=='2':
            LDL_driver()
            
def HDL_driver():
    print("HDL Interface")
    #get input
    x = get_input()
    #check if HDL is normal
    x = check_HDL(x)
    #output
    output_HDL(x)

def LDL_driver():
    print("LDL Interface")
    #get input
    x = get_input()
    #check if HDL is normal
    x = check_LDL(x)
    #output
    output_LDL(x)

def get_input():
    x = input("Enter HDL/LDL number: ")
    x = int(x)
    return x
    
def check_HDL(x):
    if x>= 60:
        return "normal."
    elif 40<=x<60:
        return "borderline low."
    elif x<40:
        return "low."
    else:
        return "Error please try again."

def check_LDL(x):
    if x < 130:
        return "normal."
    else:
        return "Error please try again."
def output_HDL(x):
    print("The HDL result is {}".format(x))
def output_LDL(x):
    print("The LDL result is {}".format(x))
if __name__ == '__main__':
    interface()
