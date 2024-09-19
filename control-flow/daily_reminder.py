# daily_reminder.py

def main():
    # Prompt user for task description
    task = input("Enter your task: ")
    
    # Prompt user for task priority
    priority = input("Priority (high/medium/low): ").lower()
    
    # Prompt user if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Determine reminder message based on priority and time sensitivity
    match priority:
        case 'high':
            priority_message = "a high priority task"
        case 'medium':
            priority_message = "a medium priority task"
        case 'low':
            priority_message = "a low priority task"
        case _:
            priority_message = "an unknown priority task"
    
    if time_bound == 'yes':
        # Ensure the print statement matches the required format
        print(f"Reminder: '{task}' is {priority_message} that requires immediate attention today!")
    else:
        # Ensure the print statement matches the required format
        print(f"Note: '{task}' is {priority_message}. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()