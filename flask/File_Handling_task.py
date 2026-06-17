""" 
What is a file upload?
File Upload allows users to select a file from their system and store it on the server
1. Uploading file
----------------
"""
# import os # to system communicate to perform os operations to import os module
# from flask import Flask, render_template
# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads' # specify the folder where uploaded files will be stored
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # configure the upload folder in the Flask app
# os.makedirs(UPLOAD_FOLDER, exist_ok=True) # create the upload folder if it doesn't exist
""" import os
from flask import Flask, redirect, request, send_file, send_from_directory, session, flash,request, render_template
import mysql.connector
app=Flask(__name__)
UPLOAD_FOLDER="uploads"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/uploadfile', methods=['GET','POST'])
def uploadfile():
    if 'user' not in session:
        return redirect('/login')
    if request.method=='POST':
        file=request.files['file']
        if file.filename=='':
            flash("No file selected")
            return redirect('/uploadfile')
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="flaskfiles"
            )
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM uploads WHERE filename=%s",(file.filename,))
        existing_file=cursor.fetchone()
        if existing_file:
            flash("File already exists")
            return redirect('/uploadfile')
        filepath=os.path.join(
            app.config['UPLOAD_FOLDER'],file.filename)
        file.save(filepath)
        cursor.execute(
            "INSERT INTO uploads(user_id,filename,file_path) VALUES(%s,%s,%s)",
            (session['user_id'],file.filename,filepath)
        )
        conn.commit()
        flash("File uploaded successfully")
        cursor.close()
        conn.close()
        return redirect('/uploadfile')
    return render_template('uploadfile.html')
#fetching file metadata
@app.route('/viewallfiles')
def viewallfiles():
    if 'user_id' not in session:
        flash("Please Login First")
        return redirect('/login')
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="flaskfiles"
    )
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM uploads WHERE user_id=%s order by uploaded_at DESC",(session['user_id'],))
    files=cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('viewallfiles.html',files=files)
@app.route('/delete/<int:file_id>')
def delete_file(file_id):
    if 'user_id' not in session:
        return redirect('/login')
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",        
        database="flaskfiles"
    )
    cursor=conn.cursor()
    cursor.execute("DELETE FROM uploads WHERE id=%s ",(file_id,))
    file=cursor.fetchone()
    if file:
        if os.path.exists(file['file_path']):
            os.remove(file['file_path'])
        cursor.execute("DELETE FROM uploads WHERE id=%s",(file_id,))
        conn.commit()
        flash("File deleted successfully")
    cursor.close()
    conn.close()
    return redirect('/viewallfiles')

@app.route('/viewfile/<int:file_id>')
def view_file(file_id):
    if 'user_id' not in session:
        return redirect('/login')
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="flaskfiles"
    )
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM uploads WHERE id=%s",(file_id,))
    file=cursor.fetchone()
    cursor.close()
    conn.close()
    if file:
        return send_file(file['file_path'])
    return "File not found"
@app.route('/download/<int:file_id>')
def download_file(file_id):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename=file_id,as_attachment=True)
@app.route('/metadata/<int:file_id>')
def metadata(file_id):
   
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root", 
        database="flaskfiles"       
    )
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM uploads WHERE id=%s",(file_id,))
    file=cursor.fetchone()
    cursor.close()
    conn.close()
    if file:
        return render_template('metadata.html', file=file)
    flash("File not found")
    return redirect('/viewallfiles') """
from flask import Flask, render_template, request, redirect, send_file, send_from_directory, flash, session
import mysql.connector
import os
from io import BytesIO

app = Flask(__name__)
app.secret_key = "secret"

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flaskfiles"
)

cursor = conn.cursor()

# Home
@app.route('/')
def home():
    return redirect('/upload')


# Upload File
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        file = request.files['file']
        video_url = request.form['video_url']

        if file.filename == '':
            flash("Select a file")
            return redirect('/upload')

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        # Duplicate Check
        if os.path.exists(filepath):
            flash("File already exists")
            return redirect('/upload')

        # Save File
        file.save(filepath)

        # Store Metadata
        sql = """
        INSERT INTO files(filename,video_url)
        VALUES(%s,%s)
        """
        cursor.execute(sql, (file.filename, video_url))
        conn.commit()

        flash("File Uploaded Successfully")

    return render_template('upload.html')


# View All Files
@app.route('/files')
def files():

    cursor.execute("SELECT * FROM files")
    data = cursor.fetchall()

    return render_template(
        'files.html',
        files=data
    )


# View File in Browser
@app.route('/view/<filename>')
def view_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename
    )


# Download File
@app.route('/download/<filename>')
def download_file(filename):

    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        filename,
        as_attachment=True
    )


# Delete File
@app.route('/delete/<int:id>')
def delete_file(id):

    cursor.execute(
        "SELECT filename FROM files WHERE id=%s",
        (id,)
    )

    file = cursor.fetchone()

    if file:

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file[0]
        )

        if os.path.exists(filepath):
            os.remove(filepath)

        cursor.execute(
            "DELETE FROM files WHERE id=%s",
            (id,)
        )

        conn.commit()

        flash("File Deleted")

    return redirect('/files')


# File Metadata
@app.route('/metadata/<int:id>')
def metadata(id):

    cursor.execute(
        "SELECT * FROM files WHERE id=%s",
        (id,)
    )

    file = cursor.fetchone()

    return f"""
    ID : {file[0]} <br>
    File Name : {file[1]} <br>
    Video URL : {file[2]} <br>
    Uploaded At : {file[3]}
    """


# BytesIO Example
@app.route('/memoryfile')
def memoryfile():

    data = BytesIO()

    data.write(
        b"Welcome to Flask File Handling"
    )

    data.seek(0)

    return send_file(
        data,
        as_attachment=True,
        download_name="sample.txt",
        mimetype="text/plain"
    )


# send_file Example
@app.route('/sendpdf')
def sendpdf():

    path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        "sample.pdf"
    )

    return send_file(path)


if __name__ == "__main__":
    app.run(debug=True)
