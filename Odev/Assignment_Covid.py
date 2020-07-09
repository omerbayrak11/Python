Age = input("Are you a cigarette addict older than 75 years old? (YES OR NO): ").title().strip() == "Yes"
chronic = input("Do you have a severe chronic disease? (YES OR NO): ").title().strip() == "Yes"
immune = input("Is your immune system too weak? (YES OR NO): ").title().strip() == "Yes"
risk = Age or chronic or immune
if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")
