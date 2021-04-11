import csv
import os
import sqlite3 as sq
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

uname = ''
nowkq = ''
nwcla = ''

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
        x = 480
        y = 380
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
            SignWindow().mainloop()

        def zhuce():

            if enmm.get() == enrmm.get():
                zh = enzh.get()
                mm = enmm.get()
                global cur
                cur.execute("insert into login (name, password) values (?,?)", (zh, mm))
                tk.messagebox.showinfo('欢迎', '注册成功')
                os.mkdir('./db/' + zh)
                global uname
                uname = zh
                self.destroy()
                usco.commit()
                usco.close()
                MainWindow().mainloop()
            else:
                tk.messagebox.showerror('错误', '请重新输入密码')

        lzh = tk.Label(self, text='新账号', font=('黑体', 19))
        lmm = tk.Label(self, text='新密码', font=('黑体', 19))
        lrmm = tk.Label(self, text='确认密码', font=('黑体', 17))

        bzhuce = tk.Button(self, text='注册', font=('黑体', 16), width=10, height=1, command=zhuce)
        bquxiao = tk.Button(self, text='取消', font=('黑体', 16), width=10, height=1, command=quxiao)
        bzhuce.place(x=70, y=330)
        bquxiao.place(x=300, y=330)

        lzh.place(x=40, y=50)
        lmm.place(x=40, y=150)
        lrmm.place(x=40, y=250)


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
                    usco.close()
                    mainwindow = MainWindow()
                    mainwindow.mainloop()
            if fd == 0:
                tk.messagebox.showinfo(message='账号密码错误')
                ezh.delete(0, 'end')
                emm.delete(0, 'end')

        def registerwindow():
            self.destroy()
            rgwindow = RegisterWindow()
            rgwindow.mainloop()

        bcancel = tk.Button(self, text='取消', font=('黑体', 16), width=10, height=1, command=signcanel)
        bsign = tk.Button(self, text='登录', font=('黑体', 16), width=10, height=1, command=signtowindow)
        brg = tk.Button(self, text='注册', font=('黑体', 16), width=10, height=1, command=registerwindow)
        bcancel.place(x=315, y=150)
        bsign.place(x=185, y=150)
        brg.place(x=55, y=150)


# 考勤窗口
class KqWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('体育项目考勤')
        self.geometry("530x350")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):

        def impclass():
            clnm = chcl.get()
            global nwcla
            nwcla = clnm
            f2 = open('./db/' + uname + '/' + clnm + '.csv', 'r', encoding='utf-8')
            fw = csv.reader(f2)
            for row1 in fw:
                stlist.insert('end', row1[0])

        def joinqq():
            nowstu = stlist.get('active')
            qqlist.insert('end', nowstu)

        def kqok():
            k = 0
            qqstu = qqlist.get(0, 'end')
            if qqstu:
                pass
            else:
                k = 1
            qqlist.delete(0, 'end')
            f3 = open('./db/' + uname + '/' + nwcla + '.csv', 'r', encoding='utf-8')
            f3r = csv.reader(f3)
            aline = []
            for row1 in f3r:
                aline.append(row1)
            f3.close()
            f4 = open('./db/' + uname + '/' + nwcla + '.csv', 'w', newline='', encoding='utf-8')
            f4w = csv.writer(f4)
            if k == 1:
                for r in aline:
                    t = int(r[1])
                    t += 10
                    r[1] = str(t)
                    f4w.writerow(r)
            else:
                for r in aline:
                    for nm in qqstu:
                        if r[0] == nm:
                            r[2] = r[2] + nowkq + ' '
                            f4w.writerow(r)
                            break
                        else:
                            t = int(r[1])
                            t += 10
                            r[1] = str(t)
                            f4w.writerow(r)
                            break
            f4.close()
            ask = messagebox.askokcancel('考勤完成', '要继续留在考勤界面吗？')
            if ask:
                stlist.delete(0, 'end')
                qqlist.delete(0, 'end')
            else:
                self.destroy()
                MainWindow().mainloop()

        stlist = tk.Listbox(self, height=15)
        stlist.place(x=60, y=50)

        qqlist = tk.Listbox(self, height=10)
        qqlist.place(x=350, y=50)

        allcl = []
        with open('./db/' + uname + '/classlist.txt', 'r', encoding='utf-8') as f:
            for row in f.readlines():
                trow = row.replace('\n', '')
                allcl.append(trow)
        chcl = ttk.Combobox(self, values=allcl, width=15)
        chcl.place(x=68, y=22)

        chclb = tk.Button(self, text='选择班级', font=('宋体', 10), width=8, height=1, command=impclass)
        chclb.place(x=205, y=22)

        qqstb = tk.Button(self, text='加入缺勤名单>>>', font=('宋体', 10), width=15, height=2, command=joinqq)
        qqstb.place(x=220, y=130)

        saveb = tk.Button(self, text='完成考勤', font=('宋体', 10), width=17, height=1, command=kqok)
        saveb.place(x=350, y=250)

        global nowkq
        tipl = tk.Label(self, text='当前考勤项目为  ' + nowkq, font=('华文行楷', 15))
        tipl.place(x=300, y=300)


