import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def download_video():
    url = url_entry.get()
    save_dir = dir_entry.get()

    if not url:
        messagebox.showerror("エラー", "URLを入力してください")
        return
    if not save_dir:
        messagebox.showerror("エラー", "保存先を指定してください")
        return

    # yt-dlpの設定
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_dir}/%(title)s.%(ext)s', # 保存場所とファイル名を指定
    }

    try:
        status_label.config(text="ダウンロード中...", fg="blue")
        root.update() # 画面を更新
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        status_label.config(text="完了！", fg="green")
        messagebox.showinfo("成功", "ダウンロードが完了しました！")
    except Exception as e:
        status_label.config(text="エラー発生", fg="red")
        messagebox.showerror("エラー", f"失敗しました: {e}")

def select_dir():
    # フォルダ選択ダイアログを表示
    path = filedialog.askdirectory()
    if path:
        dir_entry.delete(0, tk.END)
        dir_entry.insert(0, path)

# GUIの設定
root = tk.Tk()
root.title("Python Video Downloader")
root.geometry("500x250")

# URL入力欄
tk.Label(root, text="動画URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# 保存先選択
tk.Label(root, text="保存先:").pack(pady=5)
frame = tk.Frame(root)
frame.pack()
dir_entry = tk.Entry(frame, width=40)
dir_entry.pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="参照", command=select_dir).pack(side=tk.LEFT)

# ダウンロードボタン
tk.Button(root, text="ダウンロード開始", command=download_video, bg="red", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# 状態表示
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()