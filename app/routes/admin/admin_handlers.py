from app import db
from app.modules.models import *
from app.modules.statistics_tools import *
from app.modules.images_tools import *

from flask_login import login_user, current_user, logout_user
from app import app, request, redirect

from app.routes.admin import admin_login_page


# Admin login form data handler
@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect('/admin/dashboard')

        username, password = request.form.get('username'), request.form.get('password')
        if username == '' or password == '':
            return admin_login_page(error_code=400)

        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin, remember=True)
            return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code


@app.route('/admin/logout')
def admin_logout_handler():
    if current_user.is_authenticated:
        logout_user()
        return redirect('/admin/login')
    return redirect('/not-allowed')


@app.route('/admin/image-logs/view')
def admin_view_logs_handler():
    if current_user.is_authenticated:
        return get_image_stat()
    return redirect('/not-allowed')


@app.route('/admin/image-logs/clear')
def admin_clear_logs_handler():
    if current_user.is_authenticated:
        clear_image_stat()
        return redirect('/admin/dashboard')
    return redirect('/not-allowed')


@app.route('/admin/images/remove/<int:image_id>')
def admin_remove_image_handler(image_id: int):
    if current_user.is_authenticated:
        delete_image(image_id)
        return redirect('/admin/images')
    return redirect('/not-allowed')
