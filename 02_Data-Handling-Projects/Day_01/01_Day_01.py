"""
Challenge : CLI Contact Book (CSV Powered)

Create a terminal-based contact book tool that stores and manages 
contacts a using a CSV file.

Your program should :
1. Ask the user to choose one of the following options:
   - Add a new contact.
   - View all contacts.
   - Search for a contact by name
   - Exit
2. Store contacts in a file called 'contacts.csv'  with columns :
   - Name
   - Phone
   - Email
3. If the file doesn't exit, create it automatically.
4. Keep the interface clean and clear.

Example -
Add Contact
View all contacts 
Search contacts
Exit

Bonus :
- Format the contact list in a table-like view 
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv 
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Name"].lower() == name.lower():

               print("Contact name is already exist!")

    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact Added.")

def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No Contacts!")
            return

        print("\nYour Contacts : \n")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

def search_contacts():
    term = input("Enter the name to search : ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | 📞 {row["Phone"]}")
                found = True
    if not found:
        print("No matching contact found!")

def update_contacts():
    name = input("Enter the contact name to update: ").strip()

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)

    found = False

    for contact in contacts:
        if contact["Name"].lower() == name.lower():

            print("Contact found!")

            new_phone = input(
                f"Enter new phone number [{contact['Phone']}]: "
            ).strip()

            new_email = input(
                f"Enter new email [{contact['Email']}]: "
            ).strip()

            if new_phone:
                contact["Phone"] = new_phone

            if new_email:
                contact["Email"] = new_email

            found = True
            break

    if not found:
        print("Contact not found!")
        return

    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Name", "Phone", "Email"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

    print("Contact updated successfully! ✅")

def delete_contacts():
    name = input("Enter the contact name to delete: ").strip()

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)

    new_contacts = []
    found = False

    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            found = True
        else:
            new_contacts.append(contact)

    if not found:
        print("Contact not found!")
        return

    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Name", "Phone", "Email"]

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_contacts)

    print("Contact deleted successfully! 🗑️")


def main():
    while True:
        print("\n 📘 Contact Book.")
        print("\n 1. ✔ Add Contact.")
        print("\n 2. 👀 View All Contact.")
        print("\n 3. 💻 Search Contact.")
        print("\n 4. 💹 Update Contact.")
        print("\n 5. ❌ Delete Contact.")
        print("\n Exit.")

        choice = input("Choose and option (1-4) : ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contacts()
        elif choice == "5":
            delete_contacts()
        elif choice == "6":
            print("Thanks! for using our software...")
            break
        else:
            print("Invalid choice of numbers!")

if __name__ == "__main__":
    main()