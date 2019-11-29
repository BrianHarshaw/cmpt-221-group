from flask_user import roles_required

@route('/student/dashboard')  # Route to go to student page
@roles_required('Student')
def student_dashbaord():
    # render student template here

@route('/student_worker/dashboard')  # Route to go to student worker page
@roles_required('Student Worker')
def student_worker_dashboard():
    # render student worker template here

@route('/faculty/dashboard')  # Route to go to faculty page
@roles_required('Faculty')
def faculty_dashbaord():
    # render faculty template here

@route('/depart_head/dashboard')  # Route to go to department head page
@roles_required('Department Head')
def dept_head_dashboard():
    # render dept head template here

@route('/admin/dashboard')  # Route to go to admin page
@roles_required('Admin')
def admin_dashboard():
    # render admin template here