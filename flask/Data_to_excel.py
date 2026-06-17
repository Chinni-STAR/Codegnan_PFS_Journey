'''
1.Excel Data Generation
-----------------------
-->Excel Data Generation allows users to download database records in excel format...
-->Flask can generate excel files using
'''

# import flask_excel as excel
# from flask import Flask

# app=Flask(__name__)
# excel.init_excel(app)
# @app.route('/download')
# def download():
#     data=[
#         ["ID","Name","Course"],
#         [1,"chinni","python"],
#         [2,"maha","Sql"],
#         [3,"jai","python"]
#     ]
#     return excel.make_response_from_array(
#         data,"xlsx",
#         file_name="students"
#     )
# if __name__=='__main__':
#     app.run(debug=True)

from flask import Flask,session,redirect,url_for
app=Flask(__name__)
app=secret_key='secret123'
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))
if __name__=='__main__':
    app.run(debug=True)