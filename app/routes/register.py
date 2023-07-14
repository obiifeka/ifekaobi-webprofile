from flask import  render_template,request,redirect,url_for,flash
from flask  import  Blueprint




main  = Blueprint('main', __name__)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        agree_terms = request.form.get('agree_terms')

        # Perform form validation
        if not email or not password or not confirm_password or not agree_terms:
            error_message = 'All fields are required.'
            return render_template('signup.html', error_message=error_message)

        if password != confirm_password: 
            error_message = 'Passwords do not match.'
            return render_template('signup.html', error_message=error_message)

        # Perform user registration logic
        # Example: Create a new user in the database
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to a success page or login page
        flash('Registration successful. Please log in.')
        return redirect(url_for('profile.dashboard'))

    return render_template('signup.html')





# Sign-in section
@main.route('/signin',methods=['GET','POST'])
def signin():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('signin.html')
    return render_template('signin.html')

# Catrs section
@main.route('/carts',methods=['GET','POST'])
def carts():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('carts.html')
    return render_template('carts.html')

# Delivery
@main.route('/onepagecheckout/delivery',methods=['GET','POST'])
def delivery():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('onepagecheckout/delivery.html')
    return render_template('onepagecheckout/delivery.html')