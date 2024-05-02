
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
   
        if number > low and number <= high:          
            return number 
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

def calculate_future_value(my_monthly_investment,
                           my_yearly_interest_rate, my_years=20):
    my_monthly_interest_rate = (my_yearly_interest_rate / 100) / 12
    my_months = my_years * 12

    my_future_value = 0
    my_principle = 0
    
    for i in range(my_months):
        my_principle = my_future_value + my_monthly_investment
        my_monthly_interest_amount = my_principle * my_monthly_interest_rate
        my_future_value = my_principle + my_monthly_interest_amount

    return my_future_value

def main():
    programName = "Future Investment Value Calculator"
    print(f"Program: {programName}\n")

    choice = "y"
    while choice.lower() == "y":
    
        monthly_investment = get_float("Enter monthly investment: ", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate: ", 0, 15)
        years = get_int("Enter number of years ", 0, 50)
      
        future_value = calculate_future_value(
            my_years=years, my_monthly_investment=monthly_investment, my_yearly_interest_rate=yearly_interest_rate)

        print("\nThe future value of the total investement:", round(future_value, 2))
        print()

        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
