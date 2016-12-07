__author__ = 'Geoff'
from Tkinter import StringVar
import Tkinter as tk   # python
import ttk
import time

# this is a test

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.maxsize(480,320);
        self.minsize(480,320);


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            # frame.configure(background = 'black')
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("StartPage")
        self.update_idletasks()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        self.update_idletasks()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.time_var = StringVar()

        label = tk.Label(self, textvariable=self.time_var, font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"), foreground="black", background="grey")
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"), foreground="black", background="grey")
        button1.pack()
        button2.pack()

        self.update_time()

    def update_time(self):
        self.time_var.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.update_time)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Alarm", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose Music", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        controller.after(200, controller.show_frame("StartPage"))

def print_log():
    print "1 second"

# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         self.after(1000, tk.Frame.__init__(self, parent))
#         self.controller = controller
#         time_var = StringVar()
#         time_var.set(time.strftime("%H:%M:%S"))
#         label = tk.Label(parent, textvariable=time_var, font=TITLE_FONT)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage"))
#         button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()