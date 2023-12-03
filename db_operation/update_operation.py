import mysql.connector
import type.error_return_type as error_return_type
import config as cfg

class UpdateOperation():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database
        )
        self.mycursor = self.mydb.cursor()

    def contains_non_digit(self, input):
        return not input.isdigit()
    
    def format_field(self, field):
        return str(field).ljust(50)
    
    def fetch_game_by_gameid(self):
        query = f'''
        SELECT *
        FROM Video_game
        LIMIT 10000
        '''
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        result.insert(0, ("game_id", "title", "price", "release date", "sales", "Developer" ))
        return result

    def fetch_reviews(self):
        query = f'''
        SELECT *
        FROM Reviews
        LIMIT 10000
        '''
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        result.insert(0, ("game id", "reviewer id", "post id", "score", "review text" ))
        return result

    def update_review_score(self, game_id, reviewer_id, post_id, score):
        try :
            query = f'''
            UPDATE Reviews
            SET score = {score}
            WHERE game_id = {game_id} AND reviewer_id = {reviewer_id} AND post_id = {post_id}
            '''
            self.mycursor.execute(query)
            self.mycursor.fetchall()
            self.mydb.commit()

            if (self.mycursor.rowcount == 0):
                errorInstance = error_return_type.ErrorReturnType(error_message="No such review exists or you have entered score that is already in the database")
                return errorInstance
            
            return_query = f'''
            SELECT *
            FROM Reviews
            WHERE game_id = {game_id} AND reviewer_id = {reviewer_id} AND post_id = {post_id}
            '''
            self.mycursor.execute(return_query)
            result = self.mycursor.fetchall()
            result.insert(0, ("game id", "reviewer id", "post id", "score", "review text" ))
            return result
        except mysql.connector.errors.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance

    def update_game_sales_data(self, game_id, sales):
        try :
            query = f'''
            UPDATE Video_game
            SET sales = {sales}
            WHERE game_id = {game_id}
            '''
            self.mycursor.execute(query)
            self.mycursor.fetchall()
            self.mydb.commit()
            
            return_query = f'''
            SELECT *
            FROM Video_game
            WHERE game_id = {game_id}
            '''
            self.mycursor.execute(return_query)
            result = self.mycursor.fetchall()
            result.insert(0, ("game_id", "title", "price", "release date", "sales", "Developer" ))
            return result
        except mysql.connector.errors.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message="Database error")
            return errorInstance
        
    
    def fetch_game_companies(self):
        query = f'''
        SELECT *
        FROM Game_company
        LIMIT 10000
        '''
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        result.insert(0, ("Name of company", "# of employees", "Year of foundation"))
        return result
    
    def update_game_company_info(self, company_name, num_employees, foundation_year):
        try :
            # Empty string check
            if (company_name == ""):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid company name")
                return errorInstance
            elif (num_employees == ""):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid number of employees")
                return errorInstance
            elif (foundation_year == ""):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid foundation year")
                return errorInstance
            
            # Non digit check
            if (self.contains_non_digit(num_employees)):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid number of employees")
                return errorInstance
            elif (self.contains_non_digit(foundation_year)):
                errorInstance = error_return_type.ErrorReturnType(error_message="Please enter a valid foundation year")
                return errorInstance
            
            query = f'''
            UPDATE Game_company
            SET num_employees = {num_employees}, foundation_year = {foundation_year}
            WHERE company_name = "{company_name}"
            '''
            self.mycursor.execute(query)
            self.mycursor.fetchall()
            self.mydb.commit()

            if (self.mycursor.rowcount == 0):
                errorInstance = error_return_type.ErrorReturnType(error_message="No such company exists or you have entered information that is already in the database")
                return errorInstance
            
            return_query = f'''
            SELECT *
            FROM Game_company
            WHERE company_name = "{company_name}"
            '''
            self.mycursor.execute(return_query)
            result = self.mycursor.fetchall()
            result.insert(0, ("Name of company", "# of employees", "Year of foundation"))
            return result
        except mysql.connector.errors.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message=f"Database error : {err.msg}")
            return errorInstance