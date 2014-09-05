
import urwid, MySQLdb, sys, re
from connection import *
import layer
from  huisqlBase import *

class row_n_cells_menu_generator(base_huisql_item):
    def __init__(self,name):
        self.name = name
        self.columns = self.get_columns()

    def click_callback(self,button,*args):
        edit = urwid.Edit(u"Enter new value for "+column_name+" with keys "+str(pkeys)+" \n",button.label)
        fill = InputBox(edit,column_name,pkeys,table)
        layer.get_top().open_box(fill)

	def cell_menu_button(self,caption, callback,column_name):
		button = urwid.Button(caption.decode('utf8'))
		urwid.connect_signal(button, 'click', callback,column_name)
		return urwid.AttrMap(button, None, focus_map='reversed')

    def columns_menu_button(row,columns,pkeys,table):
		button = urwid.Columns([self.cell_menu_button(str(i),click,str(columns[k])) for (k,i) in enumerate(row)])
		return urwid.AttrMap(button, None, focus_map='reversed')
        
    def __call__(self):
        return self.columns_button()
