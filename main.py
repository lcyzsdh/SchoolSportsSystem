import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

uname =''
nowkq =''

# 注册窗口
class RegisterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 500
        y = 400
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.overrideredirect(True)
        self.resizable(width=False, height=False)
        self.ini_ui()

    def ini_ui(self):

        def quxiao():
            self.destroy()

        def zhuce():
            with open('./db/users.txt', 'a') as f:
                if enmm.get() == enrmm.get():
                    f.write("%s\n%s\n" % (enzh.get(), enmm.get()))
                    f.close()
                    tk.messagebox.showinfo('欢迎', '注册成功')
                    self.destroy()
                else:
                    tk.messagebox.showerror('错误', '请重新输入密码')

        lzh = tk.Label(self, text='新账号', font=('宋体', 18))
        lmm = tk.Label(self, text='新密码', font=('宋体', 18))
        lrmm = tk.Label(self, text='确认密码', font=('宋体', 18))
        enzh = tk.Entry(self, show=None, font=('宋体', 18))
        enmm = tk.Entry(self, show='*', font=('宋体', 18))
        enrmm = tk.Entry(self, show='*', font=('宋体', 18))
        enzh.focus()
        bzhuce = tk.Button(self, text='注册', font=('宋体', 12), width=10, height=1, command=zhuce)
        bquxiao = tk.Button(self, text='取消', font=('宋体', 12), width=10, height=1, command=quxiao)
        bzhuce.place(x=70, y=350)
        bquxiao.place(x=300, y=350)
        enzh.place(x=150, y=53)
        enmm.place(x=150, y=153)
        enrmm.place(x=150, y=253)
        lzh.place(x=40, y=50)
        lmm.place(x=40, y=150)
        lrmm.place(x=40, y=250)
        self.mainloop()


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
                    if t % 2 == 1:
                        zh = line
                    elif t % 2 == 0:
                        mm = line
                        if ezh.get() == zh and emm.get() == mm:
                            self.destroy()
                            global uname
                            uname = zh
                            mainwindow = MainWindow()
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
        self.geometry("650x600")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        classes = 0  # 总班级数
        alllength = 0
        classloc = []  # 班级开始的行数
        p1=0
        p2=0
        kqname='we'
        fi = open('./db/'+uname+'/classes.txt', 'r')
        allf = fi.readlines()
        for t in allf:
            alllength += 1
            if t[0] == '#':
                classes += 1
                classloc.append(alllength)
        def opfile():
            oplc = filedialog.askopenfilename()
            allname = []
            with open(oplc, 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    allname.append(line)
                f.close()
            for i in allname:
                stlist.insert('end', i)
            with open('./db/' + uname + '/classes.txt', 'a') as fi:
                fi.write('#%s\n' % classes)
                for words in allname:
                    fi.write("%s\n" % words)

        def leadclass():
            nowclass= chcl.get('active')
            banji = int(nowclass[2])
            p1=classloc[banji-1]
            p2=classloc[banji]
            for tem in allf[p1:p2-1]:
                stlist.insert('end',tem)

        def joinqq():
            nowstu=stlist.get('active')
            qqlist.insert('end',nowstu)

        def kqok():
            qqstu=qqlist.get(0,'end')
            print(qqstu)
            for st in qqstu:
                qqfile = open('./db/'+uname+'/'+kqname+'.txt','w')
                qqfile.write(st)


        stlist = tk.Listbox(self,height=40)
        stlist.place(x=390, y=50)

        qqlist =tk.Listbox(self,height=40)
        qqlist.place(x=200,y=250)

        drbutton = tk.Button(self, text='导入学生名单', font=('黑体', 10), width =10,height= 1,command=opfile)
        drbutton.place(x=500,y =500)

        chcl = tk.Listbox(self, height=12)
        for i in range(1, classes+1):
            chcl.insert('end', '班级' + str(i))
        chcl.place(x=90, y=50)

        chclb =tk.Button(self, text='选择班级>>>', width=10,height=1,command=leadclass)
        chclb.place(x=100,y=200)

        qqstb = tk.Button(self, text ='加入缺勤名单',width=10,height=1,command=joinqq)
        qqstb.place(x=200,y=300)

        saveb = tk.Button(self,text = '完成考勤',width=10,height=1,command=kqok)
        saveb.place(x=300,y=200)

# 考勤内容选择窗口
class KqChoose(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('考勤内容选择')
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 250
        y = 320
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.resizable(width=False, height=False)
        self.overrideredirect(True)
        self.ini_ui()
    def ini_ui(self):
        sb =tk.Scrollbar(self,orient='vertical')
        sb.pack(side=tk.RIGHT,fill=tk.Y)
        nrlist =tk.Listbox(self,height=6,width=20)
        nrlist.place(x=10,y=50)
        knf = open('./db/'+uname+'/kqnr.txt', 'r+')
        alln=knf.readlines()
        for n in alln:
            nrlist.insert('end',n)
        nrlist.config(yscrollcommand=sb.set)
        sb.config(command=nrlist.yview,width=16)

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
            self.destroy()
            KqChoose().mainloop()

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
        tjbutton = tk.Button(self, text='学生管理统计', font=('黑体', 16), width=20, height=3)
        tjbutton.place(x=20, y=270)

        tcbutton = tk.Button(self, text='退出', font=('黑体', 10), width=10, height=2, command=mainquit)
        tcbutton.place(x=200, y=355)


if __name__ == "__main__":

    SignWindow().mainloop()
