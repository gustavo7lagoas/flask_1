from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'testing_flask'

class Game:
    def __init__(self, name, category, game_console):
        self.name = name
        self.category = category
        self.game_console = game_console

game1 = Game('Super Mario RPG', 'RPG', 'SNES')
game2 = Game('Tetris', 'Puzzle', 'Several')
game3 = Game('Fifa 2018', 'Sports', 'Several')
game4 = Game('Street Fighter 2', 'Fight', 'Several')
game_list = [game1, game2, game3, game4]


@app.route('/')
def index():
    return render_template('list.html', title='my games', game_list=game_list)


@app.route('/new')
def new():
    return render_template('new.html', title='New Game')


@app.route('/create', methods=['POST',])
def create():
    game = Game(request.form['name'], request.form['category'],
        request.form['game_console'])
    game_list.append(game)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html', title='login')


@app.route('/authenticate', methods=['POST',])
def auth():
    if 'mestra' == request.form['passwd']:
        session['authenticated_user'] = request.form['username']
        flash('You were successfully logged in')
        return redirect('/new')
    else:
        flash('Invalid Credentials')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['authenticated_user'] = None
    return redirect('/')


app.run(debug=True)
