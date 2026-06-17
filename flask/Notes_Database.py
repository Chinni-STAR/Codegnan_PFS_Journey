# Notes Management in Flask (Add, View All, View Single, Update, Delete)
# Introduction
# Required Imports

from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Login Route (Temporary)
@app.route('/login')
def login():
    session['user_id'] = 1
    flash("Login Successful")
    return redirect('/add_note')

# Route – Add a New Note
# Features
@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if 'user_id' not in session:
        flash("Please Login First")
        return redirect('/login')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="notes_db"
        )
        cursor = conn.cursor()
        query = """
        INSERT INTO notes(user_id,title,content)
        VALUES(%s,%s,%s)
        """
        cursor.execute(
            query,
            (session['user_id'], title, content)
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Note Added Successfully")
        return redirect('/view_notes')
    return render_template('add_note.html')


# Route – View All Notes
# Features
@app.route('/view_notes')
def view_notes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="notes_db"
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM notes"
    cursor.execute(query)
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template(
        "view_notes.html",
        notes=notes
    )

# View a Single Note
@app.route('/viewnotes/<int:note_id>')
def view_note(note_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="notes_db"
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM notes WHERE note_id=%s"
    cursor.execute(query, (note_id,))
    note = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template(
        "viewnote.html",
        note=note
    )

#Update Notes
@app.route('/updatenotes/<int:note_id>', methods=['GET', 'POST'])
def update_note(note_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="notes_db"
    )
    cursor = conn.cursor(dictionary=True)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        query = """
        UPDATE notes
        SET title=%s,
            content=%s
        WHERE note_id=%s
        """
        cursor.execute(
            query,
            (title, content, note_id)
        )
        conn.commit()
        flash("Note Updated Successfully")
        cursor.close()
        conn.close()
        return redirect('/view_notes')
    query = "SELECT * FROM notes WHERE note_id=%s"
    cursor.execute(query, (note_id,))
    note = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template(
        "update_note.html",
        note=note
    )

#Delete Notes
@app.route('/deletenotes/<int:note_id>')
def delete_note(note_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="notes_db"
    )
    cursor = conn.cursor()
    query = "DELETE FROM notes WHERE note_id=%s"
    cursor.execute(query, (note_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Note Deleted Successfully")
    return redirect('/view_notes')

if __name__ == "__main__":
    app.run(debug=True)
