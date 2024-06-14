#ttk라벨에 설정된 옵션값 확인

import tkinter as tk
from tkinter import ttk

def display_options(widget):     #widget->위젯들의 공통된 특성을 갖는 클래스
    config=widget.configure()     #configure-> 위젯의 모든 옵션을 딕셔너리로 반환
    for key,value in config.items():
        print(f'{key:15s}\t{value}')

widget=ttk.Label(None)
display_options(widget)         #widget->위젯들의 공통된 특성을 갖는 클래스
