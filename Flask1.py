from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/bootstrapex')
def yunus():
    return render_template('bootstrapex.html')

app.run(debug=True)