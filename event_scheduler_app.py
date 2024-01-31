import unittest

# Global list to store events
events = []

# Function to add an event
def add_event(name, date, time):
    event = {'name': name, 'date': date, 'time': time}
    events.append(event)
    print("Event added successfully!")

# Function to view all events
def view_events():
    if not events:
        print("No events found.")
    else:
        print("Events:")
        for event in events:
            print(f"Name: {event['name']}, Date: {event['date']}, Time: {event['time']}")

# Function to delete an event
def delete_event(name):
    for event in events:
        if event['name'] == name:
            events.remove(event)
            print("Event deleted successfully!")
            return
    print("Event not found.")

# Function to search for events
def search_event(search_query):
    results = []
    for event in events:
        if search_query in event['name'] or search_query in event['date']:
            results.append(event)
    if results:
        print("Search Results:")
        for result in results:
            print(f"Name: {result['name']}, Date: {result['date']}, Time: {result['time']}")
    else:
        print("No events found matching the search criteria.")

# Function to edit an event
def edit_event(name, new_date, new_time):
    for event in events:
        if event['name'] == name:
            event['date'] = new_date
            event['time'] = new_time
            print("Event updated successfully!")
            return
    print("Event not found.")

# Main function
def main():
    while True:
        print("\nEvent Scheduler")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Search Event")
        print("5. Edit Event")
        print("6. Exit")
        choice = input("Enter your choice:\n")
        if choice == '1':
            name = input("Enter event name: \n")
            date = input("Enter event date (YYYY-MM-DD): \n")
            time = input("Enter event time (HH:MM AM/PM):\n ")
            add_event(name, date, time)
        elif choice == '2':
            view_events()
        elif choice == '3':
            name = input("Enter event name to delete:\n ")
            delete_event(name)
        elif choice == '4':
            search_query = input("Enter search query:\n ")
            search_event(search_query)
        elif choice == '5':
            name = input("Enter event name to edit:\n ")
            new_date = input("Enter new date (YYYY-MM-DD):\n ")
            new_time = input("Enter new time (HH:MM AM/PM):\n ")
            edit_event(name, new_date, new_time)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Unit tests for the event scheduler
class TestEventScheduler(unittest.TestCase):
    def test_add_event(self):
        add_event("Meeting", "2022-12-31", "18:00")
        self.assertEqual(events[0]['name'], "Meeting")

def test_delete_event(self):
        add_event("Meeting", "2022-12-31", "18:00")
        delete_event("Meeting")
        self.assertEqual(len(events), 0)

# Run the unit tests
if __name__ == '__main__':
    unittest.main()