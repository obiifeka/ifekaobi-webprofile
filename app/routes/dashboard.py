from flask import  render_template,request,redirect,url_for,flash
from flask  import  Blueprint

dashboard  = Blueprint('dashboard', __name__)


@dashboard.route('/profile/address', methods=['GET', 'POST'])
def address():
    if request.method == 'POST':
   
        return redirect(url_for('profile/dashboard.html'))

    return render_template('profile/address.html')


# Billling Address section

@dashboard.route('/profile/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('profile/create.html')
    return render_template('profile/create.html')
 
 # END Billling Address section
 
 
 
 
  # Order  section

@dashboard.route('/profile/order',methods=['GET','POST'])
def order():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('profile/order.html')
    return render_template('profile/order.html')

  # PAyments  section

@dashboard.route('/profile/payment',methods=['GET','POST'])
def payment():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('profile/payment.html')
    return render_template('profile/payment.html')






