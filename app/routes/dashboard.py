from flask import  render_template,request,redirect,url_for,flash
from flask  import  Blueprint

dashboard  = Blueprint('dashboard', __name__)

@dashboard.route('/profile/address', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
   
        return redirect(url_for('profile.dashboard'))

    return render_template('profile/address.html')







