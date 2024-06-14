import tkinter as tk
from tkinter import ttk

def buildGUI():
    global text_label   #이벤트 헨들러 접근 위해 
    text_label=ttk.Label(win, text='안녕하세요')
                               #텍스트 라벨=win 부모윈도우에 안녕하세요라는 글자 배치

    global name         #이벤트 헨들러 접근
    name=tk.StringVar()   #문자열 저장할 tk변수 객체
    input_entry=ttk.Entry(win,textvariable=name)  #입력받은 문자를 변수에 저장

    
    input_btn=ttk.Button(win,text='입력',command=input_btn_handler)
                           #입력이라는 버튼, command->버튼을 눌렀을때 처리될 동작
    quit_btn=ttk.Button(win,text='종료',command=win.destroy)
                                #win.destroy->윈도우 win 창 닫기
 
    text_label.pack()     #나열식 배치
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text='반가워요,'+name.get())
            #버튼을 눌렀을 경우 텍스트를 반가워요로 지정, get->입력받은 값 반환
    name.set('')   #버튼을 누르면 빈문자열이 되도록                         

win=tk.Tk()
win.title('라벨 위젯')
buildGUI()
win.mainloop()
