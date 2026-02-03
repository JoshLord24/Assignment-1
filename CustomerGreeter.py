# This Program is a Customer Greeting Program
def customer_greeter(name: str = ""):
    name = input("Hello! Please enter your name: ")
    cleaned_name = name.strip().title().split()[0]
    print(f"Welcome, {cleaned_name}!")
    if cleaned_name == "":
        print("Hello Valued Customer!")
customer_greeter("")
