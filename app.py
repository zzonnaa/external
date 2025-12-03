from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    rollno=request.form['rollno']
    year=request.form['year']
    return render_template('result.html', username=username, email=email, rollno=rollno, year=year)
if __name__ == '__main__':
    app.run(debug=True)
    