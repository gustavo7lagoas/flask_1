from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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


app.run(debug=True)
