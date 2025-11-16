# This script converts a given number of hours into seconds.

# Define the variable for the number of hours
hours = 2

# Define the conversion factor (60 minutes/hour * 60 seconds/minute)
SECONDS_PER_HOUR = 3600

# Calculate the number of seconds
seconds = hours * SECONDS_PER_HOUR

# Print the result in the format: [hours] hour(s) is [seconds] seconds.
print(f"{hours} hour(s) is {seconds} seconds.")
