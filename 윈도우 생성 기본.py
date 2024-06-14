#윈도우 생성 기본
import tkinter as tk

root_win=tk.Tk()                 #윈도우 객체 반환 *여기서 root_win->직접 지정가능
root_win.title('집가고싶다')        #제목
root_win.geometry('500x200-0+50')   #가로x세로,가로위치,세로위치
root_win.resizable(width=False, height=False)    #F->고정 T->고정x

root_win.mainloop()  #처리 시작







