import mysql.connector
import type.error_return_type as error_return_type
import config as cfg
class FetchOperation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database
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
            SELECT title, price
            FROM Video_Game
            WHERE price <= {budget}
            ORDER BY price DESC
            LIMIT 4000
            '''
            self.mycursor.execute(query)
            myresult = self.mycursor.fetchall()
            myresult.insert(0, ("Title", "Price"))
            return myresult
        except mysql.connector.errors.Error as err:
            print(f"mysql error : {err}")
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance
        
    
    def fetch_top_reviewed_games(self, amount_of_games):
        try :
            if (amount_of_games == ""):
                amount_of_games = 100
            elif self.contains_non_digit(amount_of_games):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid number")
                print(f"is error instance : {isinstance(errorInstance, error_return_type.ErrorReturnType)}")
                return errorInstance
            query = f'''
            SELECT 
                Video_game.title,
                Video_game.price,
                COUNT(Reviews.game_id) AS num_reviews,
                AVG(Reviews.score) AS avg_score
            FROM 
                Video_game
            JOIN 
                Reviews ON Video_game.game_id = Reviews.game_id
            GROUP BY 
                Video_game.game_id, Video_game.title, Video_game.price
            ORDER BY
                avg_score DESC,
                num_reviews DESC
            LIMIT {amount_of_games};
            '''
            self.mycursor.execute(query)
            myresult = self.mycursor.fetchall()
            myresult.insert(0, ("Title", "Price", "Number of reviews", "Average score"))
            return myresult
        except mysql.connector.errors.Error as err:
            print(f"mysql error : {err}")
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance
        
    def fetch_popular_among_streamer(self, amount_of_games):
        try :
            if (amount_of_games == ""):
                amount_of_games = 100
            elif self.contains_non_digit(amount_of_games):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid number")
                return errorInstance
            query = f'''
            SELECT 
                vg.title,
                COUNT(DISTINCT p.streamer_uid) AS streamer_count
            FROM 
                Video_game vg JOIN Plays p ON vg.game_id = p.game_id
            GROUP BY 
                vg.game_id
            ORDER BY 
                streamer_count DESC
            LIMIT {amount_of_games};
            '''
            self.mycursor.execute(query)
            myresult = self.mycursor.fetchall()
            myresult.insert(0, ("Title", "# of streamers playing"))
            return myresult
        except mysql.connector.errors.Error as err:
            print(f"mysql error : {err}")
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance
        
    def fetch_most_reviewed_streamed(self):
        try :
            query = '''
            WITH ReviewCounts AS (
                SELECT
                    vg.game_id,
                    COUNT(*) AS review_count
                FROM
                    Video_game vg
                JOIN Reviews r ON vg.game_id = r.game_id
                GROUP BY vg.game_id
            ),
            StreamCounts AS (
                SELECT
                    vg.game_id,
                    COUNT(*) AS stream_count
                FROM
                    Video_game vg
                JOIN Plays p ON vg.game_id = p.game_id
                GROUP BY vg.game_id
            ),
            GameCounts AS (
                SELECT
                    vg.game_id,
                    vg.title,
                    vg.company_name,
                    COALESCE(rc.review_count, 0) AS review_count,
                    COALESCE(sc.stream_count, 0) AS stream_count,
                    ia.platform_name
                FROM
                    Video_game vg
                LEFT JOIN ReviewCounts rc ON vg.game_id = rc.game_id
                LEFT JOIN StreamCounts sc ON vg.game_id = sc.game_id
                JOIN Is_Available ia ON vg.game_id = ia.game_id
            )
            SELECT
                gc.title,
                gc.company_name,
                gc.review_count,
                gc.stream_count,
                gc.platform_name
            FROM
                GameCounts gc
            ORDER BY
                gc.platform_name,
                gc.review_count DESC,
                gc.stream_count DESC;
            '''
            self.mycursor.execute(query)
            myresult = self.mycursor.fetchall()
            myresult.insert(0, ("Title", "Developer", "# of reviews", "# of streamers", "Platform"))
            return myresult
        except mysql.connector.errors.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance