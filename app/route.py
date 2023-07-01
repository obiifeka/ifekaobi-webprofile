from . import app
from flask  import  render_template,url_for,redirect, request



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('contact.html')
    
    # Handle GET Request here
    return render_template('contact.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('signin.html')
    
    # Handle GET Request here
    return render_template('signin.html')