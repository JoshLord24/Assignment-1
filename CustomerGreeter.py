# This Program is a Customer Greeting Program
def customer_greeter(name: str = ""):
# This Function Greets the Customer and prompts them to input their name. It then cleans the name, makes it a title, and strips whitespaces
    name = input("Hello! Please enter your name: ")
# This function prints a message if no name is inputted
    if name == "":
        print("Welcome, Valued Customer!")
        return
    cleaned_name = name.strip().title().split()[0]
# This function prints out the Cleaned Name and welcomes the customer
    print(f"Welcome, {cleaned_name}!")
customer_greeter("")
