from app import db
from app.modules.models import *

from flask_login import login_user, current_user, logout_user
from app import app, request, redirect

from app.routes.admin import admin_login_page


# Admin login form data handler
@app.route('/admin/login/form', methods=['GET', 'POST'])
def admin_login_handler():
    if request.method == 'POST':
        if current_user.is_authenticated:
            try:
                admin = Admin.query.get(current_user.get_id())
                admin.set_last_login(ip=request.remote_addr)
                db.session.add(admin)
                db.session.commit()
            except:
                pass
            return redirect('/admin/dashboard')
        username, password = request.form.get('username'), request.form.get('password')

        if username == '' or password == '':
            return admin_login_page(error_code=400)

        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.check_password(password):
            login_user(admin, remember=True)
            try:
                admin = Admin.query.get(current_user.get_id())
                print(admin)
                admin.set_last_login(ip=request.remote_addr)
                db.session.add(admin)
                db.session.commit()
            except:
                pass
            return redirect('/admin/dashboard')
    return admin_login_page(error_code=200)  # dev: Error code 200 is login error code
