# py-yt-downloader

You must have Tkinter and Pip installed on your system.

If you are a Windows user, make sure to select "Add Python to PATH" when installing Python on your system.
Or you can go to the file path and run it from there :D

---

Prerequisites:
```console
$ pip3 install -r requirements.txt
```

`customtkinter-directory`:
```console
$ pip show customtkinter
```

---

Build from source code:
```console
$ pyinstaller --noconfirm --onedir --windowed --add-data "<customtkinter-directory>/customtkinter:customtkinter/"  "py-yt-downloader.py"
```

---
When using py-yt-downloader, the videos and music you download will be saved in the "Current Directory:" location at the bottom of the application. Your "Current Directory:" will be where you run the application.
