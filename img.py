import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def show_cat():
    try:
        img = Image.open("s/cat.jpg")  # 고양이 이미지 파일 경로
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Keep a reference!
    except FileNotFoundError:
        image_label.config(text="고양이 이미지를 찾을 수 없습니다.")

def show_rabbit():
    try:
        img = Image.open("s/rabbit.png")  # 토끼 이미지 파일 경로
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except FileNotFoundError:
        image_label.config(text="토끼 이미지를 찾을 수 없습니다.")

def show_raccon():
    try:
        img = Image.open("s/raccon.jpg")  # 너구리 이미지 파일 경로
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except FileNotFoundError:
        image_label.config(text="너구리 이미지를 찾을 수 없습니다.")

# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 이미지 뷰어")

# 버튼 생성
cat_button = ttk.Button(window, text="고양이", command=show_cat)
cat_button.pack(pady=10)

rabbit_button = ttk.Button(window, text="토끼", command=show_rabbit)
rabbit_button.pack(pady=10)

raccoon_button = ttk.Button(window, text="너구리", command=show_raccon)
raccoon_button.pack(pady=10)

# 이미지를 표시할 레이블 생성
image_label = tk.Label(window, text="이미지를 선택하세요.")
image_label.pack(pady=20)

# 메인 이벤트 루프 시작
window.mainloop()