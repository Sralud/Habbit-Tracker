import datetime

habits = {}

def add_habit():
    habit_name = input("Enter the name of the habit to track: ").strip()
    if habit_name in habits:
        print(f"The habit '{habit_name}' already exists.")
    else:
        habits[habit_name] = {"streak": 0, "last_updated": None, "total_days": 0}
        print(f"Habit '{habit_name}' added!")

def mark_progress():
    habit_name = input("Enter the name of the habit to mark as done: ").strip()
    if habit_name not in habits:
        print(f"The habit '{habit_name}' does not exist.")
        return

    today = datetime.date.today()
    last_updated = habits[habit_name]["last_updated"]

    if last_updated == today:
        print(f"You already marked progress for '{habit_name}' today!")
    else:
        if last_updated == today - datetime.timedelta(days=1):
            habits[habit_name]["streak"] += 1
        else:
            habits[habit_name]["streak"] = 1

        habits[habit_name]["last_updated"] = today
        habits[habit_name]["total_days"] += 1
        print(f"Progress marked for '{habit_name}'. Current streak: {habits[habit_name]['streak']}")

def show_summary():
    if not habits:
        print("No habits to track yet. Add some habits first!")
    else:
        print("\nHabit Tracker Summary:")
        for habit_name, details in habits.items():
            print(f"- {habit_name}:")
            print(f"  Current Streak: {details['streak']} days")
            print(f"  Total Days Completed: {details['total_days']} days")
            print(f"  Last Updated: {details['last_updated'] or 'Never'}")
        print()

def habit_tracker():
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add a new habit")
        print("2. Mark progress for a habit")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_habit()
        elif choice == "2":
            mark_progress()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye! Keep up the good habits!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    habit_tracker()