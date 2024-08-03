import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    quality = quality_var.get()
    output_path = path_entry.get() or '.'
    try:
        yt = YouTube(url)
        
        # Filter streams by quality
        if quality == "Highest":
            stream = yt.streams.get_highest_resolution()
        elif quality == "Audio Only":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.filter(res=quality).first()

        # Display status and download
        if stream:
            status_label.config(text=f"Downloading: {yt.title} in {quality}")
            stream.download(output_path=output_path)
            status_label.config(text="Download completed!")
        else:
            status_label.config(text=f"No streams available for the selected quality: {quality}")

    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

# Create GUI window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL input
tk.Label(root, text="YouTube URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Quality selection
tk.Label(root, text="Select Quality:").pack()
quality_var = tk.StringVar(value="Highest")
qualities = ["Highest", "2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p", "Audio Only"]
quality_menu = tk.OptionMenu(root, quality_var, *qualities)
quality_menu.pack()

# Output path input
tk.Label(root, text="Save to (path):").pack()
path_entry = tk.Entry(root, width=50)
path_entry.pack()

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

# Run the GUI event loop
root.mainloop()
