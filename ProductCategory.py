# This Program is a Product Category Matching System
def main():
    product_name = input("Please enter the product name: ").strip().lower()
    if product_name.startswith(("laptop", "pc", "tablet", "gadget", "tech", "phone")):
        category = "Electronics, High Margin"
    elif product_name.startswith(("apparel", "clothing", "shoes", "outfit", "pants", "accessories")):
        category = "Clothing, Medium Margin"
    elif product_name.startswith(("food", "grocery", "snack", "beverage", "drink")):
        category = "Groceries, Low Margin"
    else:
        category = "Miscellaneous, Variable Margin"
    print(f"The product '{product_name.title()}' falls under the category: {category}")
main()