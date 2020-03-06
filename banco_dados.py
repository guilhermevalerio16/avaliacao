import sqlite3

connection = sqlite3.connect('tempo_no_momento.db')

c = connection.cursor()


def create_table():
    c.execute("""
    CREATE TABLE IF NOT EXISTS clima
    (
        id                     integer,
        nome                   text,
        estado                 text,
        pais                   text,
        temperatura            integer,
        direcao_do_vento       text,
        intensidade_do_vento   integer,
        umidade_relativa_do_ar integer,
        condicao               text,
        pressao                integer,
        sensacao_termica       text,
        data                   text
    )

    """)


create_table()

def data_entry(dictionary):
    parameters = (dictionary['id'], dictionary['name'], dictionary['state'], dictionary['country'],
                  dictionary['data']['temperature'], dictionary['data']['wind_direction'],
                  dictionary['data']['wind_velocity'], dictionary['data']['humidity'], dictionary['data']['condition'],
                  dictionary['data']['pressure'], dictionary['data']['sensation'], dictionary['data']['date'])

    c.execute("INSERT INTO clima VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", parameters)

def query():
    c.execute("SELECT * FROM clima")
    lines = c.fetchall()
    for line in lines:
        print(line)

    connection.commit()
