from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index1.html')
    return render_template('index1.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('register.html')
    return render_template('register.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('signin.html')
    return render_template('signin.html')

@app.route('/laptops',methods=['GET','POST'])
def laptops():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('laptops.html')
    return render_template('laptops.html')

@app.route('/props',methods=['GET','POST'])
def props():
    if request.method=='POST': 
        # Handle POST Request here
        return render_template('props.html')
    return render_template('props.html')

@app.route('/profile/dashboard',methods=['GET','POST'])
def prodile_dashboard():
    if request.method=='POST': 
        # Handle POST Request here
        return render_template('profile/dashboard.html')
    return render_template('profile/dashboard.html')







