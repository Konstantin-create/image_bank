from app import app, render_template, redirect

from flask_login import current_user
from app.modules.models import *


@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard_page():
    return render_template('admin/dashboard_page.html')
