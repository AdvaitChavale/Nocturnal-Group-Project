from flask import Flask, render_template, request, redirect, url_for, session
from data import data
from recommendation import input_fn
# from congrats import data
# from auth import register_user, login

users = {'username': 'student', 'password': 'student1234'}

app = Flask(__name__, template_folder='interfaces', static_folder='staticFolder')

correct_answers = ["B", "C", "C", "A", "B"]

input = data()


@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/login')
# def login():
#     return render_template('loginPage.html')

# @app.route('/signup', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         email = request.form["email"]
#         password = request.form["password"]
#         result = register_user(email, password)
#         if result == "succesfull":
#             return redirect(url_for('form'))
#     else:
#         return render_template('registerPage.html')
    
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         email = request.form["email"]
#         password = request.form["password"]
#         result = login(email, password)
#         if result == "succesfull":
#             return redirect(url_for('form'))
#     else:
#         return render_template('loginPage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['username'] and password == users['password']:
            return redirect('/game')
        else:
            return "<h1>Login Failed</h1>"
    return render_template('loginPage.html')

@app.route('/test', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        user_answer = [request.form[f'q{i}'] for i in range(1,6)]
        score = sum([1 for i in range(5) if user_answer[i]==correct_answers[i]])
        result = input_fn(score)
        return redirect(url_for('criteria', name="{}".format(result)))
    else:
        return render_template('form.html')

@app.route('/<name>')
def criteria(name):
    return render_template("criteria.html", type=name)

@app.route('/<name>')
def score(name):
    return render_template('registerPage.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/course')
def courses():
    current_index = session.get('current_index', 0)
    current_object = input[current_index]
    print(current_object)
    return render_template('course.html', value=current_object)

@app.route('/next', methods=['POST'])
def next_object():
    current_index = session.get('current_index', 0)
    if current_index < len(input) - 1:
        current_index += 1
        session['current_index'] = current_index
    return redirect(url_for('courses'))

@app.route('/previous', methods=['POST'])
def previous_object():
    current_index = session.get('current_index', 0)
    if current_index > 0:
        current_index -= 1
        session['current_index'] = current_index
    return redirect(url_for('courses'))

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/congrats')
def congrats():
    return render_template('congrats.html')

if __name__ == "__main__":
    app.secret_key = 'Nocturnal'
    app.run(debug=True)