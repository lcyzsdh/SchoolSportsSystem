import csv
import sqlite3 as sq
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

uname = ''
nowkq = ''
usco = sq.connect('./db/test.db')
cur = usco.cursor()
cur.execute("create table if not exists login (id varchar(20) primary key, name varchar(30), password "
            "varchar(30))")
cur.execute("insert into login (name, password) values (?,?)", ("1", "1"))  # 最后删除
cur.execute("insert into login (name, password) values (?,?)", ("admin", "admin"))


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
        enzh = tk.Entry(self, show=None, font=('宋体', 18))
        enmm = tk.Entry(self, show='*', font=('宋体', 18))
        enrmm = tk.Entry(self, show='*', font=('宋体', 18))
        enzh.focus()
        enzh.place(x=150, y=53)
        enmm.place(x=150, y=153)
        enrmm.place(x=150, y=253)

        def quxiao():
            self.destroy()

        def zhuce():

            if enmm.get() == enrmm.get():
                zh = enzh.get()
                mm = enmm.get()
                print(zh, mm)
                global cur
                cur.execute("insert into login (name, password) values (?,?)", (zh, mm))
                tk.messagebox.showinfo('欢迎', '注册成功')
                self.destroy()
            else:
                tk.messagebox.showerror('错误', '请重新输入密码')

        lzh = tk.Label(self, text='新账号', font=('宋体', 18))
        lmm = tk.Label(self, text='新密码', font=('宋体', 18))
        lrmm = tk.Label(self, text='确认密码', font=('宋体', 18))

        bzhuce = tk.Button(self, text='注册', font=('宋体', 12), width=10, height=1, command=zhuce)
        bquxiao = tk.Button(self, text='取消', font=('宋体', 12), width=10, height=1, command=quxiao)
        bzhuce.place(x=70, y=350)
        bquxiao.place(x=300, y=350)

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
        self.title('dd')
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.overrideredirect(True)
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        # bg = tk.PhotoImage(self,file='13331.gif')
        # bgl = tk.Label(self,image=bg)
        # bgl.place(x=10, y=10)
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
            global cur
            cur.execute('select name,password from login')
            user = cur.fetchall()
            zh = ezh.get()
            mm = emm.get()
            tup = (zh, mm)
            fd = 0
            for t in user:
                if t == tup:
                    fd = 1
                    self.destroy()
                    global uname
                    uname = zh
                    cur.close()
                    mainwindow = MainWindow()
                    mainwindow.mainloop()
            if fd == 0:
                tk.messagebox.showinfo(message='账号密码错误')
                ezh.delete(0, 'end')
                emm.delete(0, 'end')

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
        p1 = 0
        p2 = 0
        kqname = 'we'
        fi = open('./db/' + uname + '/classes.txt', 'r')
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
            nowclass = chcl.get('active')
            banji = int(nowclass[2])
            p1 = classloc[banji - 1]
            p2 = classloc[banji]
            for tem in allf[p1:p2 - 1]:
                stlist.insert('end', tem)

        def joinqq():
            nowstu = stlist.get('active')
            qqlist.insert('end', nowstu)

        def kqok():
            qqstu = qqlist.get(0, 'end')
            print(qqstu)
            for st in qqstu:
                qqfile = open('./db/' + uname + '/' + kqname + '.txt', 'w')
                qqfile.write(st)

        stlist = tk.Listbox(self, height=40)
        stlist.place(x=390, y=50)

        qqlist = tk.Listbox(self, height=40)
        qqlist.place(x=200, y=250)

        drbutton = tk.Button(self, text='导入学生名单', font=('黑体', 10), width=10, height=1, command=opfile)
        drbutton.place(x=500, y=500)

        chcl = tk.Listbox(self, height=12)
        for i in range(1, classes + 1):
            chcl.insert('end', '班级' + str(i))
        chcl.place(x=90, y=50)

        chclb = tk.Button(self, text='选择班级>>>', width=10, height=1, command=leadclass)
        chclb.place(x=100, y=200)

        qqstb = tk.Button(self, text='加入缺勤名单', width=10, height=1, command=joinqq)
        qqstb.place(x=200, y=300)

        saveb = tk.Button(self, text='完成考勤', width=10, height=1, command=kqok)
        saveb.place(x=300, y=200)


