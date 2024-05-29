'''
Simple Interest Calculator with random intervals...(maybe prone to error)

Final Balance = Calculated Interest + Principal

Calculated Interest = Principal * Interest (in years) * Term (in years)

'''
def new_line():
    return print("\n")

def user_input():
    principal_amount_input = float(input("Please enter your PRINCIPAL AMOUNT : $"))
    new_line()
    interest_amount_input = float(input("Please enter your INTEREST AMOUNT in (%): "))
    interest_term_input = (input("Please the TIMED INTERVAL (days/weeks/months/years) : "))
    new_line()
    term_amount_input = int(input("Please enter how long this term is for : "))
    term_term_input = (input("Please the TIMED INTERVAL (days/weeks/months/years) : "))
    new_line()

    calculation(principal = principal_amount_input, interest = interest_amount_input,
                interest_term = interest_term_input, term = term_amount_input,
                term_term = term_term_input)

def calculation(principal, interest, interest_term, term, term_term):

    interest_term = interest_term.lower()
    term_term = term_term.lower()

    if (interest_term == "year") or (interest_term == "years") or (interest_term == "y"):
        pass
    elif (interest_term == "month") or (interest_term == "months") or (interest_term == "m"):
        interest = (interest * 365) / 100
    elif (interest_term == "week") or (interest_term == "weeks") or (interest_term == "w"):
        interest = (interest * 365) / 100
    elif (interest_term == "day") or (interest_term == "days") or (interest_term == "d"):
        interest = (interest * 365) / 100
    else:
        print("Non-valid Entry! INTEREST is set to a -YEAR-")

    if (term_term == "year") or (term_term == "years") or (term_term == "y"):
        pass
    elif (term_term == "month") or (term_term == "months") or (term_term == "m"):
        term = term / 365
    elif (term_term == "week") or (term_term == "weeks") or (term_term == "w"):
        term = term / 365
    elif (term_term == "day") or (term_term == "days") or (term_term == "d"):
        term = term / 365
    else:
        term = 1
        print("Non-valid Entry! TERM is set to a -YEAR-")

    final_calculation(principal=principal, interest=interest, term=term)

def final_calculation(principal, interest, term):

    final_amount = (principal * interest * term) + principal
    final_amount = round(final_amount, 2)
    print(f"The Final Balance for this calculator is --- ${final_amount} ---")
    new_line()
    save_score(score = final_amount)

def save_score(score):
    score_list = []
    user_score = input("Would like to save this score? (Y/N) : ")
    if (user_score.lower() == "y")or (user_score.lower() == "yes"):
        score_list.append(score)
    else:
        new_line()
        restart_program()

def restart_program():
    user_restart = input("Would you like to calculate again? (Y/N) : ")
    if (user_restart.lower() == "y") or (user_restart.lower() == "yes"):
        main()
    else:
        new_line()
        print("Thanks for using this program.")
        new_line()

def main():
    print("This is a Simple Interest Calculator.")
    new_line()
    user_input()

if __name__== "__main__":
    main()