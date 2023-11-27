import mysql.connector
import type.error_return_type as error_return_type
class FetchOperation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dudeabides1999",
        database="final_project_431"
        )
        self.mycursor = self.mydb.cursor()
    
    # Users can fetch information about a video game’s publisher, released platforms, and date of release for a given game title
    def fetch_game_info_by_title(self, game_title):
        if game_title == "":
            return False
        query = f'''
        SELECT
            Video_game.title,
            Video_game.release_date,
            Game_company.company_name AS publisher,
            Game_platform.platform_name
        FROM
            Video_game
        JOIN
            Game_company ON Video_game.company_name = Game_company.company_name
        JOIN
            Is_Available ON Video_game.game_id = Is_Available.game_id
        JOIN
            Game_platform ON Is_Available.platform_name = Game_platform.platform_name
        WHERE
            Video_game.title LIKE '%{game_title}%'
        ORDER BY
            Video_game.title, Game_platform.platform_name;
        '''
        self.mycursor.execute(query)
        myresult = self.mycursor.fetchall()
        myresult.insert(0, (f"Fetched all title that contains {game_title}", ""))
        myresult.insert(1, ("Title", "Release Date", "Publisher", "Platform"))
        return myresult

    def contains_non_digit(self,input_string):
        for char in input_string:
            if not char.isdigit():
                return True  # Found a non-digit character
        return False  # All characters are digits

    def fetch_top_selling_game(self, amount_of_games):
        if self.contains_non_digit(amount_of_games):
            return False
        if amount_of_games == "":
            amount_of_games = 100
        print(amount_of_games)
        query = f'''
        SELECT title, sales
        FROM Video_Game
        ORDER BY sales DESC
        LIMIT {amount_of_games}
        '''
        self.mycursor.execute(query)
        myresult = self.mycursor.fetchall()
        myresult.insert(0, (f"Fetched {amount_of_games} games", ""))
        myresult.insert(1, ("Title", "Sales"))
        return myresult
    
    def fetch_game_within_budget(self, budget):
        try :
            if self.contains_non_digit(budget):
                print("input format error")
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid number")
                print(f"is error instance : {isinstance(errorInstance, error_return_type.ErrorReturnType)}")
                return errorInstance
            if budget == "":
                budget = 40
            query = f'''
            T title, price
            FROM Video_Game
            WHERE price <= {budget}
            ORDER BY price DESC
            '''
            self.mycursor.execute(query)
            myresult = self.mycursor.fetchall()
            myresult.insert(0, ("Title", "Price"))
            return myresult
        except mysql.connector.errors.Error as err:
            print(f"mysql error : {err}")
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance