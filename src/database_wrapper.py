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
    self.check_connection()
    self.db_cursor.execute("INSERT INTO follow_records (user_id, is_following_id, followed_at) VALUES ('%s', '%s', '%s')" % (user_id, is_following_user_id, strftime("%Y%m%d %H:%M:%S", gmtime())))
    self.db_connection.commit()

  def add_unfollow_record(self, user_id, unfollowed_user_id):
    self.check_connection()
    self.db_cursor.execute("UPDATE follow_records SET unfollowed_at = '%s' WHERE user_id = '%s' AND is_following_id = '%s'" % (strftime("%Y%m%d %H:%M:%S", gmtime()), user_id, unfollowed_user_id))
    self.db_connection.commit()

  def check_if_ever_followed(self, user_id, is_following_user_id):
    self.check_connection()
    self.db_cursor.execute("SELECT id FROM follow_records WHERE user_id ='%s' AND is_following_id='%s'" % (user_id, is_following_user_id))
    return len(self.db_cursor.fetchall()) > 0

  def all_currently_following(self, user_id):
    self.check_connection()
    #self.db_cursor.execute("SELECT is_following_id FROM follow_records WHERE user_id = '%s' AND unfollowed_at IS NULL" % (user_id))
    #get the oldest first
    self.db_cursor.execute("SELECT is_following_id FROM follow_records WHERE user_id = '%s' AND unfollowed_at IS NULL ORDER BY id ASC;" % (user_id))
    return list(map(lambda row: row[0], self.db_cursor.fetchall()))

  def check_connection(self):
    if not self.is_connected:
      raise Exception('database_wrapper not connected!')