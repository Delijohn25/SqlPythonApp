from connection import get_connection

def view_games():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT FROM games"
    cursor.execute(sql)
    games = cursor.fetchall()

    if games:
        print("Λίστα games")
        for game in games:
            print(f"id{game[0]}, title:{game[1]}, year: {game[2]}, genre: {game[3]}, publicer: {game[4]}")
    else:
        print("Δέν υπάρχουν games")
    cursor.close()
    connection.close()

view_games()