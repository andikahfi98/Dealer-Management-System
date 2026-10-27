# Dealer Management System

**A Python-based CRUD application with SQLite database integration.**

## 1. Project Overview

Dealer Management System is a command-line application developed using Python and SQLite to manage dealer information through basic Create, Read, Update, and Delete (CRUD) operations.

This project was built as part of a hands-on Python learning journey, starting with fundamental programming concepts and gradually progressing toward database integration.

The primary objective is to strengthen Python programming skills, understand database interactions, and implement a simple but functional data management application.

## 2. Key Features

| Feature | Description |
|---|---|
| Create Dealer | Add a new dealer with a unique ID, name, and city |
| List Dealers | Retrieve and display all registered dealers |
| Search Dealer | Search for a specific dealer using its ID |
| Update Dealer | Modify an existing dealer's name and city |
| Delete Dealer | Remove a dealer using its ID |
| Input Validation | Handle non-numeric dealer IDs |
| Duplicate Prevention | Prevent duplicate primary keys |
| Persistent Storage | Store and retrieve dealer records using SQLite |
| Error Handling | Handle database integrity errors and invalid inputs |

## 3. Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and CRUD functions |
| SQLite | Relational database management |
| sqlite3 | Python database connectivity |
| JSON | File-based persistence during initial development |
| SQL | Data manipulation and retrieval |
| VS Code | Development environment |
| Git & GitHub | Version control and project documentation |

The application uses Python's built-in libraries and does not require additional third-party packages.

## 4. Database Structure

The SQLite database contains a `dealers` table with the following schema:

| Column | Data Type | Constraint | Description |
|---|---|---|---|
| id | INTEGER | PRIMARY KEY | Unique dealer identifier |
| name | TEXT | NOT NULL | Dealer name |
| city | TEXT | NOT NULL | Dealer location |

**Table creation:**

```sql
CREATE TABLE IF NOT EXISTS dealers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);
```

The `id` column serves as the primary key to prevent duplicate dealer identifiers.

## 5. Application Workflow

The application uses a terminal-based menu to execute database operations.

```text
             START APPLICATION
                     |
                     v
           DEALER MANAGEMENT MENU
                     |
       +-------------+-------------+
       |             |             |
       v             v             v
    CREATE         READ          UPDATE
       |             |             |
       +-------------+-------------+
                     |
                     v
              SQLite Database
                     |
                     v
              Commit / Retrieve
                     |
                     v
              Return to Menu
```

The Delete operation also uses the same database connection pattern, removing a record based on its unique ID.

Each database operation is implemented through a dedicated Python function.

## 6. Project Structure

```text
Dealer-Management-System/
|
|-- dealer_management_sqlite.py
|-- dealer_management.py
|-- database_setup.py
|-- README.md
|-- .gitignore
|
|-- practice/
|   |-- insert_dealer.py
|   |-- search_dealer.py
|   |-- update_dealer.py
|   |-- delete_dealer.py
|   |-- cleanup_dummy.py
|
|-- dealers.db         (generated locally)
```

**File descriptions**

- `dealer_management_sqlite.py` — Main application integrating CRUD operations with SQLite.
- `dealer_management.py` — Earlier implementation using Python lists and JSON storage.
- `database_setup.py` — Creates the SQLite database table.
- `practice/` — Individual scripts used to learn and implement database operations.
- `.gitignore` — Excludes local database files, JSON data, and Python cache files from Git tracking.

The `dealers.db` file is generated locally and is not included in the repository.

## 7. Getting Started

### Prerequisites

- Python 3.10 or newer
- VS Code or another Python-compatible editor
- Git (optional)

### Step 1 — Clone the repository

Clone the repository using its GitHub URL, then navigate to the project directory.

### Step 2 — Initialize the database

Run:

```bash
python database_setup.py
```

This creates the `dealers.db` database and the `dealers` table if they do not already exist.

A new database starts with an empty dealer table.

### Step 3 — Run the application

```bash
python dealer_management_sqlite.py
```

The application displays an interactive menu:

```text
=== DEALER MANAGEMENT SYSTEM ===

1. List Dealers
2. Create Dealer
3. Search Dealer
4. Update Dealer
5. Delete Dealer
6. Exit

Enter your choice:
```

### Step 4 — Manage dealer data

Select an operation and follow the terminal prompts.

**Example: Create a dealer**

```text
Enter your choice: 2

Enter Dealer ID: 101
Enter Dealer Name: Kirana Cellular
Enter Dealer City: Serang

Dealer created successfully.
```

**Example: Search a dealer**

```text
Enter your choice: 3

Enter Dealer ID: 101

ID: 101, Name: Kirana Cellular, City: Serang
```

The example records are illustrative; actual output depends on the database contents.

## 8. Implementation Details

### Database Connectivity

Database operations use Python's built-in `sqlite3` module.

```python
conn = sqlite3.connect("dealers.db")
cursor = conn.cursor()
```

### Parameterized Queries

SQL statements use placeholders to separate user input from SQL instructions.

```python
cursor.execute(
    "SELECT * FROM dealers WHERE id = ?",
    (dealer_id,)
)
```

This approach helps prevent SQL injection and avoids manual SQL string formatting.

### Transaction Management

Changes made through INSERT, UPDATE, and DELETE operations are committed to the database using `conn.commit()`.

Database connections are closed when operations finish.

### Error Handling

The application implements basic exception handling for situations including:

- Duplicate dealer IDs
- Invalid numeric input
- Database integrity errors
- Dealer IDs that do not exist

For UPDATE and DELETE operations, `cursor.rowcount` is used to determine whether records were affected.

## 9. Development Journey

This project was developed incrementally to reinforce Python concepts through practical implementation.

| Phase | Implementation | Key Learning |
|---|---|---|
| 1 | Python Fundamentals | Variables, conditions, loops, and functions |
| 2 | In-Memory CRUD | Lists, dictionaries, and data manipulation |
| 3 | Exception Handling | Input validation and error management |
| 4 | JSON Storage | File handling, serialization, and persistence |
| 5 | SQLite Integration | Database connections and SQL queries |
| 6 | Interactive CRUD | Integrating application logic with database operations |

The initial version used a List of Dictionaries to store dealer information. JSON was introduced to preserve data across application restarts.

The final implementation moved to SQLite, allowing the application to manage structured data using SQL queries rather than relying on in-memory collections.

## 10. Key Learnings

Building this project helped reinforce several core programming concepts:

- Structuring reusable Python functions.
- Understanding mutable objects, return values, and control flow.
- Implementing CRUD operations using SQL.
- Managing database connections and transactions.
- Handling invalid inputs and database constraints.
- Understanding the difference between file-based and database-based persistence.
- Organizing a Python project into reusable components.

One important takeaway was understanding how data retrieved from SQLite differs from in-memory Python objects, and why SQL operations are required to persist database changes.

## 11. Current Limitations

This project is a learning-oriented command-line application rather than a production-ready system.

Current limitations include:

- Basic input validation; blank dealer names and cities are not yet rejected.
- No graphical user interface or user authentication.
- Database connections are managed independently by each CRUD function.
- No automated test suite.

These limitations provide opportunities for future improvements in application architecture, validation, and testing.

---

## Project Summary

Dealer Management System demonstrates the progression from fundamental Python programming to a functional SQLite-backed CRUD application.

The project emphasizes practical understanding of programming logic, database interactions, data persistence, and error handling.

**Project Type:** Python Learning & Backend Fundamentals

**Implementation:** Python, SQLite, SQL

**Interface:** Command-Line Application