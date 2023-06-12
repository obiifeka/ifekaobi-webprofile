from flask import redirect,url_for,render_template,request, Blueprint
from  . import app

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

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

 
  