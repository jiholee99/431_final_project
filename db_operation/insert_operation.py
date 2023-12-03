import mysql.connector
import type.error_return_type as error_return_type
import config as cfg
class InsertOperation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database
        )
        self.mycursor = self.mydb.cursor()
    
    # Users can input streamer information
    def insertStreamerInfo(self, streamer_uid, username, subscribers):
        try:                               #test if streamer_uid can be converted to int, return false if fails
            streamer_uid = int(streamer_uid)
        except ValueError:
            print("streamer_uid cannot be converted to int")
            return False
        try:                               #test if subscribers can be converted to int, return false if fails
            subscribers = int(subscribers)
        except ValueError:
            print("subscribers cannot be converted to int")
            return False
        if streamer_uid == "": # checks for empty strings in streamer_uid
            print("streamer_uid is blank")
            return False
        if username == "": # checks for empty strings in username
            print("username is blank")
            return False
        if subscribers == "":              # if subscribers is empty, set subscribers to 0
            subscribers = 0
        subscribers = int(subscribers)
        
        query = f'''
        INSERT INTO Streamer(streamer_uid, username, subscribers)
        VALUES({streamer_uid}, '%{username}%', {subscribers});
        '''
        self.mycursor.execute(query)
        self.mydb.commit()
        #myresult = self.mycursor.fetchall()
        #myresult.insert(0, (f"Fetched all title that contains {game_title}", ""))
        #myresult.insert(1, ("Title", "Release Date", "Publisher", "Platform"))
        #return myresult
        return f"Inserted streamer info: Streamer User ID:{streamer_uid}, Username: {username}, Subscribers: {subscribers}"

    #def contains_non_digit(self,input_string):
    #    for char in input_string:
    #        if not char.isdigit():
    #            return True  # Found a non-digit character
    #    return False  # All characters are digits

    #users can input platforms that a streamer streams on
    def insertPlatform(self, streamer_uid, platform):
        #if self.contains_non_digit(amount_of_games):
        #    return False
        try:                               #test if streamer_uid can be converted to int, return false if fails
            streamer_uid = int(streamer_uid)
        except ValueError:
            print("ValueError with the streamer_uid")
            return False
        if streamer_uid == "":
            print("streamer_uid is blank")
            print(streamer_uid)
            return False
        if platform == "":
            print("platform is blank")
            print(platform)
            return False
        streamer_uid = int(streamer_uid)
        #print(amount_of_games)
        query = f'''
        INSERT INTO streams_on(streamer_uid, platform_name)
        VALUES({streamer_uid}, '%{platform}%');
        '''
        self.mycursor.execute(query)
        self.mydb.commit()
        #myresult = self.mycursor.fetchall()
        #myresult.insert(1, ("Title", "Sales"))
        #return myresult
        return "Inserted platform that a streamer streams on: Streamer User ID: {streamer_uid}, Platform: {platform}"
    """
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
    """