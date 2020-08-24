def interface():
    print("My Program")
    while True:
        print("Options for you:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
            
def HDL_driver():
    print("HDL Interface")
    #get input
    x = get_input()
    #check if HDL is normal
    check_HDL(x)
    #output
    
def get_input():
    x = input("Enter HDL number: ")
    x = int(x)
    return x
    
def check_HDL(x):
    if x>= 60:
        return "HDL is normal."
    elif 40<=x<60:
        return "HDL is borderline low."
    elif x<40:
        return "HDL is low."
    else:
        return "Error please try again."
interface()
