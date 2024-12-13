import sqlite3

# Create the Book class
class Book:
    def __init__(self, title, author, ISBN, price):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Price: {self.price}")

# Set up the SQLite database
def setup_database():
    # Connect to SQLite Database (this will create a file named bookstore.db)
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    # Create a table for books if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            ISBN TEXT,
            price REAL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to add a book from user input
def add_book():
    # Prompt the user for book details
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    ISBN = input("Enter ISBN number: ")
    price = float(input("Enter book price: "))

    # Connect to the database
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    # Insert the new book into the database
    cursor.execute('''
        INSERT INTO books (title, author, ISBN, price) VALUES
        (?, ?, ?, ?)
    ''', (title, author, ISBN, price))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Book added successfully!")

# Function to display all books from the database
def display_books_from_db():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    # Retrieve all books from the database
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    # Display the books
    for book in books:
        print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}, Price: {book[3]}")

    # Close the connection
    conn.close()

# Main function to run the program
def main():
    setup_database()  # Set up the database and table

    while True:
        # Ask the user what they want to do
        print("\n1. Add a new book")
        print("2. View all books")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_book()  # Call the function to add a new book
        elif choice == '2':
            display_books_from_db()  # Display all books
        elif choice == '3':
            print("Goodbye!")
            break  # Exit the loop and the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
