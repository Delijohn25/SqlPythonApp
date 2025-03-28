from connection import get_connection

def insert_games(title, year, genre, publicer):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO games(title, year, genre, publicer) VALUES (%s, %s, %s, %s)"
    values = (title, year, genre, publicer)
    cursor.execute(sql, values)
    connection.commit()
    print("Το game προστέθηκε")
    cursor.close()
    connection.close()

insert_games("God Of War", 2018, "RPG", "Santa Monica Studio")
insert_games("Mortal Kombat X", 2015, "fighting", "Warner Bros")