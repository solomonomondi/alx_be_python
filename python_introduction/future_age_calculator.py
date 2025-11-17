# This script prompts the user for their current age and calculates how old
# they will be in the year 2050 (assuming the current year is 2023, requiring
# an addition of 27 years).

# 1. Prompt the user for their current age and capture the input.
# The input() function returns a string, so we must wrap it in int() for arithmetic.
current_age_str = input("How old are you? ")
current_age = int(current_age_str)

# 2. Define the number of years to add (2050 - 2023 = 27)
YEARS_TO_FUTURE = 27

# 3. Calculate the age in 2050
future_age = current_age + YEARS_TO_FUTURE

# 4. Print the result in the specified format
print(f"In 2050, you will be {future_age} years old.")