import tkinter as tk

window = tk.Tk()
wi = window.winfo_screenwidth()
he = window.winfo_screenheight()
x = 500
y = 200
window.geometry("%dx%d+%d+%d" % (x, y, (wi - x) / 2, (he - y) / 2))
window.overrideredirect(True)
window.resizable(width=False, height=False)
l = tk.Label(window, text='账号', font=('宋体', 18))
l.place(x=30, y=40)
l1 = tk.Label(window, text='密码', font=('宋体', 18))
l1.place(x=30, y=90)
e1 = tk.Entry(window, show=None, font=('宋体', 18))
e1.place(x=130, y=43)
e1.focus()
e2 = tk.Entry(window, show='*', font=('宋体', 18))
e2.place(x=130, y=93)


def focus():
    e2.focus()


def func():
    window.destroy()


B1 = tk.Button(window, text='取消', font=('宋体', 12), width=10, height=1, command=func)
B2 = tk.Button(window, text='登录', font=('宋体', 12), width=10, height=1)
B3 = tk.Button(window, text='注册', font=('宋体', 12), width=10, height=1)
B1.place(x=330, y=150)
B2.place(x=200, y=150)
B3.place(x=70, y=150)
window.mainloop()
