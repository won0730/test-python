import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def buildGUI():
    global text_area   #이벤트 헨들러 접근 위해 
    text_area=tk.Text(win, width=30,height=5,wrap=tk.WORD)
       #ttk가 따로 없음
       #부모윈도우 win지정, 폭 높이 조정, wrap=줄바꿈 방식->GUI에서 단어 단위로 줄바꿈
                                    #WORD->단어단위 CHAR->문자단위(한글자)

    #text_area=scrolledtext.ScrolledText(win, width=30,height=5,wrap=tk.WORD)
    #tk.Text대신 위 위젯을 사용할 경우 스크롤바 생

    
    input_btn=ttk.Button(win,text='출력',command=input_btn_handler)
                           #출력이라는 버튼, command->버튼을 눌렀을때 처리될 동작
   
 
    text_area.pack()     #나열식 배치
    input_btn.pack()
    

def input_btn_handler():
    print(text_area.get(0.0,tk.END))
 #텍스트 영역에서 내용을 가져오는 부분->0.0은 텍스트 영역 젤 첫번째, END는 역역의 끝을 의미
    text_area.delete(0.0,tk.END)
 #텍스트를 출력후 GUI에서 텍스를 전부 없                                 

win=tk.Tk()
win.title('라벨 위젯')
buildGUI()
win.mainloop()
