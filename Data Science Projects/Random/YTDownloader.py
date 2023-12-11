def YTDownloader(base_url):

    pip install yt-dlp --quiet
    import yt_dlp
    import os

    url = base_url
    downloads_folder = os.path.expanduser("~/Downloads")

    ydl_opts = {
        "outtmpl": os.path.join(downloads_folder, "%(title)s.%(ext)s")
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  

if __name__ == "__main__":
    base_url = input("Enter video url: ")
    YTDownloader(base_url)
    print("\nYour video has downloaded successfully!")