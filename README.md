# YouTube-Video-Downloader GUI

A simple and efficient Python desktop application to download YouTube videos in the best available quality (video + audio) using a Tkinter-based GUI and the powerful `yt_dlp` library.

---

## Features

- Download YouTube videos via URL input
- Choose your preferred download folder
- Downloads best video and audio merged into a `.mp4` file
- Uses multithreading to keep the interface responsive
- Progress bar and pop-up alerts for download status
- Clean dark-themed interface

---

## Tech Stack

- Python 3
- Tkinter – for GUI
- yt_dlp – for downloading and merging video/audio
- threading – for smooth background processing

---

## Preview

![image](https://github.com/user-attachments/assets/465aa3d0-9532-4cf2-b2ba-de02048d61da)

- The application features a minimalist dark-themed GUI built with Tkinter, designed for clarity and ease of use.

- Users can input a YouTube URL, select a download destination folder, and initiate the download with a single click.

- A progress bar runs during downloads to indicate activity, while pop-up messages provide real-time feedback on success or errors.

---

## How It Works

1. The user enters a YouTube URL in the input field.
2. They may optionally select a destination folder for saving the video.
3. On clicking the "Download Video" button:
   - The app fetches the best video and audio streams
   - Merges them into an `.mp4` file
   - Displays a success or error message when done
4. A progress bar runs during the download to indicate activity.

---

## Code Highlights

### Download Options

```python
ydl_opts = {
    "format": "bestvideo+bestaudio",
    "merge_output_format": "mp4",
    "outtmpl": f"{output_folder}/%(title)s.%(ext)s"
}
```
- bestvideo+bestaudio: ensures highest quality

- merge_output_format: merges video and audio into MP4

- outtmpl: custom naming based on video title
