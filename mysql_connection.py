import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.cv5n2at5qukz.ap-northeast-2.rds.amazonaws.com',
        database = 'recipe_Db',
        user = 'recipe_user',
        password = 'recipe1234'
    )
    return connection