import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def buildGUI():
    global check      #이벤트 헨들러 접근
    check = tk.IntVar()    #체크 상태 저장 변수
    check_btn = ttk.Checkbutton(win, text='옵션을 선택하세요',variable=check,
                                command=open_dialog_box)

    check_btn.pack()

def open_dialog_box():
    if check.get() == 1:    #1-> 체크박스 선택된 상태
        messagebox.showinfo('확인', '옵션 선택')#확인 버튼이 있는 옵션 선택이라는 창 띄움
    else:
        messagebox.showinfo('확인', '옵션 해제')


win=tk.Tk()
win.title('위젯')
buildGUI()
win.mainloop()
