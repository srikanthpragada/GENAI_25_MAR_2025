import sqlite3
def get_total_credits(search_string):
    """Return the total number of credits for courses matching the search string."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(credits) FROM Courses
            WHERE name LIKE ? OR description LIKE ?
        """, (f"%{search_string}%", f"%{search_string}%"))
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0
# filepath: c:\classroom\mar25\aipair\courses_crud.py

def create_table():
    """Create the Courses table if it doesn't exist."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                credits INTEGER
            )
        """)
        conn.commit()

def add_course(name, description, credits):
    """Add a new course to the Courses table."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Courses (name, description, credits)
            VALUES (?, ?, ?)
        """, (name, description, credits))
        conn.commit()

def get_courses():
    """Retrieve all courses from the Courses table."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        return cursor.fetchall()

def update_course(course_id, name=None, description=None, credits=None):
    """Update an existing course in the Courses table."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE Courses SET name = ? WHERE id = ?", (name, course_id))
        if description:
            cursor.execute("UPDATE Courses SET description = ? WHERE id = ?", (description, course_id))
        if credits:
            cursor.execute("UPDATE Courses SET credits = ? WHERE id = ?", (credits, course_id))
        conn.commit()

def delete_course(course_id):
    """Delete a course from the Courses table."""
    with sqlite3.connect("courses.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Courses WHERE id = ?", (course_id,))
        conn.commit()

# Example usage
if __name__ == "__main__":
    create_table()
    add_course("Mathematics", "An introduction to algebra and calculus", 4)
    add_course("Physics", "Fundamentals of mechanics and thermodynamics", 3)
    print("Courses after adding:")
    print(get_courses())
    update_course(1, credits=5)
    print("Courses after updating:")
    print(get_courses())
    delete_course(2)
    print("Courses after deleting:")
    print(get_courses())

    print()