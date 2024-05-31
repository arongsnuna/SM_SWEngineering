import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from wordClass import WordDBModel



# ----------------------------- Model -----------------------------
class ManagementModel:
    
    # 삭제하기
    def delete_enter(del_entry):
        # 입력 상자에서 입력된 내용 가져오기
        word = del_entry.get()
        wordModel = WordDBModel()
        
        # 입력된 내용을 터미널에 출력하기
        if (word == "삭제할 단어"):
            print("삭제 ERROR: 모든 단어 입력 X")
        else:
            if(wordModel.check_word_exist(word)):
                wordModel.delete_word(word)
                messagebox.showinfo("단어 삭제", "삭제되었습니다.")

            else:
                messagebox.showinfo("단어 삭제", "존재하지 않는 단어입니다.")

            # 입력 상자 초기화
            del_entry.delete(0, "end")
            del_entry.insert(0, "삭제할 단어")

    # 수정하기
    def modify_enter(modify_word_entry, modify_korean_entry):
        # 입력 상자에서 입력된 내용 가져오기
        word = modify_word_entry.get()
        korean=modify_korean_entry.get()
        wordModel = WordDBModel()
        

        # 입력된 내용을 터미널에 출력하기
        if (word == "수정할 단어" or korean == "수정할 단어의 뜻"):
            print("수정 ERROR: 모든 단어 입력 X")
        else:
            print("Modify input) word = ", word, "korean = ", korean)
            if(wordModel.check_word_exist(word)):
                wordModel.update_word(word, korean)
                messagebox.showinfo("단어 수정", "수정되었습니다")
            else:
                messagebox.showinfo("단어 수정", "존재하지 않는 단어입니다.")

            # 입력 상자 초기화
            modify_word_entry.delete(0, "end")
            modify_word_entry.insert(0, "추가할 단어")
            modify_korean_entry.delete(0, "end")
            modify_korean_entry.insert(0, "추가할 단어의 뜻")


    # 추가하기
    def add_enter(add_word_entry, add_korean_entry):
        # 입력 상자에서 입력된 내용 가져오기
        word = add_word_entry.get()
        korean=add_korean_entry.get()
        wordModel = WordDBModel()

        # 입력된 내용을 터미널에 출력하기
        if (word == "추가할 단어" or korean == "추가할 단어의 뜻"):
            print("추가 ERROR: 모든 단어 입력 X")
        else:
            if(wordModel.check_word_exist(word)):
                messagebox.showinfo("단어 추가", "이미 존재하는 단어입니다.")
            else:
                wordModel.add_word(word, korean)
                messagebox.showinfo("단어 추가", "추가되었습니다.")
            
            # 입력 상자 초기화
            add_word_entry.delete(0, "end")
            add_word_entry.insert(0, "추가할 단어")
            add_korean_entry.delete(0, "end")
            add_korean_entry.insert(0, "추가할 단어의 뜻")

# ----------------------------- View -----------------------------
class ManagementView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self): # GUI 초기화
        """root = tk.Tk()
        root.title("단어 관리")
        root.geometry("700x550")
        root.configure(background="#FFFFFF")  """
        root = self.root
        style = ttk.Style()
        style.theme_use('clam')

        canvas = tk.Canvas(root)
        canvas.pack(side="left", fill="both", expand=True)
        frame = tk.Frame(canvas)
        canvas.create_window((50, 0), window=frame, anchor="nw")

        delete_box = tk.Frame(frame, bg="#838383") # "단어 삭제" 프레임
        delete_box.pack(pady=30, fill="x")

        del_text_box = tk.Label(delete_box, text="단어 삭제하기", font=("Helvetica", 15), bg="#838383")
        del_text_box.pack(padx=5, pady=10)

        del_entry = tk.Entry(delete_box, bg="white", fg="black", bd=2, relief="flat")
        del_entry.insert(0, "삭제할 단어")
        del_entry.pack(padx=20, pady=10)
        del_entry.bind("<Return>", lambda e:ManagementModel.delete_enter(del_entry))

        add_box = tk.Frame(frame, bg="gray") # "단어 추가" 프레임
        add_box.pack(pady=30, fill="x")

        add_text_box = tk.Label(add_box, text="단어 추가하기", font=("Helvetica", 15), bg="#838383")
        add_text_box.pack(padx=20, pady=10)

        add_word_entry = tk.Entry(add_box, bg="white", fg="black", bd=2, relief="flat")
        add_word_entry.insert(0, "추가할 단어")
        add_word_entry.pack(side="left", padx=20, pady=10)
        add_word_entry.bind("<Return>", lambda e:ManagementModel.add_enter(add_word_entry, add_korean_entry))

        add_korean_entry = tk.Entry(add_box, bg="white", fg="black", bd=2, relief="flat")
        add_korean_entry.insert(0, "추가할 단어의 뜻")
        add_korean_entry.pack(side="left", fill="x", padx=20, pady=10)
        add_korean_entry.bind("<Return>", lambda e:ManagementModel.add_enter(add_word_entry, add_korean_entry))
        #add_korean_entry.bind("<Return>", ManagementModel.add_enter(add_word_entry, add_korean_entry, add_ex_entry))

        modify_box = tk.Frame(frame, bg="gray") # "단어 수정" 프레임
        modify_box.pack(pady=30, fill="x")

        text_box = tk.Label(modify_box, text="단어 수정하기", font=("Helvetica", 15), bg="#838383")
        text_box.pack(padx=20, pady=10)

        modify_word_entry = tk.Entry(modify_box, bg="white", fg="black", bd=2, relief="flat")
        modify_word_entry.pack(side="left", fill="x", padx=20, pady=10)
        modify_word_entry.insert(0, "수정할 단어")
        modify_word_entry.bind("<Return>", lambda e:ManagementModel.modify_enter(modify_word_entry, modify_korean_entry))

        modify_korean_entry = tk.Entry(modify_box, bg="white", fg="black", bd=2, relief="flat")
        modify_korean_entry.pack(side="left", fill="x", padx=20, pady=10)
        modify_korean_entry.insert(0, "수정할 단어의 뜻")
        modify_korean_entry.bind("<Return>", lambda e:ManagementModel.modify_enter(modify_word_entry, modify_korean_entry))

        #upload_csv_icon = tk.PhotoImage(file="resource\csv_upload_btn.png").subsample(2) # csv 파일 업로드 버튼
        upload_csv_button = tk.Button(canvas, relief = "flat", bd = 0, font=('Helvetica', 15, 'bold'), text="csv 파일 업로드",  bg='#838383', command=lambda:ManagementController.upload_csv_file(), cursor="hand2")
        upload_csv_button.place(x=500, y=450)

        
        self.root.mainloop()

# ----------------------------- Controller -----------------------------
class ManagementController:
    def __init__(self, root):
        self.model = ManagementModel
        self.view = ManagementView(root)

    def upload_csv_file():
        print("csv 파일 업로드 완")