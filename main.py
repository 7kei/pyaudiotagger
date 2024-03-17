import tkinter
import os
import music_tag
import io

from PIL import Image, ImageTk
from tkinter import ttk, filedialog

class taggerGui():

    songInfo = None

    def __init__(self):
        rootGui = tkinter.Tk()
        rootGui.title("Python Audio Tagger")
        rootGui.geometry("1280x720")

        mainFrame = tkinter.Frame(rootGui)

        self.artSrc = Image.open(os.path.dirname(__file__) + "\\images\\art_placeholder.png")
        self.art = self.artSrc.resize((500, 500))
        self.ttkArt = ImageTk.PhotoImage(self.art)
        self.ttkArtLabel = ttk.Label(mainFrame, image=self.ttkArt)
        self.ttkArtLabel.grid(row=0, column=0, rowspan=8, padx=100, pady=100)

        titleLabel = ttk.Label(mainFrame, text="Track Title: ")
        titleLabel.grid(row=0, column=1, padx=25)
        self.titleEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.titleEntry.grid(row=0, column=2)

        albumLabel = ttk.Label(mainFrame, text="Album Title: ")
        albumLabel.grid(row=1, column=1)
        self.albumEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.albumEntry.grid(row=1, column=2)

        songArtistLabel = ttk.Label(mainFrame, text="Song Artist: ")
        songArtistLabel.grid(row=2, column=1)
        self.songArtistEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.songArtistEntry.grid(row=2, column=2)

        albumArtistLabel = ttk.Label(mainFrame, text="Album Artist: ")
        albumArtistLabel.grid(row=3, column=1)
        self.albumArtistEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.albumArtistEntry.grid(row=3, column=2)

        yearLabel = ttk.Label(mainFrame, text="Year: ")
        yearLabel.grid(row=4, column=1)
        self.yearEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.yearEntry.grid(row=4, column=2)

        genreLabel = ttk.Label(mainFrame, text="Genre: ")
        genreLabel.grid(row=5, column=1)
        self.genreEntry = ttk.Entry(mainFrame, state=tkinter.DISABLED, width=50)
        self.genreEntry.grid(row=5, column=2)

        trackNumberFrame = ttk.Frame(mainFrame)

        trackNumberLabel = ttk.Label(trackNumberFrame, text="Track ")
        trackNumberLabel.grid(row=0, column=0)
        self.trackNumberEntry = ttk.Entry(trackNumberFrame, state=tkinter.DISABLED, width=5)
        self.trackNumberEntry.grid(row=0, column=1)

        totalTrackNumberLabel = ttk.Label(trackNumberFrame, text=" of ")
        totalTrackNumberLabel.grid(row=0, column=2)
        self.totalTrackNumberEntry = ttk.Entry(trackNumberFrame, state=tkinter.DISABLED, width=5)
        self.totalTrackNumberEntry.grid(row=0, column=3)

        trackNumberFrame.grid(row=6, column=1, columnspan=2)

        discNumberFrame = ttk.Frame(mainFrame)

        discNumberLabel = ttk.Label(discNumberFrame, text="Disc ")
        discNumberLabel.grid(row=0, column=0)
        self.discNumberEntry = ttk.Entry(discNumberFrame, state=tkinter.DISABLED, width=5)
        self.discNumberEntry.grid(row=0, column=1)

        totalDiscNumberLabel = ttk.Label(discNumberFrame, text=" of ")
        totalDiscNumberLabel.grid(row=0, column=2)
        self.totalDiscNumberEntry = ttk.Entry(discNumberFrame, state=tkinter.DISABLED, width=5)
        self.totalDiscNumberEntry.grid(row=0, column=3)

        discNumberFrame.grid(row=7, column=1, columnspan=2)

        self.loadAlbumArtButton = ttk.Button(mainFrame, text="Load Album Art", command=self.load_album_art, state=tkinter.DISABLED)
        self.loadAlbumArtButton.grid(row=0, column=0)

        loadSaveFrame = tkinter.Frame(mainFrame)
        
        self.loadButton = ttk.Button(loadSaveFrame, text="Load Song", command=self.load_song)
        self.loadButton.grid(row=0, column=0)
        self.saveButton = ttk.Button(loadSaveFrame, text="Save Song", command=self.save_song, state=tkinter.DISABLED)
        self.saveButton.grid(row=0, column=1)

        loadSaveFrame.grid(row=7, column=0)

        mainFrame.pack()

        rootGui.mainloop()

    def load_album_art(self):
        filetypes = (
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg"),
            ("JPEG files", "*.jpeg"),
            ("All files", "*.*")
        )

        file = tkinter.filedialog.askopenfilename(title="Open a picture for the album art.", filetypes=filetypes)

        if file is not None:
            try:
                sArt = Image.open(file)
            except Exception as e:
                tkinter.messagebox.showerror(title="Error!", message=f"Invalid file inputted.\n{type(e)}\n{e}")
                return
            
            ssArt = sArt.resize((500, 500))
            ssTtkArt = ImageTk.PhotoImage(ssArt)
            self.ttkArtLabel.configure(image=ssTtkArt)
            self.ttkArtLabel.image = ssTtkArt

            with open(file, 'rb') as img_in:
                self.songInfo['artwork'] = img_in.read()

    def load_song(self):
        filetypes = (
            ("MP3 files", "*.mp3"),
            ("FLAC files", "*.flac"),
            ("OGG files", "*.ogg"),
            ("WAV files", "*.wav"),
            ("All files", "*.*")
        )

        file = tkinter.filedialog.askopenfilename(title="Open an audio file.", filetypes=filetypes)

        if file != '':
            try:
                self.songInfo = music_tag.load_file(file)
            except Exception as e:
                tkinter.messagebox.showerror(title="Error!", message=f"Invalid file inputted.\n{type(e)}\n{e}")
                return

            if self.songInfo['artwork'].first is not None:
                sArt = Image.open(io.BytesIO(self.songInfo['artwork'].first.data))
            else:
                sArt = Image.open(os.path.dirname(__file__) + "\\images\\art_placeholder.png")
            ssArt = sArt.resize((500, 500))
            ssTtkArt = ImageTk.PhotoImage(ssArt)
            self.ttkArtLabel.configure(image=ssTtkArt)
            self.ttkArtLabel.image = ssTtkArt

            self.titleEntry.configure(state=tkinter.NORMAL)
            self.titleEntry.delete(0, tkinter.END)
            self.titleEntry.insert(0, self.songInfo['tracktitle'])

            self.albumEntry.configure(state=tkinter.NORMAL)
            self.albumEntry.delete(0, tkinter.END)
            self.albumEntry.insert(0, self.songInfo['album'])

            self.songArtistEntry.configure(state=tkinter.NORMAL)
            self.songArtistEntry.delete(0, tkinter.END)
            self.songArtistEntry.insert(0, self.songInfo['artist'])

            self.albumArtistEntry.configure(state=tkinter.NORMAL)
            self.albumArtistEntry.delete(0, tkinter.END)
            self.albumArtistEntry.insert(0, self.songInfo['albumartist'])

            self.yearEntry.configure(state=tkinter.NORMAL)
            self.yearEntry.delete(0, tkinter.END)
            self.yearEntry.insert(0, self.songInfo['year'])

            self.genreEntry.configure(state=tkinter.NORMAL)
            self.genreEntry.delete(0, tkinter.END)
            self.genreEntry.insert(0, self.songInfo['genre'])

            self.trackNumberEntry.configure(state=tkinter.NORMAL)
            self.trackNumberEntry.delete(0, tkinter.END)
            self.trackNumberEntry.insert(0, self.songInfo['tracknumber'])

            self.totalTrackNumberEntry.configure(state=tkinter.NORMAL)
            self.totalTrackNumberEntry.delete(0, tkinter.END)
            self.totalTrackNumberEntry.insert(0, self.songInfo['totaltracks'])

            self.discNumberEntry.configure(state=tkinter.NORMAL)
            self.discNumberEntry.delete(0, tkinter.END)
            self.discNumberEntry.insert(0, self.songInfo['discnumber'])

            self.totalDiscNumberEntry.configure(state=tkinter.NORMAL)
            self.totalDiscNumberEntry.delete(0, tkinter.END)
            self.totalDiscNumberEntry.insert(0, self.songInfo['totaldiscs'])

            self.saveButton.configure(state=tkinter.NORMAL)
            self.loadAlbumArtButton.configure(state=tkinter.NORMAL)
    
    def save_song(self):

        self.songInfo['tracktitle'] = str(self.titleEntry.get())
        self.songInfo['album'] = str(self.albumEntry.get())
        self.songInfo['artist'] = str(self.songArtistEntry.get())
        self.songInfo['albumartist'] = str(self.albumArtistEntry.get())

        if str(self.yearEntry.get()).isnumeric() is True:
            self.songInfo['year'] = str(self.yearEntry.get())

        self.songInfo['genre'] = str(self.genreEntry.get())

        if str(self.trackNumberEntry.get()).isnumeric() is True:
            self.songInfo['tracknumber'] = str(self.trackNumberEntry.get())
        if str(self.totalTrackNumberEntry.get()).isnumeric() is True:
            self.songInfo['totaltracks'] = str(self.totalTrackNumberEntry.get())
        if str(self.discNumberEntry.get()).isnumeric() is True:
            self.songInfo['discnumber'] = str(self.discNumberEntry.get())
        if str(self.totalDiscNumberEntry.get()).isnumeric() is True:
            self.songInfo['totaldiscs'] = str(self.totalDiscNumberEntry.get())

        try:
            self.songInfo.save()
        except Exception as e:
            tkinter.messagebox.showerror(title="Error!", message=f"Cannot save file.\n{type(e)}\n{e}")
            return

if __name__ == "__main__":
    taggerGui()