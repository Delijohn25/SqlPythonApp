from connection get_connection

def update_games(game_id, title= None, year= None, genre= None, publicer= None):

    connection = get_connection()
    cursor = connection.cursor()

    updates = [] #updates = [title = %s,year= %s, genre= %s, publicer= %s]
    values = [] #values =  ['game 3', 2002, 'RPG', 'EA']

    if title:
        updates.append("title = %s")
        values.append(title)

    if year:
        updates.append("year = %s")
        values.append(year)

    if genre:
        updates.append("genre = %s")
        values.append(genre)

     if publicer:
        updates.append("publicer = %s")
        values.append(publicer)

    if updates:
        sql = f"UPDATE games SET {', '.join(updates)} WHERE game_id = %s"
        values.append(game_id)
        cursor.execute(sql, tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            print("Το update έγινε!")
        else:
            print("Δεν βρέθηκε.")

        cursor.close()
        connection.close()

try:
    game_id = int(input("Εισάγεται τo game id που θέλετε να το αλλάξετε:"))
    title = input("Εισάγεται τον τίτλο αν θέλετε να τον αλλάξετε:")
    year = int(input("Εισάγεται την χρονολογία αν θέλετε να την αλλάξετε:"))
    genre = int(input("Εισάγεται το είδος αν θέλετε να το αλλάξετε:"))
    publicer = input("Εισάγεται τον εκδότη αν θέλετε να τον αλλάξετε:")
    update_games(game_id, title or None, year or None, genre or None, publicer or None)
except ValueError:
    print("Δώστε έγκυρο το game id")