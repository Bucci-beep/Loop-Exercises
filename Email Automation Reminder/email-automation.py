# Define a list of users

users = [
    {
        "name": "Alice",
        "email": "alice@example.com",
        "tasks": ["Submit monthly report", "Schedule team meeting"]
    },
    {
        "name": "Bob",
        "email": "bob@example.com",
        "tasks": ["Update project status", "Review budget"]
    },
    {
        "name": "Bucci",
        "email": "bucci@example.com",
        "tasks": ["Edit videos for social media", "Upload TikTok content"]
    }
]

# Create a function to send the email
def send_email(user):
    # Create the email subject and message
    subject = "Monthly reminder: Your tasks and goals"
    message = f"Hello {user['name']},\n\nHere are your tasks for this month:\n"

    #Append each task to the message
    for task in user["tasks"]:
        message += f" - {task}\n"

    message += "\nBest regards, \nYour reminder service"

    #Simulate sending email by printing the message
    print(f"Sending email to {user['email']}")
    print("Subject:", subject)
    print("Message:")
    print(message)
    print("-" *40)

# Loop through the list of users and send each one an email reminder
for user in users:
    send_email(user)