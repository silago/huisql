import urwid, MySQLdb, sys, re

class InputBox(urwid.Filler):
    def __init__(self,edit,column,pkeys,table):
        self.column = column
        self.pkeys   = pkeys
        self.table   = table
        self.edit    = edit
        urwid.Filler.__init__(self,self.edit)
    
    def update_command(self):
	#where = "true";
	#for (k,v) in self.pkeys.iteritems():
	#    where = where+' and '+k+' = "'+v+'"'
	#CURSOR.execute('update '+self.table+' set '+self.column+'= "'+self.edit.edit_text+'" where '+where+";")
	#DB.commit()
	pass
    
    
    def keypress(self, size, key):
        if key != 'esc':
            if key != 'enter':
                return super(InputBox, self).keypress(size, key)
            self.update_command()
            top.original_widget = top.original_widget[0]
            top.original_widget = top.original_widget[0]
            top.box_level -= 1
        else: pass 



