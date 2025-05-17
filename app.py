from flask import Flask, render_template
from flask_mysqldb import MySQL  # <-- import MySQL extension here
from mail_setup import mail
from routes.user_routes import user_routes
from routes.staff_routes import staff_routes
from routes.worker_routes import worker_routes
from routes.central_routes import central_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL config - ADD this block here:
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'

# Initialize MySQL extension
mysql = MySQL(app)

# Mail Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'swachhindiamission@gmail.com'
app.config['MAIL_PASSWORD'] = 'kgqh ygmw fdrc tnxx'  # Replace with your app password

# Initialize mail object
mail.init_app(app)

# Register blueprints for each module
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(staff_routes, url_prefix='/staff')
app.register_blueprint(worker_routes, url_prefix='/worker')
app.register_blueprint(central_routes, url_prefix='/central')

# Home route
@app.route('/')
def index():
    return render_template('home.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Prevent caching for all responses
@app.after_request
def prevent_caching(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)
