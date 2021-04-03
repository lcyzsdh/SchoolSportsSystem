import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
       super().__init__()
       self.title("SchoolSportsSystem")
       self.geometry("1480x900")
       self.ini()
    def ini(self):
        self.btn1 = tk.Button(self,text="1")
        self.btn1.pack(padx=200,pady=30)

if __name__ == "__main__":
    app =MainWindow()
    app.mainloop()