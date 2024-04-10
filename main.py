import pygame
import os
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Simple Music Player")

        self.playlist = []
        self.current_track_index = 0

        # Create buttons
        self.play_button = tk.Button(master, text="Play", command=self.play, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.stop_button.pack(pady=5)

        self.prev_button = tk.Button(master, text="Previous", command=self.prev_track, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.next_button = tk.Button(master, text="Next", command=self.next_track, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.load_button = tk.Button(master, text="Load Playlist", command=self.load_playlist, font=('Helvetica', 12), bg='#FFD700', fg='#000000')
        self.load_button.pack(pady=5)

    def load_playlist(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        self.playlist = list(file_paths)

    def play(self):
        if not self.playlist:
            return
        pygame.mixer.init()  # Initialize mixer
        pygame.mixer.music.load(self.playlist[self.current_track_index])
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    player = MusicPlayer(root)
    root.mainloop()
