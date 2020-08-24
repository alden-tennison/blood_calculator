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
    #check if HDL is normal
    #output
    
def get_input():
    x = input("Enter HDL number: ")
    x = int(x)
    return x
interface()
