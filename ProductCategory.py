# This Program is a Product Category Matching System
def main():
    product_name = input("Please enter the product name: ").strip().lower()
    
    match product_name:
        case "laptop" | "smartphone" | "tablet" | "camera" | "tech":
            category = "Electronics, High Margin"
        case "t-shirt" | "jeans" | "shoes" | "jacket" | "accessories":
            category = "Clothing, Medium Margin"
        case "snack" | "drink" | "grocery" | "fruit" | "vegetable":
            category = "Groceries, Low Margin"
        case _:
            category = "Miscellaneous, Variable Margin"
    
    print(f"The product '{product_name.title()}' falls under the category: {category}")
main()