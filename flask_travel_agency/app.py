"""
Cultural Compass Travel Agency - Flask Application
A web application for a youth-focused cultural travel agency
that connects to a MySQL database using mysql.connector.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "cultural_compass_secret_key"

# ============================================================
# Database Connection
# ============================================================

def get_db_connection():
    """Create and return a connection to the MySQL database."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="travel_agency"
    )
    return conn


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    """Display the home page with featured packages."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM packages ORDER BY created_at DESC LIMIT 3")
    featured = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("home.html", featured=featured)


# ============================================================
# PACKAGES - View All, View One, Add, Edit, Delete, Search
# ============================================================

@app.route("/packages")
def packages():
    """Display all travel packages."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM packages ORDER BY created_at DESC")
    all_packages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("packages.html", packages=all_packages)


@app.route("/packages/<int:package_id>")
def package_detail(package_id):
    """Display a single package with its comments."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM packages WHERE id = %s", (package_id,))
    package = cursor.fetchone()

    if not package:
        flash("Package not found.", "error")
        cursor.close()
        conn.close()
        return redirect(url_for("packages"))

    cursor.execute(
        "SELECT * FROM comments WHERE package_id = %s ORDER BY created_at DESC",
        (package_id,),
    )
    comments = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template("package_detail.html", package=package, comments=comments)


@app.route("/packages/add", methods=["GET", "POST"])
def add_package():
    """Form to add a new travel package."""
    if request.method == "POST":
        title = request.form["title"]
        destination = request.form["destination"]
        description = request.form["description"]
        duration = request.form["duration"]
        price = request.form["price"]
        image_url = request.form["image_url"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO packages (title, destination, description, duration, price, image_url) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (title, destination, description, duration, price, image_url),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Travel package added successfully!", "success")
        return redirect(url_for("packages"))

    return render_template("add_package.html")


@app.route("/packages/edit/<int:package_id>", methods=["GET", "POST"])
def edit_package(package_id):
    """Form to edit an existing travel package."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        title = request.form["title"]
        destination = request.form["destination"]
        description = request.form["description"]
        duration = request.form["duration"]
        price = request.form["price"]
        image_url = request.form["image_url"]

        cursor.execute(
            "UPDATE packages SET title=%s, destination=%s, description=%s, "
            "duration=%s, price=%s, image_url=%s WHERE id=%s",
            (title, destination, description, duration, price, image_url, package_id),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Package updated successfully!", "success")
        return redirect(url_for("package_detail", package_id=package_id))

    cursor.execute("SELECT * FROM packages WHERE id = %s", (package_id,))
    package = cursor.fetchone()
    cursor.close()
    conn.close()

    if not package:
        flash("Package not found.", "error")
        return redirect(url_for("packages"))

    return render_template("edit_package.html", package=package)


@app.route("/packages/delete/<int:package_id>", methods=["POST"])
def delete_package(package_id):
    """Delete a travel package."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM packages WHERE id = %s", (package_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Package deleted successfully.", "success")
    return redirect(url_for("packages"))


@app.route("/packages/search")
def search_packages():
    """Search packages by destination or title."""
    query = request.args.get("q", "")
    results = []

    if query:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        search_term = f"%{query}%"
        cursor.execute(
            "SELECT * FROM packages WHERE title LIKE %s OR destination LIKE %s "
            "OR description LIKE %s ORDER BY created_at DESC",
            (search_term, search_term, search_term),
        )
        results = cursor.fetchall()
        cursor.close()
        conn.close()

    return render_template("search.html", results=results, query=query)


# ============================================================
# COMMENTS - Add and Delete
# ============================================================

@app.route("/comments/add", methods=["POST"])
def add_comment():
    """Add a comment to a travel package."""
    package_id = request.form["package_id"]
    username = request.form["username"]
    message = request.form["message"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comments (package_id, username, message) VALUES (%s, %s, %s)",
        (package_id, username, message),
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash("Comment posted!", "success")
    return redirect(url_for("package_detail", package_id=package_id))


@app.route("/comments/delete/<int:comment_id>", methods=["POST"])
def delete_comment(comment_id):
    """Delete a comment."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT package_id FROM comments WHERE id = %s", (comment_id,))
    comment = cursor.fetchone()
    package_id = comment["package_id"] if comment else None

    cursor.execute("DELETE FROM comments WHERE id = %s", (comment_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Comment deleted.", "success")
    if package_id:
        return redirect(url_for("package_detail", package_id=package_id))
    return redirect(url_for("packages"))


# ============================================================
# BOOKINGS - Book, View All, Delete
# ============================================================

@app.route("/book/<int:package_id>", methods=["GET", "POST"])
def book_package(package_id):
    """Form to book a travel package."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        travel_date = request.form["travel_date"]
        num_travelers = request.form["num_travelers"]

        cursor.execute(
            "INSERT INTO bookings (package_id, name, email, travel_date, num_travelers) "
            "VALUES (%s, %s, %s, %s, %s)",
            (package_id, name, email, travel_date, num_travelers),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Booking request submitted successfully!", "success")
        return redirect(url_for("bookings"))

    cursor.execute("SELECT * FROM packages WHERE id = %s", (package_id,))
    package = cursor.fetchone()
    cursor.close()
    conn.close()

    if not package:
        flash("Package not found.", "error")
        return redirect(url_for("packages"))

    return render_template("book.html", package=package)


@app.route("/bookings")
def bookings():
    """View all booking requests."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT b.*, p.title AS package_title, p.destination "
        "FROM bookings b LEFT JOIN packages p ON b.package_id = p.id "
        "ORDER BY b.created_at DESC"
    )
    all_bookings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("bookings.html", bookings=all_bookings)


@app.route("/bookings/delete/<int:booking_id>", methods=["POST"])
def delete_booking(booking_id):
    """Delete a booking request."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Booking deleted.", "success")
    return redirect(url_for("bookings"))


# ============================================================
# FESTIVALS - Information Page
# ============================================================

@app.route("/festivals")
def festivals():
    """Display cultural festivals information."""
    return render_template("festivals.html")


# ============================================================
# CONTACT - Contact Form
# ============================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact form for general inquiries."""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)",
            (name, email, subject, message),
        )
        conn.commit()
        cursor.close()
        conn.close()

        flash("Message sent! We will get back to you soon.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")


# ============================================================
# Run the Application
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
