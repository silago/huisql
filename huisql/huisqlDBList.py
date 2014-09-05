from  huisqlBase import *
from huisqlTable import table_menu_generator
from connection import *
import urwid, MySQLdb, sys, re
import layer

class database_menu_generator(base_huisql_item):
    def __init__(self):
        base_huisql_item()
        " it have no parent "
        " have to execute 'show tables;' "
        " have to generate buttons "
        " have to put buttons to menu "
        " have to return generated menu, finally "
        " --- --- --- "
        " therefore parent class have to know how to generate menu "

    def click_callback(self,button,*args):
        caption = args[0][0]
        DB.select_db(caption)
        CURSOR.execute("show tables;")
        data = self.menu(caption,[table_menu_generator(i[0])() for i in CURSOR.fetchall()])
        return layer.get_top().open_box(data)

    def db_menu_button(self,caption):
        return self.base_menu_button([caption], self.click_callback,caption)
    
    def __call__(self):
        CURSOR.execute("SHOW DATABASES;")
        data = [self.db_menu_button(i[0]) for i in CURSOR.fetchall()]
        return self.menu('databases',data)
