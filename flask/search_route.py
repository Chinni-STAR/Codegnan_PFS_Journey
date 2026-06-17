    
""" 
1.Search note
--------------
-->This allows users to search notes, files, or any database
records based on a keyword entered in a form....
"""
from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)

@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []
    error = None
    message = None

    if request.method == 'POST':
        keyword = request.form['keyword'].strip()

        # Input Validation Using Regex
        if not re.match(r'^[A-Za-z0-9 ]+$', keyword):
            error = "Only letters, numbers, and spaces are allowed."
            return render_template(
                'search.html',
                error=error,
                results=results
            )

        # Database Connection
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='student_db'
        )

        cursor = conn.cursor(dictionary=True)

        # Query Execution Using LIKE Operator
        query = """
        SELECT ID AS id,
               NAME AS name,
               EMAIL AS email,
               PHONE AS phone,
               COURSE AS course
        FROM students
        WHERE NAME LIKE %s
        """
        cursor.execute(query, ('%' + keyword + '%',))

        results = cursor.fetchall()

        # If no records found
        if not results:
            message = f"No student found with the name {keyword}"

        cursor.close()
        conn.close()

    return render_template(
        'search.html',
        results=results,
        error=error,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)