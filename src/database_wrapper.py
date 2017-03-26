import psycopg2

class DatabaseWrapper:
  def __init__(self, database_name="", database_host=""):
    self.database_name = database_name
    self.database_host = database_host

  def connect(self):
    try:
        self.db_connection  = psycopg2.connect("dbname='" + self.database_name + "' host='" + self.database_host + "'")
        self.db_cursor = self.db_connection.cursor()
        return True
    except:
        
        return False