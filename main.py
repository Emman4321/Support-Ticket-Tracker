""" By Emmanuel Fatungase
IT System Tracker
05/30/2025

This is a python project that models an IT System Tracker for managing IT support tickets. It allows users to add, view, update, and generate reports on support tickets.
This project uses a CSV file to store ticket data and provides a simple command-line interface for interaction.

    Returns:
    - `add_ticket`: Adds a new support ticket.
    - `view_tickets`: Displays all support tickets.
    - `update_ticket`: Updates the status of an existing support ticket.
    
    """

import csv
import datetime

CSV_FILE = 'tickets.csv'

def load_tickets():
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    
def save_tickets(tickets):
    with open(CSV_FILE, mode='w', newline='') as file:
        fieldnames = ['ID', 'Name', 'Department', 'Issue', 'Status', 'Date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tickets)

def add_ticket():
    tickets = load_tickets()
    ticket_id = len(tickets) + 1
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    issue = input("Describe your issue: ")
    status = 'Open'
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_ticket = {
        'ID': ticket_id,
        'Name': name,
        'Department': department,
        'Issue': issue,
        'Status': status,
        'Date': date
    }
    save_tickets(tickets + [new_ticket])
    print(f"Ticket #{ticket_id} added successfully.")

def view_tickets():
    tickets = load_tickets()
    for ticket in tickets:
        print(ticket)
        
def update_ticket():
    tickets = load_tickets()
    ticket_id = input("Enter the ticket ID to update: ")
    for ticket in tickets:
        if ticket['ID'] == ticket_id:
            print(f"Current status: {ticket['Status']}")
            new_status = input("Enter new status (Open/Closed): ")
            ticket['Status'] = new_status
            save_tickets(tickets)
            print(f"Ticket #{ticket_id} updated successfully.")
            return
    print(f"Ticket #{ticket_id} not found.")
    
    def gen_report():
        tickets = load_tickets()
        status_count = {"Open": 0, "In Progress": 0, "Closed": 0}
        for ticket in tickets:
            status_count[ticket['Status']] += 1
        print("Ticket Status Report:")
        for status, count in status_count.items():
            print(f"{status}: {count}")
        print(f"Total tickets: {len(tickets)}\n")
        
    def main():
        while True:
            print("\n===IT System Support Ticket Tracker===")
            print("1. Add Ticket")
            print("2. View Tickets")
            print("3. Update Ticket")
            print("4. Generate Report")
            print("5. Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                add_ticket()
            elif choice == '2':
                view_tickets()
            elif choice == '3':
                update_ticket()
            elif choice == '4':
                gen_report()
            elif choice == '5':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")
                
    if __name__ == "__main__":
        main()
