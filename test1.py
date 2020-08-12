import tkinter as tk
from PIL import ImageTk, Image
import os
import types

if os.name == 'nt':
    import ctypes
    import winsound

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    windows = True


class Notification(tk.Tk):

    '''

    A class that simulates Toast Notification

    ---------------------------------------------------------

    `icon_path string specifying is path to the icon to be displayed .ico files are not recommended as images. The image will be resized to a
    smaller image of 1:1 ratio

    `param buttons is a list of tuples containing 2 elements
        [0] element is text to be displayed on button
        [1] element is function to be called on click

    `param timeout is in seconds
    '''

    def __init__(self, title, message, icon_path=None, buttons=[], timeout=5) -> 'window':
        super().__init__()
        self.bg = '#282828'
        self.fg = '#fafafa'

        self.resizable(False, False)#Window cannot be scaled
        self.overrideredirect(1)#Don't show the titlebar
        self.config(bg=self.bg)
        self.lift()#show window on top of all windows
        self.after(timeout * 1000, self.destroy)#close after timeout seconds

        self.close_button()
        self.frame_notif = tk.Frame(bg=self.bg)
        self.frame_notif.pack(pady=(1, 20))

        self.set_icon(icon_path)
        self.content(title, message)
        self.action_buttons(buttons)

    def close_button(self):
        self.close = tk.Button(text='➔', command=self.close, relief='flat', bg=self.bg,
                               fg=self.fg, activebackground=self.bg, activeforeground=self.fg, justify='right')

        self.close.pack(anchor='ne', ipadx=16)

        self.bind('<Button-1>', self.callback)

    def set_icon(self, icon_path):
        if icon_path:
            # if os.path.exists(icon_path):
            try:
                self.img = Image.open(icon_path).resize(
                    (64, 64), Image.ANTIALIAS)
            except (OSError, PermissionError):
                raise TypeError(
                    'The image could not be read. Make sure the provided path is to an image')
            self.img = ImageTk.PhotoImage(self.img)
            self.icon = tk.Label(self.frame_notif, image=self.img, bg=self.bg)
            self.icon.pack(side=tk.LEFT, anchor='nw', ipadx=1)

    def content(self, title, message):
        if not isinstance(title, str):
            raise TypeError('Provided title is not a string')
        if not isinstance(message, str):
            raise TypeError('Provided message is not a string')
        self.frame_text = tk.Frame(self.frame_notif, width=24, bg=self.bg)
        self.frame_text.pack(anchor='e')

        if title:

            self.title = tk.Label(self.frame_text, text=title, font=(
                'Verdana', 14, 'bold'), bg=self.bg, fg=self.fg)
            self.title.pack(padx=9, pady=2, anchor='w')

        self.label = tk.Label(self.frame_text, text=f"{message}", width=30, font=(
            'Verdana', 12), wraplength=400, bg=self.bg, fg=self.fg, justify='left')
        self.label.pack(pady=2, anchor='w')

    def action_buttons(self, buttons):

        if buttons:

            self.update()
            width = self.winfo_width()
            self.frame_button = tk.Frame(self, bg=self.bg, width=width)
            self.frame_button.pack(padx=3, pady=1)

            len_buttons = len(buttons)

            button_kwg = {'width': width // (len_buttons * 11), 'font': ('Verdana', 10), 'height': 2,
                          'fg': self.fg, 'bg': "#444", 'activebackground': "#666", 'activeforeground': self.fg, 'relief': 'flat'}

            for pair in buttons:
                if type(pair[1]) == types.FunctionType:
                    button = tk.Button(self.frame_button,
                                       text=str(pair[0]), command=pair[1], **button_kwg)
                else:
                    raise TypeError(f'{pair[1]} is not a function')
                button.grid(column=buttons.index(pair), row=0, pady=2)
                button.bind('<Leave>', self.on_exit)
                button.bind('<Enter>', self.on_enter)

    def notify(self):
        self.geometry('-8-57')#show window on bottom-right corner
        self.mainloop()

    def callback(self, event):
        if type(event.widget) == tk.Button:
            event.widget.config(relief='flat')#Don't depress button on press

    def on_enter(self, event):
        event.widget.config(bg='#666')

    def on_exit(self, event):
        event.widget.config(bg='#444')

    def close(self):
        self.destroy()



if __name__ == '__main__':
    
    def ok():
        print('ok')


    def cancel():
        print('cancel')


    def close():
        print('close')

    v = Notification('Title', 'This is dummy message used for development. If you are seeing this please go to the python module and delete 126th line. Thank you!',
                     'Battery\\battery.ico', [
                         ('OK', ok), ('Cancel', cancel), ('Close', close)])
    v.notify()
