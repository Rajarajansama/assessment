from flask import Flask, request, render_template

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USERNAME'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'createpassword'
app.config['MYSQL_DATABASE_DB'] = 'login'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def my_form():
    return render_template('loginpage.html')


@app.route('/', methods=['post'])
def authenticate():

    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user where username='" + username + "' and password='" + password +"'")
    data = cursor.fetchone()
    if data is None:
        return "username or password is wrong"
    else:
        return"logged in successfully"


if __name__ == "__main__":
    app.run()
