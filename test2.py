#!/usr/bin/env python

__author__ = 'Geoff'
from Tkinter import StringVar
import Tkinter as tk   # python
import ttk
import time

# this is a test

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Frame):
    """The container frame"""

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self)
            # frame.configure(background = 'black')
            self.frames[F] = frame #we may as well use the class itself as the key, instead of the name

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        #update_idletasks() should be needed very rarely

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# button attributes. It's good to put things like this in a single place
# so that it's easy to change all the buttons at once
opt = {"foreground": "black", "background":"grey"}

class StartPage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #tkinter automatically assigns parent to "self.master"

        self.time_var = StringVar()

        label = tk.Label(self, textvariable=self.time_var, font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One", **opt)
        button1.config(command=lambda: parent.show_frame(PageOne)) #same thing as yours, just neater (in my opinion)
        button1.pack()

        button2 = tk.Button(self, text="Go to Page Two", **opt)
        button2.config(command=lambda: parent.show_frame(PageTwo))
        button2.pack()

        self.update_time()

    def update_time(self):
        self.time_var.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.update_time)

class PageOne(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Alarm", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page")
        button.config(command=lambda: parent.show_frame(StartPage))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose Music", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page")
        button.config(command=lambda: parent.show_frame(StartPage))
        button.pack()

        # what was the point of this? It's useless.
        # controller.after(200, controller.show_frame("StartPage"))


def print_log():
    print "1 second"

def main():
    # this could be a class but in general we try not to use classes when a function will do
    root = tk.Tk()
    app = SampleApp(root)
    app.pack(side="top", fill="both", expand=True)
    root.geometry("480x320")
    root.resizable(0, 0)
    root.mainloop()

if __name__ == "__main__":
    main()
