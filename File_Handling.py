# File Handling Mini Project - Contact Management System
# CodeOrbit Tech - Python Programming Internship

import csv
import os

FILE_NAME = "contacts.csv"


# Function to create the CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])


# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("Contact added successfully!")


# Function to view all contacts
def view_contacts():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No contacts available.")
                return

            print("\n===== CONTACT LIST =====")

            for row in rows[1:]:
                print("Name:", row[0])
                print("Phone:", row[1])
                print("Email:", row[2])
                print("------------------------")

    except FileNotFoundError:
        print("Error: Contact file not found.")


# Function to search for a contact
def search_contact():
    search_name = input("Enter name to search: ").lower()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            found = False

            for contact in reader:
                if contact["Name"].lower() == search_name:
                    print("\nContact found!")
                    print("Name:", contact["Name"])
                    print("Phone:", contact["Phone"])
                    print("Email:", contact["Email"])
                    found = True

            if not found:
                print("Contact not found.")

    except FileNotFoundError:
        print("Error: Contact file not found.")


# Main program
create_file()

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice. Please select 1 to 4.")