# 考勤内容选择窗口
class KqChoose(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('考勤内容选择')
        wi = self.winfo_screenwidth()
        he = self.winfo_screenheight()
        x = 200
        y = 200
        self.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
        self.resizable(width=False, height=False)
        self.overrideredirect(True)
        self.ini_ui()

    def ini_ui(self):
        sb = tk.Scrollbar(self, orient='vertical')
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        nrlist = tk.Listbox(self, height=8, width=25)
        nrlist.place(x=0, y=0)
        kqf = open('./db/' + uname + '/kqlist.csv', 'r', encoding='utf-8')
        kqc = csv.reader(kqf)
        for n in kqc:
            nrlist.insert('end', n[0])

        nrlist.config(yscrollcommand=sb.set)
        sb.config(command=nrlist.yview, width=16)

        def enter():
            global nowkq
            nowkq = nrlist.get('active')
            self.destroy()
            KqWindow().mainloop()

        enterb = tk.Button(self, width=23, height=1, text='确定', command=enter)
        enterb.place(x=5, y=155)


# 导入新班级窗口
class DrNewClass(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('导入新班级')
        self.geometry("330x120")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        def drmd():
            mdfile = filedialog.askopenfilename(filetypes=[("CSV", ".csv")])
            var.set(mdfile)

        def drquit():
            f = open(var.get(), 'r', encoding='utf-8')
            fc = csv.reader(f)
            f2 = open('./db/' + uname + '/' + nmet.get() + '.csv', 'a', newline='', encoding='utf-8')
            fw = csv.writer(f2)
            for row in fc:
                row.append('0')
                row.append('')
                fw.writerow(row)
            f2.close()
            f3 = open('./db/' + uname + '/classlist.txt', 'a', encoding='utf-8')
            f3.write(nmet.get() + '\n')
            f3.close()
            self.destroy()
            StManager().mainloop()

        def fh():
            self.destroy()
            StManager().mainloop()

        crb = tk.Button(self, text='从.csv导入名单...', command=drmd)
        crb.place(x=220, y=12)
        var = tk.StringVar(self)
        var.set("请选择班级名单")
        locl = tk.Label(self, textvariable=var)
        locl.place(x=20, y=15)
        mcb = tk.Label(self, text='班级名称：', font=('黑体', 9))
        mcb.place(x=10, y=55)
        nmet = tk.Entry(self, show=None, font=('黑体', 12), width=20)
        nmet.place(x=65, y=55)
        qdb = tk.Button(self, text='确定', width=10, command=drquit)
        qdb.place(x=245, y=50)
        fhb = tk.Button(self, text='返回', command=fh, width=10)
        fhb.place(x=245, y=80)


# 学生管理窗口
class StManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('学生及考勤项目管理')
        self.geometry("540x350")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        # 学生班级管理
        def drnc():
            self.destroy()
            DrNewClass().mainloop()

        def ok():
            nmli.delete(0, 'end')
            f2 = open('./db/' + uname + '/' + chcl.get() + '.csv', 'r', encoding='utf-8')
            fw = csv.reader(f2)
            for row2 in fw:
                nmli.insert('end', row2[0])

        nmlabel = tk.Label(self, text='当前用户为  ' + uname, font=('华文行楷', 15))
        nmlabel.place(x=290, y=300)
        crbj = tk.Button(self, text='导入新班级...', command=drnc, font=('宋体', 10))
        crbj.place(x=80, y=300)
        allcl = []
        try:
            f = open('./db/' + uname + '/classlist.txt', 'r', encoding='utf-8')
        except FileNotFoundError:
            t = open('./db/' + uname + '/classlist.txt', 'w', encoding='utf-8')
            t.close()
        else:
            for row in f.readlines():
                trow = row.replace('\n', '')
                allcl.append(trow)

        chcl = ttk.Combobox(self, values=allcl)
        chcl.place(x=42, y=20)
        nmli = tk.Listbox(self, height=13)
        nmli.place(x=56, y=50)
        qd = tk.Button(self, text='班级选择预览', command=ok, font=('宋体', 8))
        qd.place(x=214, y=20)

        # 考勤内容管理
        nrlist = tk.Listbox(self, height=9, width=27)
        nrlist.place(x=295, y=50)
        ft1 = open('./db/' + uname + '/kqlist.csv', 'a', encoding='utf-8')
        ft1.close()
        kqf = open('./db/' + uname + '/kqlist.csv', 'r', encoding='utf-8')
        kqc = csv.reader(kqf)
        for n in kqc:
            nrlist.insert('end', n[0] + '      ' + n[1] + '学分')

        def addn():
            kqnm = newnm.get()
            kqsc = newsc.get()
            nrlist.insert('end', kqnm + '      ' + kqsc + '学分')
            kqf1 = open('./db/' + uname + '/kqlist.csv', 'a', newline='', encoding='utf-8')
            kqw = csv.writer(kqf1)
            kqw.writerow([kqnm, kqsc])
            newnm.delete(0, 'end')
            newsc.delete(0, 'end')
            tk.messagebox.showinfo('添加成功', '添加成功')
            kqf1.close()

        def fc():
            self.destroy()
            MainWindow().mainloop()

        adl = tk.Label(self, text='名称:                            学分:')
        adl.place(x=250, y=220)
        newnm = tk.Entry(self, width=14)
        newnm.place(x=285, y=220)
        newsc = tk.Entry(self, width=2)
        newsc.place(x=422, y=220)
        ad = tk.Button(self, width=5, height=1, text='添加', font=('宋体', 10), command=addn)
        ad.place(x=450, y=218)
        fh = tk.Button(self, text='返回', command=fc, font=('宋体', 14))
        fh.place(x=460, y=295)


# 学生导出窗口
class StWatcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('学生成绩导出')
        self.geometry("310x400")
        self.resizable(width=False, height=False)
        self.init_ui()

    def init_ui(self):
        def exp():
            sav = filedialog.asksaveasfilename(title='导出名单', filetypes=[('SCV文件', '.csv')])
            f1 = open(sav + '.csv', 'w', newline='', encoding='GB2312')
            fnw = csv.writer(f1)
            f2 = open('./db/' + uname + '/' + chcl.get() + '.csv', 'r', encoding='utf-8')
            fr = csv.reader(f2)
            fnw.writerow(['姓名', '总学分', '缺勤项目'])
            for row1 in fr:
                fnw.writerow(row1)
            tk.messagebox.showinfo('成功', '导出成功！')

        def fc():
            self.destroy()
            MainWindow().mainloop()

        def ok():
            nmli.delete(0, 'end')
            f2 = open('./db/' + uname + '/' + chcl.get() + '.csv', 'r', encoding='utf-8')
            fw = csv.reader(f2)
            for row2 in fw:
                nmli.insert('end', row2[0] + '     ' + '总' + row2[1] + '学分')

        dcb = tk.Button(self, text='导出为.csv...', width=13, command=exp)
        dcb.place(x=195, y=250)
        fh = tk.Button(self, text='返回', width=13, command=fc)
        fh.place(x=195, y=340)
        allcl = []
        with open('./db/' + uname + '/classlist.txt', 'r', encoding='utf-8') as f:
            for row in f.readlines():
                trow = row.replace('\n', '')
                allcl.append(trow)
        chcl = ttk.Combobox(self, values=allcl)
        chcl.place(x=30, y=20)
        nmli = tk.Listbox(self, height=18)
        nmli.place(x=30, y=50)
        qd = tk.Button(self, text='班级选择预览', command=ok)
        qd.place(x=200, y=18)


# 主窗口
class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("学生体育考勤管理系统")
        self.geometry("680x405")
        self.resizable(width=False, height=False)
        self.ini_ui()

    def ini_ui(self):
        toplabel = tk.Label(self, text="学 生 体 育 考 勤 系 统", font=('黑体', 16))
        toplabel.place(x=10, y=15)

        global uname
        namelabel = tk.Label(self, text='欢迎  ' + uname + "  使用本系统", font=('华文行楷', 12))
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

        kqbutton = tk.Button(self, text='学生体育考勤', font=('宋体', 16), width=20, height=3, command=opkqwindow)
        kqbutton.place(x=20, y=70)
        ckbutton = tk.Button(self, text='导出学生成绩', font=('宋体', 16), width=20, height=3, command=opstdcwindow)
        ckbutton.place(x=20, y=170)
        tjbutton = tk.Button(self, text='学生考勤管理', font=('宋体', 16), width=20, height=3, command=opstmnwindow)
        tjbutton.place(x=20, y=270)

        tcbutton = tk.Button(self, text='退出系统', font=('微软雅黑', 9), width=8, height=1, command=mainquit)
        tcbutton.place(x=210, y=358)

        tpl = tk.Label(self)
        tpl.pack()


if __name__ == "__main__":
    SignWindow().mainloop()
