import urwid
top = None

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative',100),
            valign='middle', height=('relative', 100),
            min_width=24, min_height=8,
            left=self.box_level * 0,
            right=(self.max_box_levels - self.box_level - 1) * 0,
            top=self.box_level * 0,
            bottom=(self.max_box_levels - self.box_level - 1) * 0)
        self.box_level += 1
    def execute_command(self):
        edit = urwid.Edit(u"execute command")
        fill = InputBox(edit,column_name,pkeys,table)
        self.open_box(fill)
        

    def keypress(self, size, key):
        if key == "ctrl r":
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
            edit = urwid.Edit(u"Enter command \r\n")
            fill = ExecBox(edit)
            top.open_box(fill)
        elif key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

def get_top(m=None):
    global top
    if top == None:
       if m!=None:
           top = CascadingBoxes(m)
    return top
