import MySQLdb


DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_DB   = ""
DB_CHARSET = "utf8"
DB = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS)
#CURSOR = DB.cursor(cursorclass=MySQLdb.cursors.DictCursor)
CURSOR = DB.cursor()

