# This program is a tax bracket determiner
def main():
        income = float(input("Please enter your annual income: "))
        if income < 50000:
            print("Low Bracket (10%). Estimated tax: $", income * 0.10)
        elif 50000 <= income < 100000:
            print("Medium Bracket (20%). Estimated tax: $", income * 0.20)
        else:
            print("High Bracket (30%). Estimated tax: $", income * 0.30)
        if income < 0:
            print("Invalid income. Please enter a non-negative value.")
main()
