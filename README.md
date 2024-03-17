# pyaudiotagger (A Python Audio Tagger GUI)

## About

This is a school project. It provides a GUI for manipulating audio metadata. It uses [music_tag](https://pypi.org/project/music-tag/) as the metadata library and [Tkinter](https://docs.python.org/3/library/tkinter.html) as the GUI library.

## Usage

### Requirements

- Python 3.12.2
- [music_tag](https://pypi.org/project/music-tag/)
- A supported audio file.

### Supported audio files

The program supports whatever the [music_tag](https://pypi.org/project/music-tag/) library supports. As of music_tag 0.4.3, the library supports:

- aac
- aiff
- dsf
- flac
- m4a
- mp3
- ogg
- opus
- wav
- wv

### How to Use

1. Install the required libraries:
    - `pip install -r requirements.txt`
2. Open the main.py file.
3. Load an audio file using the "Load Song" button.
4. Manipulate the tags based on the GUI.
5. Save an audio file using the "Save Song" button.

## License

This project uses the MIT license. [Learn more here.](https://choosealicense.com/licenses/mit/)