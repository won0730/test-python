import tkinter as tk
from tkinter import ttk

def buildGUI():
    text_label1=ttk.Label(win, text='안녕하세요') #객체=Label(부모윈도우,text='문자열')
                                           #부모윈도우:부착될 윈도우, 제일 바탕이 되는

    text_label2=ttk.Label(win)       #부모윈도우 지정
    text_label2.configure(text='반가워요',foreground='white',
                          background='red',font=('맑은 고딕',20))
                        #configure=특정 옵션값 변경
    text_label1.pack()
    text_label2.pack()         
                        #pack->지정한 부모윈도우에 나열식으로 배치
win=tk.Tk()
win.title('라벨 위젯')
buildGUI()
win.mainloop()


#여러 위젯에 같은 스타일을 원할 경우 스타일을 설정하여 사용 할 수도 있음(38p)
