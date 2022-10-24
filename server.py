from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Dojo Survey Practice Session"

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')

#ALWAYS INCLUDE!! 
if __name__=="__main__":
    app.run(debug=True) 