print("JAY SHREE KRISHNA")
print(" ")
import os
from datetime import datetime

JOURNAL_FILE = "journal.txt"

def add_entry():
    entry = input("Enter your journal entry:\n")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(JOURNAL_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n{entry}\n\n")
    print("Entry added successfully!\n")

def view_entries():
    try:
        if not os.path.exists(JOURNAL_FILE):
            print("No journal entries found. Start by adding a new entry!\n")
            return
        with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                print("Your Journal Entries:\n")
                print(content)
            else:
                print("No journal entries found. Start by adding a new entry!\n")
    except FileNotFoundError:
        print("Error: The journal file does not exist. Please add a new entry first.\n")

def search_entry():
    if not os.path.exists(JOURNAL_FILE):
        print("No journal entries found. Start by adding a new entry!\n")
        return
    keyword = input("Enter a keyword or date to search: ").strip()
    found = False
    with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
        entries = file.read().strip().split("\n\n")
        for entry in entries:
            if keyword.lower() in entry.lower():
                if not found:
                    print("Matching Entries:\n")
                    found = True
                print(entry + "\n")
    if not found:
        print(f"No entries were found for the keyword: {keyword}.\n")

def delete_entries():
    if not os.path.exists(JOURNAL_FILE):
        print("No journal entries to delete.\n")
        return
    confirm = input("Are you sure you want to delete all entries? (yes/no): ").lower()
    if confirm == "yes":
        os.remove(JOURNAL_FILE)
        print("All journal entries have been deleted.\n")
    else:
        print("Deletion cancelled.\n")

def main():
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid option. Please select a valid option from the menu.\n")
            continue

        if choice == 1:
            add_entry()
        elif choice == 2:
            view_entries()
        elif choice == 3:
            search_entry()
        elif choice == 4:
            delete_entries()
        elif choice == 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option from the menu.\n")

if __name__ == "__main__":
    main()