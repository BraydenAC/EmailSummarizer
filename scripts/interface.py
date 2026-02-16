
from .host import _AISys
from .logger import logger

class main:
    #Initialize AI system
    host = _AISys()

    user_entry = ""
    while user_entry != "q":
        #Select project option or q to end session
        print("Enter the name used in your emails for your project, or q to quit.")
        logger.info("requesting user entry")
        user_entry = input("Input: ")
        logger.debug(f"User entered '{user_entry}'")

        if user_entry != "q":
            #Send project summary request to AI system
            returned_result = host.RunSummaryTask(user_entry)
            #print returned output
            print(f"Output for {user_entry} is {returned_result}")
    print("quitting...")
