from tkinter import *
from tkinter import filedialog
import TrichRutDacTrung as ft
import jsonpickle as json
import TinhDoTuongDong

# Mở file JSON và đọc nội dung của file
with open('metadata/data.json', 'r') as file:
    json_data = file.read()

# Chuyển đổi nội dung file JSON thành đối tượng Python
feature_list = json.loads(json_data)

def nhanDang():
    file = filedialog.askopenfilename(filetypes=(("Audio files", "*.wav"), ("all files", "*.*")))
    if file:
        # Trích rút đặc trưng từ file âm thanh
        features = ft.features(file=file)
        # Bao bọc các đặc trưng vào đối tượng Feature
        audio_features = [TinhDoTuongDong.Feature(link=file, feature=f) for f in features]
        # Tính toán độ tương đồng
        doTD = TinhDoTuongDong.SimilarityCalculation(feature_list, audio_features)
        lbl2 = Label(win, text="Top 3 tiếng người đàn ông giống nhất: \n" + "\n".join(doTD), font=("Arial Bold", 14))
        lbl2.place(x=100, y=250)

def nhanNhanDang():
    global win
    win = Toplevel(window)
    win.title("Truy xuất tiếng người đàn ông")
    win.geometry('800x600')
    butAdd = Button(win, text='Chọn tệp âm thanh', width=20, height=2, command=nhanDang)
    butAdd.place(x=100, y=200)
    win.mainloop()

window = Tk()
window.title("Truy xuất tiếng người đàn ông")
window.geometry('800x600')
but2 = Button(window, text='Nhận dạng âm thanh', command=nhanNhanDang, width=20, height=2)
but2.place(x=340, y=300)
window.mainloop()
