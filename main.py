import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# 注册窗口
class RegisterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 500
        y = 200
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.resizable(width=False, height=False)
        self.title('学生体育考勤管理系统注册')
        self.init_ui()

    def init_ui(self):
        b1 = tk.Button()


# 登录窗口
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
        self.init_ui()

    def init_ui(self):
        lzh = tk.Label(self, text='账号', font=('黑体', 22))
        lzh.place(x=30, y=40)
        lmm = tk.Label(self, text='密码', font=('黑体', 22))
        lmm.place(x=30, y=90)
        ezh = tk.Entry(self, show=None, font=('黑体', 22))
        ezh.place(x=130, y=43)
        ezh.focus()
        emm = tk.Entry(self, show='*', font=('黑体', 22))
        emm.place(x=130, y=93)

        def signcanel():
            self.destroy()

        def signtowindow():
            with open("./db/users.txt", "r") as f:
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
                    t = t + 1
                    if t % 3 == 1:
                        zh = line
                    elif t % 3 == 2:
                        mm = line
                    elif t % 3 == 0:
                        if ezh.get() == zh and emm.get() == mm:
                            self.destroy()
                            mainwindow = MainWindow()
                            mainwindow.nm = line
                            mainwindow.mainloop()
                            f.close()
                        else:
                            if t == length:
                                zhwrong = tk.messagebox.showinfo(message='账号密码错误')
                                ezh.delete(0, 'end')
                                emm.delete(0, 'end')
                        zh = ''
                        mm = ''

        def registerwindow():
            rgwindow = RegisterWindow()
            rgwindow.mainloop()

        bcancel = tk.Button(self, text='取消', font=('黑体', 16), width=10, height=1, command=signcanel)
        bsign = tk.Button(self, text='登录', font=('黑体', 16), width=10, height=1, command=signtowindow)
        brg = tk.Button(self, text='注册', font=('黑体', 16), width=10, height=1, command=registerwindow)
        bcancel.place(x=330, y=150)
        bsign.place(x=200, y=150)
        brg.place(x=70, y=150)


# 考勤窗口
class KqWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('体育考勤')
        self.geometry("1050x600")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        stlist = tk.Listbox(self, height=50)
        stlist.place(x=40, y=60)

        def opfile():
            oplc = filedialog.askopenfilename()
            allname = []
            with open(oplc, 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    allname.append(line)
            print(allname)

        drbutton = tk.Button(self, text='daoru' ,font=('黑体', 16), width =10,height= 2,command=opfile)
        drbutton.place(x=100,y =200)


# 主窗口
class MainWindow(tk.Tk):
    nm = ''

    def __init__(self):
        super().__init__()
        self.title("学生体育考勤管理系统")
        self.geometry("280x400")
        self.resizable(width=False, height=False)
        self.ini_ui()

    def ini_ui(self):
        toplabel = tk.Label(self, text="学 生 体 育 统 计 系 统", font=('黑体', 16))
        toplabel.place(x=10, y=15)

        namelabel = tk.Label(self, text=self.nm, font=('黑体', 16))
        namelabel.place(x=10, y=25)

        def mainquit():
            self.destroy()

        def opkqwindow():
            KqWindow().mainloop()

        mainmenu = tk.Menu(self)
        helpmenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label='帮助', menu=helpmenu)
        helpmenu.add_command(label="帮助文件....", )
        helpmenu.add_command(label='退出', command=mainquit)
        self.config(menu=mainmenu)

        kqbutton = tk.Button(self, text='学生体育考勤', font=('黑体', 16), width=20, height=3, command=opkqwindow)
        kqbutton.place(x=20, y=70)
        ckbutton = tk.Button(self, text='导出学生成绩', font=('黑体', 16), width=20, height=3)
        ckbutton.place(x=20, y=170)
        tjbutton = tk.Button(self, text='学生数据统计', font=('黑体', 16), width=20, height=3)
        tjbutton.place(x=20, y=270)
        tcbutton = tk.Button(self, text='退出', font=('黑体', 10), width=10, height=2, command=mainquit)
        tcbutton.place(x=200, y=355)


if __name__ == "__main__":

    SignWindow().mainloop()
