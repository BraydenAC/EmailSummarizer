
from .host import _AISys
# from .logger import something

class main:
    #Initialize AI system
    host = _AISys()

    user_entry = ""
    while user_entry != "q":
        #Select project option or q to end session
        print("Enter the name used in your emails for your project, or q to quit.")
        user_entry = input("Input: ")

        if user_entry != "q":
            #Send project summary request to AI system
            #print returned output
            print("Non-exit sequence entered!")
    print("quitting...")
