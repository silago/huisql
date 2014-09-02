import urwid, MySQLdb, sys, re

class _proto_base_huisql_item_factory():
    def __init__(self):
        pass
    
    def click_callback(self):
        pass

    def base_menu_button(self,caption, callback,*args):
        button = urwid.Button(caption)
        urwid.connect_signal(button, 'click', callback,args)
        return urwid.AttrMap(button, None, focus_map='reversed')
    
    
    def menu(self, title, choices,**kwargs):
        body = [urwid.Text(title), urwid.Divider()]
        for arg in kwargs:
            c_list = urwid.Columns([urwid.Text(i) for i in kwargs[arg]])
            body = body + [c_list,urwid.Divider(),]
        body.extend(choices)
        return urwid.ListBox(urwid.SimpleFocusListWalker(body))

class base_huisql_item(_proto_base_huisql_item_factory):
    def __init__(self):
        _proto_base_huisql_item_factory.__init__(self)
