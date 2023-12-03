import mysql.connector
import type.error_return_type as error_return_type
import config as cfg

class AnalyticalOperation:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        database=cfg.database
        )
        self.mycursor = self.mydb.cursor()

    def get_sorted_game_report(self, sort_by):
        try :
            if sort_by == "# of streamers playing":
                query = f'''
                SELECT 
                    vg.game_id,
                    vg.title,
                    COUNT(DISTINCT ia.platform_name) AS num_platforms_available,
                    COUNT(DISTINCT p.streamer_uid) AS num_streamers_playing,
                    vg.sales
                FROM 
                    Video_game vg
                LEFT JOIN 
                    Is_Available ia ON vg.game_id = ia.game_id
                LEFT JOIN 
                    Plays p ON vg.game_id = p.game_id
                GROUP BY 
                    vg.game_id, vg.title, vg.sales
                ORDER BY
                    num_streamers_playing DESC
                LIMIT 100000
                '''
            elif sort_by == "# of platform available":
                query = f'''
                SELECT 
                    vg.game_id,
                    vg.title,
                    COUNT(DISTINCT ia.platform_name) AS num_platforms_available,
                    COUNT(DISTINCT p.streamer_uid) AS num_streamers_playing,
                    vg.sales
                FROM 
                    Video_game vg
                LEFT JOIN 
                    Is_Available ia ON vg.game_id = ia.game_id
                LEFT JOIN 
                    Plays p ON vg.game_id = p.game_id
                GROUP BY 
                    vg.game_id, vg.title, vg.sales
                ORDER BY
                    num_platforms_available DESC
                LIMIT 100000
                '''
            elif sort_by == "Game sales":
                query = f'''
                SELECT 
                    vg.game_id,
                    vg.title,
                    COUNT(DISTINCT ia.platform_name) AS num_platforms_available,
                    COUNT(DISTINCT p.streamer_uid) AS num_streamers_playing,
                    vg.sales
                FROM 
                    Video_game vg
                LEFT JOIN 
                    Is_Available ia ON vg.game_id = ia.game_id
                LEFT JOIN 
                    Plays p ON vg.game_id = p.game_id
                GROUP BY 
                    vg.game_id, vg.title, vg.sales
                ORDER BY
                    vg.sales DESC
                LIMIT 100000
                '''
            else:
                errorInstance = error_return_type.ErrorReturnType(error_message="Invalid sort by value")
                return errorInstance
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()
            result.insert(0, ("Game id" , "Title", "# of platforms available", "# of streamers playing", "Sales"))
            return result
        except mysql.connector.errors.Error as err:
            errorInstance = error_return_type.ErrorReturnType(error_message=f"Database error. Message detail : \n{err.msg}")
            return errorInstance