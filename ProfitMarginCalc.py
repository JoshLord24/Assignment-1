# This program is a Profit Margin Calculator
def main():
    revenue = float(input("Enter the total revenue: "))
    cost = float(input("Enter the total cost: "))
    if revenue == 0:
        print("Revenue cannot be zero.")
        return
    profit = revenue - cost
    profit_margin = (profit / revenue) * 100
    print(f"The Profit Margin is: {profit_margin:.2f}%")
    print(f"The Total Profit is : ${profit:.2f}")
main()
