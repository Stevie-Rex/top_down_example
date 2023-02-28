# Main function
def main():
    # Get input from user
    principal = get_input("Enter loan amount: ")
    rate = get_input("Enter interest rate: ")
    years = int(get_input("Enter loan term (years): "))

    # Calculate monthly payment
    payment = calculate_payment(principal, rate, years)

    # Display output
    display_output(principal, rate, years, payment)

# Get input function
def get_input(prompt):
    # Write prompt to console
    print(prompt)

    # Read input from console
    userinput = input()

    # Convert input to float
    value = float(userinput)

    # Return value
    return value

# Calculate payment function
def calculate_payment(principal, rate, years):
   # Convert annual rate to monthly rate
   monthly_rate = rate / 12 / 100

   # Convert years to months
   months = years * 12

   # Calculate monthly payment using formula
   payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-months))

   # Return payment
   return payment

# Display output function
def display_output(principal, rate, years, payment):
   # Write output to console using formatting
   print(f"Loan amount: ${principal:.2f}")
   print(f"Interest rate: {rate / 100:.2%}")
   print(f"Loan term: {years} years")
   print(f"Monthly payment: ${payment:.2f}")

main()