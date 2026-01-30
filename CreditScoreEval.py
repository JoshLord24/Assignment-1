# This Program is a Credit Score Evaluator
def main():
    print("Welcome to the Credit Score Evaluator!")
    
    score = int(input("Please enter your credit score: "))
    if score <300 or score >850:
        print ("Invalid Credit Score. Score must be between 300 and 850.")
    
    elif score >= 750:
        print("Your credit score is Excellent, Loan Approved! Interest Rate: Low.")
    elif 700 <= score <750:
        print("Your credit score is Good, Loan Approved with Review. Interest Rate: Medium.")
    elif 600 <= score <700:
        print("Your credit score is Fair, Loan Conditionally Approved. ")
    elif score < 600:
        print("Your credit score is Poor, Loan Denied, seek credit improvement.")
main()
