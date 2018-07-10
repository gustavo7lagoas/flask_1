from models import Game, User

SQL_DELETA_JOGO = 'delete from jogo where id = %s'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_JOGO = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id = %s'
SQL_BUSCA_JOGOS = 'SELECT id, nome, categoria, console from jogo'
SQL_CRIA_JOGO = 'INSERT into jogo (nome, categoria, console) values (%s, %s, %s)'


class GameDao:
    def __init__(self, db):
        self.__db = db

    def save(self, jogo):
        cursor = self.__db.connection.cursor()

        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid
        self.__db.connection.commit()
        return jogo

    def get_all(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = translate_game(cursor.fetchall())
        return jogos

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tuple = cursor.fetchone()
        return Game(tuple[1], tuple[2], tuple[3], id=tuple[0])

    def delete(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.connection.commit()


class UserDao:
    def __init__(self, db):
        self.__db = db

    def search_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = translate_user(dados) if dados else None
        return usuario


def translate_game(jogos):
    def cria_jogo_com_tuple(tuple):
        return Game(tuple[1], tuple[2], tuple[3], id=tuple[0])
    return list(map(cria_jogo_com_tuple, jogos))


def translate_user(tuple):
    return User(tuple[0], tuple[1], tuple[2])
