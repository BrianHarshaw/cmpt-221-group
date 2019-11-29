from flask import Flask, escape, url_for, request, render_template
from flask_user import roles_required
from jinja2 import Template
app = Flask(__name__)

## Below works without the roles. Need to setup the specific actions each user can do in each role.
## Need to implement Database and login before the roles can go to their respective pages
## Code for above is @roles_required('__role_here__') and after the @app.route

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student/dashboard')  # Route to go to student page
def student_dashbaord():
    return render_template('student.html')  # render student template here

@app.route('/student_worker/dashboard')  # Route to go to student worker page
def student_worker_dashboard():
    return render_template('student_worker.html')  # render student worker template here

@app.route('/faculty/dashboard')  # Route to go to faculty page
def faculty_dashbaord():
    return render_template('faculty.html')  # render faculty template here

@app.route('/department_head/dashboard')  # Route to go to department head page
def dept_head_dashboard():
    return render_template('dept_head.html')  # render dept head template here

@app.route('/admin/dashboard')  # Route to go to admin page
def admin_dashboard():
    return render_template('admin.html')  # render admin template here

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 80, debug = True)