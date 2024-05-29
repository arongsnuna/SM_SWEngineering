import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

# ------------------------------------ 링크 ----------------------------------
def open_link():
    # 시험 장소 조회 링크 열기
    webbrowser.open("https://m.exam.toeic.co.kr/receipt/centerMap.php")

def open_member_login_link():
    # 회원 로그인 링크 열기
    webbrowser.open("https://www.ybmnet.co.kr/common/login.asp?url=%2Fcommon%2FcertifyResponse.php%3FreturnUrl%3D%2Freceipt%2FconfirmList.php&what=m.exam.toeic.co.kr")

def open_non_member_login_link():
    # 비회원 로그인 링크 열기
    webbrowser.open("https://certify.ybmnet.co.kr/common/certiModuleExam/certify_step1.asp?returnUrl=https%3A%2F%2Fm.exam.toeic.co.kr%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php&loginWhat=m.exam.toeic.co.kr&loginUrl=%2Fcommon%2FcertifyResponse.php%3FexamCate%3DTOE%26returnUrl%3D%252Freceipt%252FconfirmList.php")

# -------------------------------- 이미지 파일 경로 ---------------------------
ets_icon_path = "dictionary/assets/frame2/exam_place_seyeon_image/ets.png"
member_login_icon_path = "dictionary/assets/frame2/exam_place_seyeon_image/member_login_icon.png"
non_member_login_icon_path = "dictionary/assets/frame2/exam_place_seyeon_image/non_member_login_icon.png"
gear_icon_path = "dictionary/assets/frame2/title_bar_frame_image.png"
menu_icon_path = "dictionary/assets/frame2/title_bar_frame_image/sidebar_icon.png"

# -------------------------------- GUI 초기화 --------------------------------
root = tk.Tk()
root.title("토익 시험 일정")
root.geometry("700x550")
root.configure(background="#FFFFFF")  

style = ttk.Style()
style.theme_use('clam')

# -------------------------------- 회색 바 설정 --------------------------------
style.configure('TFrame', background='#838383')
title_bar_frame = ttk.Frame(root, style='TFrame', height=30)
title_bar_frame.pack(fill='x')

gear_icon = ImageTk.PhotoImage(Image.open(gear_icon_path).resize((30, 30)))
menu_icon = ImageTk.PhotoImage(Image.open(menu_icon_path).resize((30, 30)))

gear_button = tk.Button(title_bar_frame, image=gear_icon, borderwidth=0, bg="#838383", cursor="hand2")
gear_button.pack(side=tk.LEFT, padx=20)

text_label = tk.Label(title_bar_frame, text="토익 고사장 안내", font=("Helvetica", 15, "bold"), background="#838383")
text_label.pack(side="left", padx=5)

menu_button = tk.Button(title_bar_frame, image=menu_icon, borderwidth=0, bg="#838383", cursor="hand2")
menu_button.pack(side=tk.RIGHT, padx=20)

# -------------------------------- 내용 --------------------------------
window_width = root.winfo_width()

ets_icon = ImageTk.PhotoImage(Image.open(ets_icon_path))
member_login_icon = ImageTk.PhotoImage(Image.open(member_login_icon_path))
non_member_login_icon = ImageTk.PhotoImage(Image.open(non_member_login_icon_path))

ets_button = tk.Button(root, image=ets_icon, borderwidth=0, bg="#FFFFFF", command=open_link, cursor="hand2")
ets_button.pack(pady=(20,0))

ets_label = tk.Label(root, text="[ 고사장 조회 ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
ets_label.pack(pady=(0,30))  

member_login_button = tk.Button(root, image=member_login_icon, borderwidth=0, bg="#FFFFFF", command=open_member_login_link, cursor="hand2")
member_login_button.pack()

member_login_label = tk.Label(root, text="[ 회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
member_login_label.pack(pady=(0,30))

non_member_login_button = tk.Button(root, image=non_member_login_icon, borderwidth=0, bg="#FFFFFF", command=open_non_member_login_link, cursor="hand2")
non_member_login_button.pack()

non_member_login_label = tk.Label(root, text="[ 비회원 정보 조회 (YBM) ]", font=("Helvetica", 15, "bold"), bg="#FFFFFF")
non_member_login_label.pack()

root.mainloop()
