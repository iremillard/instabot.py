import psycopg2
from time import gmtime, strftime

class DatabaseWrapper:

  def __init__(self, database_name="", database_host=""):
    self.database_name = database_name
    self.database_host = database_host
    self.is_connected = False

  def connect(self):
    try:
        self.db_connection = psycopg2.connect("dbname='" + self.database_name + "' host='" + self.database_host + "'")
        self.db_cursor = self.db_connection.cursor()
        self.is_connected = True
        return True
    except:
        return False

  def add_follow_record(self, user_id, is_following_user_id):
    if self.is_connected:
      self.db_cursor.execute("INSERT INTO follow_records (user_id, is_following_id, followed_at) VALUES ('%s', '%s', '%s')" % (user_id, is_following_user_id, strftime("%Y%m%d %H:%M:%S", gmtime())))
      self.db_connection.commit()
    else:
      raise Exception('database_wrapper not connected!')

  #def add_unfollow_record(self, user_id, unfollowed_user):

  def check_if_ever_followed(self, user_id, is_following_user_id):
    if self.is_connected:
      self.db_cursor.execute("SELECT id FROM follow_records WHERE user_id ='%s' AND is_following_id='%s'" % (user_id, is_following_user_id))
      return len(self.db_cursor.fetchall()) > 0
    else:
      raise Exception('database_wrapper not connected!')