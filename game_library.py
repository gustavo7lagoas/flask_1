from flask import Flask, render_template, request, redirect, session, flash, \
    url_for

app = Flask(__name__)
app.secret_key = 'testing_flask'


class User:
    def __init__(self, id, name, passwd):
        self.id = id
        self.name = name
        self.passwd = passwd


user1 = User('gustavo', 'Gustavo Moreira', 'passwd')
user2 = User('fran', 'Francislene Patrícia', '1234')
user3 = User('nicolas', 'Nicolas', 'lol')
users = {user1.id: user1, user2.id: user2, user3.id: user3}


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
    if 'authenticated_user' not in session or session['authenticated_user'] == None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template('new.html', title='New Game')


@app.route('/create', methods=['POST',])
def create():
    game = Game(request.form['name'], request.form['category'],
        request.form['game_console'])
    game_list.append(game)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', title='login', next=next)


@app.route('/authenticate', methods=['POST',])
def auth():
    if request.form['username'] in users:
        user = users[request.form['username']]
        if user.passwd == request.form['passwd']:
            session['authenticated_user'] = request.form['username']
            flash('{}, you were successfully logged in'.format(user.name))
            next = request.form['next']
            return redirect(next)
    flash('Invalid Credentials')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['authenticated_user'] = None
    return redirect(url_for('index'))


app.run(debug=True)
