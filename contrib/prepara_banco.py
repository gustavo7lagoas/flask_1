import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='172.17.0.2', port=3306)

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `gamelibrary`;")
# conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `gamelibrary` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `gamelibrary`;
    CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) COLLATE utf8_bin NOT NULL,
      `category` varchar(40) COLLATE utf8_bin NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `user` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `name` varchar(20) COLLATE utf8_bin NOT NULL,
      `password` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO gamelibrary.user (id, name, password) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from gamelibrary.user')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
      'INSERT INTO gamelibrary.game (name, category, console) VALUES (%s, %s, %s)',
      [
            ('God of War 4', 'Action', 'PS4'),
            ('NBA 2k18', 'Sports', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Racing', 'SNES'),
            ('Fire Emblem Echoes', 'Strategy', '3DS'),
      ])

cursor.execute('select * from gamelibrary.game')
print(' -------------  Games:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()