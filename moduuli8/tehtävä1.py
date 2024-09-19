import mysql.connector

connection = mysql.connector.connect(
                host='127.0.0.1', # localhost
                port=3306,
                database='flight_game',
                user='nikedw',
                password='sad22',
                autocommit=True,
                collation='utf8mb4_general_ci'
                )

def fetch_airport_by_icao(code):
    sql = (f"SELECT name, municipality "
           f"FROM airport WHERE ident='{code}'")
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

airport = fetch_airport_by_icao('ZYTH')

user_input = input("Anna ICAO-koodi: ")
airport = fetch_airport_by_icao(user_input)

if airport:
    print(f"Haettu lentokenttä: {airport[0]}, {airport[1]}.")
else:
    print("Lentokenttää ei löydetty annetulla koodilla.")
