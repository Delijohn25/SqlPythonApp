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

title = input("Εισάγετε τίτλο του game:")
year = int(input("Εισάγετε το έτος λυκλοφορίας του game:"))
gerne = input("Εισάγετε το είδος του game:")
publicer = input("Εισάγετε τον εκδότη του game:")

insert_games(title, year, genre, publicer)