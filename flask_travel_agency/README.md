# Cultural Compass Travel Agency

A Flask web application for a youth-focused cultural travel agency that connects to a MySQL database using `mysql.connector`. The application allows users to browse travel packages, explore cultural festivals, book trips, leave comments, and contact the agency -- all through a web browser.

## Project Description

Cultural Compass is a travel agency website designed for young adults (ages 18-30) who are interested in cultural exploration, international festivals, and meaningful travel experiences. The site simplifies travel planning by offering curated packages, festival information, and a community comment section where travelers can connect.

This project was inspired by a real travel experience to South Korea, which showed how transformative cultural travel can be. The goal is to make international travel more accessible and less overwhelming for young travelers.

## How the Application Uses the Database

The Flask application connects to a **MySQL database** using the `mysql.connector` library. Here is how it works:

1. **Connection**: The `get_db_connection()` function in `app.py` creates a connection to the MySQL server using `mysql.connector.connect()` with the host, user, password, and database name.

2. **SQL Queries**: Each Flask route executes SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) through a cursor object. For example, when a user submits a booking form, the application runs an `INSERT INTO bookings` query to save the data.

3. **Retrieving Results**: Query results are fetched using `cursor.fetchall()` or `cursor.fetchone()` with `dictionary=True` so each row is returned as a Python dictionary.

4. **Displaying Data**: The retrieved data is passed to HTML templates using `render_template()`, where Jinja2 template syntax displays the information on the web page.

5. **User Input**: HTML forms collect user input (names, emails, dates, etc.), which is sent to Flask routes via POST requests. The form data is accessed using `request.form[]` and safely inserted into the database using parameterized queries (`%s` placeholders) to prevent SQL injection.

## Database Structure

The database `travel_agency` contains **4 tables**:

### `packages` - Travel Packages
| Column      | Type           | Description                    |
|-------------|----------------|--------------------------------|
| id          | INT (PK, AUTO) | Unique package identifier      |
| title       | VARCHAR(200)   | Package name                   |
| destination | VARCHAR(200)   | Travel destination             |
| description | TEXT           | Detailed description           |
| duration    | VARCHAR(50)    | Trip duration                  |
| price       | DECIMAL(10,2)  | Price per person               |
| image_url   | VARCHAR(500)   | URL for the package image      |
| created_at  | TIMESTAMP      | When the record was created    |

### `bookings` - Booking Requests
| Column        | Type           | Description                   |
|---------------|----------------|-------------------------------|
| id            | INT (PK, AUTO) | Unique booking identifier     |
| package_id    | INT (FK)       | References packages(id)       |
| name          | VARCHAR(200)   | Traveler's full name          |
| email         | VARCHAR(200)   | Traveler's email              |
| travel_date   | DATE           | Preferred travel date         |
| num_travelers | INT            | Number of travelers           |
| created_at    | TIMESTAMP      | When the booking was submitted|

### `comments` - User Comments
| Column     | Type           | Description                    |
|------------|----------------|--------------------------------|
| id         | INT (PK, AUTO) | Unique comment identifier      |
| package_id | INT (FK)       | References packages(id)        |
| username   | VARCHAR(100)   | Commenter's display name       |
| message    | TEXT           | Comment text                   |
| created_at | TIMESTAMP      | When the comment was posted    |

### `contacts` - Contact Form Messages
| Column   | Type           | Description                      |
|----------|----------------|----------------------------------|
| id       | INT (PK, AUTO) | Unique message identifier        |
| name     | VARCHAR(200)   | Sender's name                    |
| email    | VARCHAR(200)   | Sender's email                   |
| subject  | VARCHAR(300)   | Message subject                  |
| message  | TEXT           | Message content                  |
| created_at| TIMESTAMP     | When the message was sent        |

## Features (CRUD Operations)

| Operation  | What It Does                                                |
|------------|-------------------------------------------------------------|
| **Create** | Add new travel packages, submit bookings, post comments, send contact messages |
| **Read**   | View all packages, view package details, view bookings, view comments |
| **Update** | Edit existing travel packages (title, description, price, etc.)  |
| **Delete** | Delete packages, delete bookings, delete comments           |
| **Search** | Search packages by destination, title, or keyword           |

## Pages

| Page             | URL                    | Description                                    |
|------------------|------------------------|------------------------------------------------|
| Home             | `/`                    | Welcome page with featured packages            |
| All Packages     | `/packages`            | Browse all travel packages                     |
| Package Details  | `/packages/<id>`       | View package info and comments                 |
| Add Package      | `/packages/add`        | Form to add a new package                      |
| Edit Package     | `/packages/edit/<id>`  | Form to update a package                       |
| Search           | `/packages/search?q=`  | Search packages by keyword                     |
| Book a Trip      | `/book/<id>`           | Booking form for a specific package            |
| View Bookings    | `/bookings`            | View all booking requests                      |
| Festivals        | `/festivals`           | Learn about cultural festivals worldwide       |
| Contact          | `/contact`             | Send a message to the agency                   |

## How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Set Up MySQL Database

Make sure MySQL is running, then execute the SQL file:

```bash
mysql -u root -p < database.sql
```

Or open MySQL Workbench, paste the contents of `database.sql`, and execute it.

### 3. Configure Database Connection

Open `app.py` and update the database connection settings if needed:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",       # Change to your MySQL password
    database="travel_agency"
)
```

### 4. Run the Application

```bash
python app.py
```

Then open your browser and go to: **http://127.0.0.1:5000**

## Technologies Used

- **Python** - Backend programming language
- **Flask** - Web framework for Python
- **MySQL** - Relational database management system
- **mysql.connector** - Python library to connect Flask with MySQL
- **HTML5** - Page structure and templates (Jinja2)
- **CSS3** - Custom styling
- **Bootstrap 5** - Responsive design framework
- **Bootstrap Icons** - Icon library

## Project Files

```
flask_travel_agency/
├── app.py                  # Main Flask application
├── database.sql            # SQL file to create database and tables
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── static/
│   └── css/
│       └── style.css       # Custom CSS styles
└── templates/
    ├── base.html           # Base template with navigation and footer
    ├── home.html           # Home page
    ├── packages.html       # All packages page
    ├── package_detail.html # Single package with comments
    ├── add_package.html    # Add new package form
    ├── edit_package.html   # Edit package form
    ├── search.html         # Search results page
    ├── book.html           # Booking form
    ├── bookings.html       # View all bookings
    ├── festivals.html      # Cultural festivals page
    └── contact.html        # Contact form
```
