from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
    author = "Sumanth"
    Name = "Michael"
    return render_template('index.html')
    
@app.route('/signup', methods = ['POST'])
def signup():
    stock = request.form['Ticker Symbol']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
  app.run(port=33507)