# 考勤内容选择窗口
class KqChoose(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('考勤内容选择')
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 200
        y = 220
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.resizable(width=False, height=False)
        self.overrideredirect(True)
        self.ini_ui()

    def ini_ui(self):
        sb = tk.Scrollbar(self, orient='vertical')
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        nrlist = tk.Listbox(self, height=8, width=25)
        nrlist.place(x=0, y=0)
        knf = open('./db/' + uname + '/kqnr.txt', 'r+')
        alln = knf.readlines()
        for n in alln:
            nrlist.insert('end', n)
        nrlist.config(yscrollcommand=sb.set)
        sb.config(command=nrlist.yview, width=16)

        def addn():
            an = newa.get()
            nrlist.insert(0, an)
            newa.delete(0, 'end')

        def enter():
            global nowkq
            nowkq = nrlist.get('active')
            self.destroy()
            KqWindow().mainloop()

        newa = tk.Entry(self, width=18)
        newa.place(x=10, y=155)
        ad = tk.Button(self, width=2, height=1, text='+', font=('Arial', 13), command=addn)
        ad.place(x=150, y=150)

        enterb = tk.Button(self, width=23, height=1, text='确定', command=enter)
        enterb.place(x=5, y=185)


# 导入新班级窗口
class DrNewClass(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('导入newc')
        self.geometry("350x200")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        def drmd():
            mdfile = filedialog.askopenfilename(filetypes=[("CSV", ".csv")])
            var.set(mdfile)

        def drquit():
            f = open(var.get(), 'r')
            fc = csv.reader(f)
            f2 = open('./db/' + uname + '/'+nmet.get()+'.csv', 'a', newline='')
            fw = csv.writer(f2)
            for row in fc:
                fw.writerow(row[0])
            f2.close()
            f3 =open('./db/' + uname + '/classlist.txt','a')
            print(nmet.get())
            f3.write(nmet.get()+'\n')
            f3.close()
            self.destroy()
            StManager().mainloop()

        crb = tk.Button(self, text='从.csv导入名单', command=drmd)
        crb.place(x=30, y=20)
        var = tk.StringVar(self)
        var.set("请选择班级")
        locl = tk.Label(self,textvariable=var)
        locl.place(x=10,y=10)
        nmet =tk.Entry(self, show=None, font=('宋体', 18))
        nmet.place(x=20,y=30)
        qdb= tk.Button(self,text='que ding',command=drquit)
        qdb.place(x=90,y=40)


# 学生管理窗口
class StManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('学生管理')
        self.geometry("650x600")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        def drnc():
            self.destroy()
            DrNewClass().mainloop()

        def ok():
            nmli.delete(0,'end')
            f2 = open('./db/' + uname + '/' + chcl.get() + '.csv', 'r',encoding='utf-8')
            fw = csv.reader(f2)
            for row in fw:
                nmli.insert('end', row[0])

        nmlabel = tk.Label(self, text='welcome' + uname)
        nmlabel.place(x=10, y=10)
        crbj = tk.Button(self, text='导入新班级', command=drnc)
        crbj.place(x=80, y=10)
        allcl = []
        with open('./db/' + uname + '/classlist.txt','r') as f:
            for row in f.readlines():
                trow =row.replace('\n','')
                allcl.append(trow)
        chcl = ttk.Combobox(self, values=allcl)
        chcl.place(x=200, y=400)
        nmli = tk.Listbox(self, height=20)
        nmli.place(x=40, y=60)
        nmlisb = tk.Scrollbar(self)
        nmli.config(yscrollcommand=nmlisb.set)
        nmlisb.config(command=nmli.yview, width=16)
        nmlisb.pack(side=tk.RIGHT, fill=tk.Y)
        qd = tk.Button(self, text='班级选择预览', command=ok)
        qd.place(x=300, y=200)


# 学生导出窗口
class StWatcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('学生管理')
        self.geometry("650x600")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        def ok():
            nmli.delete(0, 'end')
            f2 = open('./db/' + uname + '/' + chcl.get() + '.csv', 'r', encoding='utf-8')
            fw = csv.reader(f2)
            for row in fw:
                nmli.insert('end', row[0])

        nmlabel = tk.Label(self, text='welcome' + uname)
        nmlabel.place(x=10, y=10)
        ifl =tk.Label(self,'shuang ji cha kan')
        allcl = []
        with open('./db/' + uname + '/classlist.txt', 'r') as f:
            for row in f.readlines():
                trow = row.replace('\n', '')
                allcl.append(trow)
        chcl = ttk.Combobox(self, values=allcl)
        chcl.place(x=200, y=400)
        nmli = tk.Listbox(self, height=20)
        nmli.place(x=40, y=60)
        nmlisb = tk.Scrollbar(self)
        nmli.config(yscrollcommand=nmlisb.set)
        nmlisb.config(command=nmli.yview, width=16)
        nmlisb.pack(side=tk.RIGHT, fill=tk.Y)
        qd = tk.Button(self, text='班级选择预览', command=ok)
        qd.place(x=300, y=200)


# 主窗口
class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("学生体育考勤管理系统")
        self.geometry("680x405")
        self.resizable(width=False, height=False)
        self.ini_ui()

    def ini_ui(self):
        toplabel = tk.Label(self, text="学 生 体 育 统 计 系 统", font=('黑体', 16))
        toplabel.place(x=10, y=15)

        global uname
        namelabel = tk.Label(self, text='欢迎' + uname + "使用本系统", font=('黑体', 10))
        namelabel.place(x=30, y=360)

        def mainquit():
            self.destroy()

        def opkqwindow():
            self.destroy()
            KqChoose().mainloop()

        def opstmnwindow():
            self.destroy()
            StManager().mainloop()

        def opstdcwindow():
            self.destroy()
            StWatcher().mainloop()

        mainmenu = tk.Menu(self)
        helpmenu = tk.Menu(mainmenu, tearoff=0)
        mainmenu.add_cascade(label='帮助', menu=helpmenu)
        helpmenu.add_command(label="帮助文件....", )
        helpmenu.add_command(label='退出', command=mainquit)
        self.config(menu=mainmenu)

        kqbutton = tk.Button(self, text='学生体育考勤', font=('黑体', 16), width=20, height=3, command=opkqwindow)
        kqbutton.place(x=20, y=70)
        ckbutton = tk.Button(self, text='导出学生成绩', font=('黑体', 16), width=20, height=3, command=opstdcwindow)
        ckbutton.place(x=20, y=170)
        tjbutton = tk.Button(self, text='学生管理导入', font=('黑体', 16), width=20, height=3, command=opstmnwindow)
        tjbutton.place(x=20, y=270)

        tcbutton = tk.Button(self, text='退出系统', font=('微软雅黑', 8), width=8, height=1, command=mainquit)
        tcbutton.place(x=200, y=358)

        tpl = tk.Label(self)
        tpl.pack()


if __name__ == "__main__":
    SignWindow().mainloop()
