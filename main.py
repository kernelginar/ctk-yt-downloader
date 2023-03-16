import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from pytube import YouTube

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class YT_Downloader(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Download Function
        def startDownloadVideo():
            try:
                video_finish_label.configure(text="")
                
                video_link_yt = video_link.get()
                video_file_name_yt = video_file_name.get()
                video_file_extension_yt = video_file_extension.get()
                
                video_ytObject = YouTube(video_link_yt, on_progress_callback=video_on_progress)
                
                video = video_ytObject.streams.filter(file_extension=video_file_extension_yt).get_highest_resolution()
                video.download(filename=video_file_name_yt+"."+video_file_extension_yt)
                video_finish_label.configure(text="Downloaded!")
            except:
                video_finish_label.configure(text="Failed to download video!")
            video_finish_label.configure(text="Video downloaded!")
                    
        # Video Progress Bar Function
        def video_on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            per = str(int(percentage_of_completion))
            video_pPercentage.configure(text=per + "%")
            video_pPercentage.update()
            
            video_progressBar.set(float(percentage_of_completion) / 100)
        
        self.title("YouTube Video - Audio Downloader")
        self.geometry("800x600")
        self.minsize(800, 600)
        
        
        ################################# Video ######################################
        
        
        # Main Tab
        tab = ctk.CTkTabview(master=self)
        tab.pack(padx=10, pady=10, expand=True, fill="both")
        tab.add("Video")
        tab.add("Audio")
        
        # Video Label
        video_label = ctk.CTkLabel(master=tab.tab("Video"), text="-- YouTube Video Downloader --")
        video_label.pack(padx=10, pady=10)
        
        # Video Input
        video_link = ctk.CTkEntry(master=tab.tab("Video"), width=350, height=40, placeholder_text="YouTube Link")
        video_link.pack(padx=10, pady=10)
        
        # Video File Name
        video_file_name = ctk.CTkEntry(master=tab.tab("Video"), width=350, height=40, placeholder_text="File Name")
        video_file_name.pack(padx=10, pady=10)
        
        # Video File Extension
        video_file_extension = ctk.CTkEntry(master=tab.tab("Video"), width=350, height=40, placeholder_text="File Extension: mp4, mkv")
        video_file_extension.pack(padx=10, pady=10)
        
        # Video Finished label
        video_finish_label = ctk.CTkLabel(master=tab.tab("Video"), text="")
        video_finish_label.pack()
        
        # Video Progress Percentage
        video_pPercentage = ctk.CTkLabel(master=tab.tab("Video"), text="%0")
        video_pPercentage.pack()
        
        video_progressBar = ctk.CTkProgressBar(master=tab.tab("Video"), width=400)
        video_progressBar.set(0)
        video_progressBar.pack(padx=10, pady=10)
               
        # Video Download Button
        video_download = ctk.CTkButton(master=tab.tab("Video"), text="Download", command=startDownloadVideo)
        video_download.pack(padx=10, pady=20)
        
        
        ############################## Audio #############################
        
        
        # Download Function
        def startDownloadAudio():
            try:
                audio_finish_label.configure(text="")
                
                audio_link_yt = audio_link.get()
                audio_file_name_yt = audio_file_name.get()
                audio_file_extension_yt = audio_file_extension.get()
                
                audio_ytObject = YouTube(audio_link_yt, on_progress_callback=on_progress)
                audio = audio_ytObject.streams.get_audio_only()
                audio.download(filename=audio_file_name_yt+"."+audio_file_extension_yt)
            except:
                audio_finish_label.configure(text="YouTube link is invalid")
            audio_finish_label.configure(text="Downloaded!")
            
        
        # Progress Bar Function
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            per = str(int(percentage_of_completion))
            audio_pPercentage.configure(text=per + "%")
            audio_pPercentage.update()
            
            audio_progressBar.set(float(percentage_of_completion) / 100)
            
        
        # Audio Label
        audio_label = ctk.CTkLabel(master=tab.tab("Audio"), text="-- YouTube Audio Downloader --")
        audio_label.pack(padx=10, pady=10)
        
        # Audio input
        audio_link = ctk.CTkEntry(master=tab.tab("Audio"), width=350, height=40, placeholder_text="YouTube Link")
        audio_link.pack(padx=10, pady=10)
        
        # Audio file name
        audio_file_name = ctk.CTkEntry(master=tab.tab("Audio"), width=350, height=40, placeholder_text="File Name")
        audio_file_name.pack(padx=10, pady=10)
        
        # Audio File Extension
        audio_file_extension = ctk.CTkEntry(master=tab.tab("Audio"), width=350, height=40, placeholder_text="File Extension: mp3, avi, webm etc...")
        audio_file_extension.pack(padx=10, pady=10)
        
        # Audio Finished label
        audio_finish_label = ctk.CTkLabel(master=tab.tab("Audio"), text="")
        audio_finish_label.pack()
        
        # Audio Progress Percentage
        audio_pPercentage = ctk.CTkLabel(master=tab.tab("Audio"), text="%0")
        audio_pPercentage.pack()
        
        audio_progressBar = ctk.CTkProgressBar(master=tab.tab("Audio"), width=400)
        audio_progressBar.set(0)
        audio_progressBar.pack(padx=10, pady=10)
               
        # Audio Download Button
        audio_download = ctk.CTkButton(master=tab.tab("Audio"), text="Download", command=startDownloadAudio)
        audio_download.pack(padx=10, pady=20)        
        
if __name__ == "__main__":
    app = YT_Downloader()
    app.mainloop()