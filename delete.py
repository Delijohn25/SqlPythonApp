from connection import get_connection   

def delete_games(game_id):
    connection = get_connection()
    cursor = connection_cursor()
    sql = "DELETE FROM games WHERE id = %s"
    cursor.execute(sql,(game_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Διαγράφηκε")
    else:
        print("Δεν διαγράφηκε")

        cursor.close()
        connection.close()
        
try:
    games = int(input("Εισάγετε τίτλο:"))
    delete_games(game_id)
except ValueError:
    print("Δεν βάλατε έγκυρο τίτλο")