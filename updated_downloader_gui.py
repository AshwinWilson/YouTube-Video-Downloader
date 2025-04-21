import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from yt_dlp import YoutubeDL
import threading

# Function to download video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    output_folder = folder_path.get() or "D:/Nuclear codes/Python/Downloads"

    ydl_opts = {
        "format": "bestvideo+bestaudio",
        "merge_output_format": "mp4",
        "outtmpl": f"{output_folder}/%(title)s.%(ext)s"
    }

    # Show progress bar
    progress_bar.start()
    
    def download():
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'Unknown Title')
                messagebox.showinfo("Success", f"Downloaded: {title}")
        except Exception as e:
            messagebox.showerror("Download Failed", str(e))
        finally:
            progress_bar.stop()

    threading.Thread(target=download).start()  # Run download in a separate thread

# Function to choose folder
def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# Create main window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("500x400")
root.configure(bg="#1e1e2d")  # Dark theme background

# Set window icon
# root.iconbitmap("icon.ico")  # Uncomment if you have an icon file

# Title Label
tk.Label(root, text="🎥 YouTube Video Downloader", font=("Arial", 16, "bold"), bg="#1e1e2d", fg="#ffcc00").pack(pady=10)

# YouTube URL Entry
tk.Label(root, text="Enter YouTube URL:", font=("Arial", 12), bg="#1e1e2d", fg="white").pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Folder Selection
folder_path = tk.StringVar()
ttk.Button(root, text="Choose Folder", command=choose_folder).pack(pady=5)
ttk.Entry(root, textvariable=folder_path, width=50).pack(pady=5)

# Download Button
download_btn = ttk.Button(root, text="📥 Download Video", command=download_video)
download_btn.pack(pady=20)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(pady=5)

# Run the GUI loop
root.mainloop()
