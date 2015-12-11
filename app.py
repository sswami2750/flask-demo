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

if __name__ == '__main__':
  app.run(port=33507)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

if __name__ == "__main__":
    app.run()