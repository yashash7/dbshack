import mysql.connector as my
class database():
    def __init__(self):
        self.__host = "bmm9nmdc8jkviblsmk1v-mysql.services.clever-cloud.com"
        self.__database="bmm9nmdc8jkviblsmk1v"
        self.__user="ul8a9buow3kovfwl"
        self.__password="T5fBv04lvFp9hBV9W70b"
        self.conn = my.connect(host = self.__host, database = self.__database, user = self.__user, password = self.__password)
        self.cursor =self.conn.cursor()
    def get_user(self):
        stat = "select username, password from dbsusers"
        self.cursor.execute(stat)
        res = self.cursor.fetchall()
        return res