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
    
    # Generate customized reminder based on priority and time sensitivity
    if time_bound == 'yes':
        # Use Match Case for priority levels
        match priority:
            case 'high':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            case 'medium':
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            case 'low':
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        # Use Match Case for priority levels (not time-bound)
        match priority:
            case 'high':
                print(f"Reminder: '{task}' is a high priority task")
            case 'medium':
                print(f"Reminder: '{task}' is a medium priority task")
            case 'low':
                print(f"Reminder: '{task}' is a low priority task")

# Run the reminder function
if __name__ == "__main__":
    daily_reminder()