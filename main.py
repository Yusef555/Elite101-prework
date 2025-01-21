print("Welcome to the tech support Chatbot")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")
help = input("How can I help you today?\n Please choose from the following:\n1. Computer issues\n2.Glitchy interaction\n 3.Cannot see your cursor")
conversation = input("Is that all you need help with? If yes type (y). if not, type (n) ")
if conversation == 'n':
    print("Ok, have a good day!")
if conversation == 'y':
    print("Please choose one of the following:\n1. Computer issues\n2.Glitchy interaction\n 3.Cannot see your cursor")
conversation = input("Is that all you need help with? If yes type (y). if not, type (n) ")