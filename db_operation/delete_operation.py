import mysql.connector
import type.error_return_type as error_return_type
import config as cfg

class DeleteOperation():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database
        )
        self.mycursor = self.mydb.cursor()
    
    def fetch_reviewer(self):
        try :
            query = f'''
            SELECT *
            FROM Reviewer
            LIMIT 100000
            '''
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()
            result.insert(0, ("reviewer id", "first name", "last name"))
            return result
        except mysql.connector.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message=err.msg)
            return errorInstance
        
    def fetch_reviews(self):
        try :
            query = f'''
            SELECT *
            FROM Reviews
            ORDER BY reviewer_id
            LIMIT 100000
            '''
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()
            result.insert(0, ("game id", "reviewer id", "post id", "score", "review text"))
            return result
        except mysql.connector.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message=err.msg)
            return errorInstance

    def delete_reviewer_and_reviews(self, reviewer_id):
        try :
            query = f'''
            CALL DeleteReviewerAndReviews({reviewer_id});
            '''
            self.mycursor.execute(query)
            return True
        except mysql.connector.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message=err.msg)
            return errorInstance
    
    