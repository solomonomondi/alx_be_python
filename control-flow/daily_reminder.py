
def daily_reminder():
    print("=== Daily Task Reminder ===")
    
    # Get user input
    task = input("Enter your task: ")
    
    # Validate priority input using a loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter only 'high', 'medium', or 'low'")
    
    # Validate time-bound input using a loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter only 'yes' or 'no'")
    
    # Process using Match Case for priority
    match priority:
        case 'high':
            urgency = "urgent"
        case 'medium':
            urgency = "important"
        case 'low':
            urgency = "optional"
    
    # Add time sensitivity using conditional statements
    if time_bound == 'yes':
        time_message = "that requires immediate attention today!"
    else:
        time_message = "to be completed when possible."
    
    # Generate and display customized reminder
    print(f"\nReminder: '{task}' is a {priority} priority task {time_message}")
    
    # Additional loop for emphasis based on priority
    if priority == 'high':
        print("\n" + "!" * 50)
        print("CRITICAL REMINDER - DO NOT FORGET!")
        print("!" * 50)

# Run the reminder function
if __name__ == "__main__":
    daily_reminder()