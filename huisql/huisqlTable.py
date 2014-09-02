import urwid, MySQLdb, sys, re
from connection import *
class table():
    """ table 
        

    """
    def __init__(self,name):
        self.name = name
        self.columns = self.get_columns()

    def get_columns(self):
        CURSOR.execute("SHOW COLUMNS from `"+self.name+"` ;");
        self.columns = CURSOR.fetchall()
        self.pkeys= [(str(i[0])) for i in self.columns if "PRI" in i]
        self.columns = [str(i[0]) for i in self.columns] 

    def create_button(self):
        button = urwid.Button(self.name)
        urwid.connect_signal(button, 'click', self.action)
        return urwid.AttrMap(button, None, focus_map='reversed')

    def action(self,button):
        top.open_box(self.generate_children_menu())

    def generate_children_menu(self):
        if not self.columns: self.get_columns()
        " here row genarator shall be called instead of dirty sql executing "
        CURSOR.execute("select *  from "+self.name+";");
        children_menu = base_menu(self.name,[row_columns(i,self.columns,{i2:str(i[self.columns.index(i2)])  for i2 in self.pkeys  },self.name) \
             for (i) in (CURSOR.fetchall())],headers=self.columns)
        return children_menu
    def __call__(self):
        return self.create_button()
