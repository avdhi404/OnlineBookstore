# Online Bookstore

An Online Bookstore project built with Python, leveraging SQLite for database management. This project allows users to add, store, and display book information dynamically.

## Features

- Add new books with details like title, author, ISBN, and price.
- Store book information in a SQLite database.
- Retrieve and display all stored books.
- Simple command-line interface for user interaction.

## Project Structure

```
OnlineBookstore/
├── bookstore.py       # Main Python script
├── bookstore.db       # SQLite database file (created automatically)
├── README.md          # Project documentation
```

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python and SQLite.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/avdhi404/OnlineBookstore.git
   cd OnlineBookstore
   ```

2. Ensure Python is installed by running:
   ```bash
   python3 --version
   ```

3. Install any necessary Python libraries (if required):
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: This project uses built-in Python libraries, so no additional installations may be necessary.)*

## Usage

1. Run the script:
   ```bash
   python3 bookstore.py
   ```

2. Follow the prompts to:
   - Add a new book.
   - View all books in the database.

## Example

Here’s an example of how the program works:

```bash
$ python3 bookstore.py
Enter book title: The Python Handbook
Enter author name: Jane Doe
Enter ISBN number: 987654321
Enter book price: 15.99

Title: The Python Handbook
Author: Jane Doe
ISBN: 987654321
Price: 15.99
```

## Technologies Used

- **Python**: Core programming language.
- **SQLite**: Lightweight, file-based database for storing book information.

## Contributing

Contributions are welcome! If you have ideas or improvements, feel free to fork this repository and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[avdhi404](https://github.com/avdhi404)