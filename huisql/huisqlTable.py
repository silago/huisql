import urwid, MySQLdb, sys, re
from connection import *
import layer
from  huisqlBase import *
from huisqlRow import row_n_cells_menu_generator

class table_menu_generator(base_huisql_item):
    def __init__(self,name):
        self.name = name
        self.columns = self.get_columns()

    def get_columns(self):
        CURSOR.execute("SHOW COLUMNS from `"+self.name+"` ;");
        self.columns = CURSOR.fetchall()
        self.pkeys= [(str(i[0])) for i in self.columns if "PRI" in i]
        self.columns = [str(i[0]) for i in self.columns] 

    def click_callback(self,button,*args):
        if not self.columns: self.get_columns()
        " here row genarator shall be called instead of dirty sql executing "
        CURSOR.execute("select *  from "+self.name+";");
        data = self.menu(self.name,[row_n_cells_menu_generator(i,self.columns,{i2:str(i[self.columns.index(i2)])  for i2 in self.pkeys  },self.name) \
             for (i) in (CURSOR.fetchall())],headers=self.columns)

        return layer.get_top().open_box(data)

    def table_menu_button(self):
        button = urwid.Button(self.name)
        urwid.connect_signal(button, 'click', self.click_callback)
        return urwid.AttrMap(button, None, focus_map='reversed')
        
    def __call__(self):
        return self.table_menu_button()
