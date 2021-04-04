import tkinter as tk
from tkinter import messagebox

class SignWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 500
        y = 200
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.overrideredirect(True)
        self.resizable(width=False, height=False)
        self.ini_ui()

    def ini_ui(self):
        lzh = tk.Label(self, text='账号', font=('宋体', 18))
        lzh.place(x=30, y=40)
        lmm = tk.Label(self, text='密码', font=('宋体', 18))
        lmm.place(x=30, y=90)
        ezh = tk.Entry(self, show=None, font=('宋体', 18))
        ezh.place(x=130, y=43)
        ezh.focus()
        emm = tk.Entry(self, show='*', font=('宋体', 18))
        emm.place(x=130, y=93)

        def signcanel():
            self.destroy()

        def signtowindow():
            with open("./db/users.txt","r") as f:
                t = 0
                zh = ''
                mm = ''
                length = 0
                for line in f.readlines():
                    length = length + 1
                f.close()
            with open("./db/users.txt", "r") as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    t = t+1
                    if t % 2 == 1:
                        zh = line
                    elif t % 2 == 0:
                        mm = line
                        if ezh.get() == zh and emm.get() == mm:
                            self.destroy()
                            mainwindow = MainWindow()
                            mainwindow.mainloop()
                        else:
                            if t == length:
                                zhwrong = tk.messagebox.showinfo(message='账号密码错误')
                        zh = ''
                        mm = ''

        bcancel = tk.Button(self, text='取消', font=('宋体', 12), width=10, height=1, command=signcanel)
        bsign = tk.Button(self, text='登录', font=('宋体', 12), width=10, height=1, command=signtowindow)
        brg = tk.Button(self, text='注册', font=('宋体', 12), width=10, height=1)
        bcancel.place(x=330, y=150)
        bsign.place(x=200, y=150)
        brg.place(x=70, y=150)


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

        tasklist = tk.Menubutton(self, text='考情内容选择', relief='raised')
        kqmenu = tk.Menu(tasklist,tearoff=0)
        kqmenu.add_command(label='出操')
        tasklist.pack()
        tasklist.config(menu=kqmenu)


if __name__ == "__main__":
    signwindow= SignWindow()
    signwindow.mainloop()
