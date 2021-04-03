import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("学生体育统计系统")
        self.geometry("1080x600")
        self.ini_ui()

    def ini_ui(self):


        toplabel = tk.Label(self, text="学 生 体 育 统 计 系 统", font=('楷体', 24))
        toplabel.pack()

        mainmenu = tk.Menu(self)
        helpmenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label='帮助', menu=helpmenu)
        helpmenu.add_command(label="帮助文件....")
        helpmenu.add_command(label='退出')
        self.config(menu=mainmenu)

        tasklist = tk.Menubutton(self, text='考情内容选择',relief='raised')
        kqmenu = tk.Menu(tasklist,tearoff=0)
        kqmenu.add_command(label='出操')
        tasklist.pack()
        tasklist.config(menu=kqmenu)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
