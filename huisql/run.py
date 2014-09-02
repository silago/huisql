# -*- coding: utf-8 -*-
import urwid, MySQLdb, sys, re
from huisqlDBList import database_menu_generator 
from UrwidItems import *
import layer
from connection import *



 



def get_table_columns_and_pkeys(caption):
    CURSOR.execute("SHOW COLUMNS from "+caption+";");
    columns = CURSOR.fetchall()
    pkeys= [(str(i[0])) for i in columns if "PRI" in i]
    columns = [str(i[0]) for i in columns] 
    return [columns,pkeys]


class ExecBox(urwid.Filler):
    def __init__(self,edit):
        self.edit = edit
        urwid.Filler.__init__(self,self.edit)
    def table_rows_menu(self,caption,query):
        table_data = get_table_columns_and_pkeys(caption)
        CURSOR.execute(query)
        data = base_menu(caption,[row_cells(i,table_data[0],{i2:str(i[table_data[0].index(i2)])  for i2 in table_data[1]  },caption) for (i) in (CURSOR.fetchall())],headers=table_data[0])
        return top.open_box(data)
    def command(self):
        CURSOR.execute(self.edit.edit_text)
        db.commit()
        data = CURSOR.fetchall()
    def keypress(self, size, key):
        if key != 'esc':
            if key != 'enter':
                return super(ExecBox, self).keypress(size, key)
            q = self.edit.edit_text
            match = re.search('\S+',q)
            match = match.group(0).lower()
            if match == 'select':
                table_name = re.search('(?<=from )[^ ;]+',q,re.I)
                table_name = table_name.group(0)
                self.table_rows_menu(table_name,q)            
            elif match == 'show':
                pass
            elif match == 'delete':
                pass
            elif match == 'update':
                pass
            else:
                pass

class InputBox(urwid.Filler):
    def __init__(self,edit,column,pkeys,table):
        self.column = column
        self.pkeys   = pkeys
        self.table   = table
        self.edit    = edit
        urwid.Filler.__init__(self,self.edit)
    
    def update_command(self):
        where = "true";
        for (k,v) in self.pkeys.iteritems():
            where = where+' and '+k+' = "'+v+'"'
        CURSOR.execute('update '+self.table+' set '+self.column+'= "'+self.edit.edit_text+'" where '+where+";")
        DB.commit()
    
    
    def keypress(self, size, key):
        if key != 'esc':
            if key != 'enter':
                return super(InputBox, self).keypress(size, key)
            self.update_command()
            top.original_widget = top.original_widget[0]
            top.original_widget = top.original_widget[0]
            top.box_level -= 1
        else: pass 

def row_button(caption, callback,column_name):
    button = urwid.Button(caption.decode('utf8'))
    urwid.connect_signal(button, 'click', callback,column_name)
    return urwid.AttrMap(button, None, focus_map='reversed')

def row_cells(row,columns,pkeys,table):
    def click(button,column_name):
        edit = urwid.Edit(u"Enter new value for "+column_name+" with keys "+str(pkeys)+" \n",button.label)
        fill = InputBox(edit,column_name,pkeys,table)
        top.open_box(fill)
    button = urwid.Columns([row_button(str(i),click,str(columns[k])) for (k,i) in enumerate(row)])
    return urwid.AttrMap(button, None, focus_map='reversed')








def item_chosen(button):
    response = urwid.Text([u'You chose ', button.label, u'\n'])
    done = menu_button(u'Ok', exit_program)
    top.open_box(urwid.Filler(urwid.Pile([response, done])))



def exit_program(button):
    raise urwid.ExitMainLoop()


if __name__=="__main__":
    top = layer.get_top(database_menu_generator()())
    urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
