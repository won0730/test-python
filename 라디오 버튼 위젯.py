import tkinter as tk
from tkinter import ttk

GENDERS = [ '남성','여성', '기타' ]   #리스트로 버튼 항목 지정
COLORS =[ 'red', 'yellow', 'purple' ]  #각 색깔 지


def buildGUI():
    text_label = ttk.Label(win, text='당신의 성별은? ') #버튼 위 문자열 출력
    text_label.pack()      #나열

    global gender
    gender = tk.IntVar()  #선택한 항목 저장
    for i in range(3):    #반복 이용해 라디오 버튼 모두 보이게함
        radio_btn = ttk.Radiobutton(win,text=GENDERS[i],value=i,variable=gender,
                                    command=radio_btn_hadler)
        radio_btn.pack()

    gender.set(-1)   #라디오 버튼 선택 지우기

def radio_btn_hadler():
    choice = gender.get() #값반환
    win.configure(background=COLORS[choice])  #해당 순서에 맞는 색 으로 배경 지정


win = tk.Tk()
win.title('버튼 위젯 예')
buildGUI()
win.mainloop()
