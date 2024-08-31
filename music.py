import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the mixer
mixer.init()

# Function to browse and select an MP3 file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

# Function to play the selected music file
def play_music():
    filename = file_entry.get()
    if filename:
        mixer.music.load(filename)
        mixer.music.play()

# Function to pause the music
def pause_music():
    mixer.music.pause()

# Function to resume the music
def resume_music():
    mixer.music.unpause()

# Function to stop the music
def stop_music():
    mixer.music.stop()

# Function to adjust the volume
def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

# Create the main window
root = tk.Tk()
root.title("Music Player")

# Create and place the file entry field
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=0, padx=10, pady=10)

# Create and place the browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Create and place the control buttons
play_button = tk.Button(root, text="Play", command=play_music)
play_button.grid(row=1, column=0, padx=10, pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.grid(row=1, column=1, padx=10, pady=10)

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.grid(row=1, column=2, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.grid(row=1, column=3, padx=10, pady=10)

# Create and place the volume scale
volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(50)  # Set the default volume to 50%
volume_scale.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
