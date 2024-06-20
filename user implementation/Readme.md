# 🤖🎬 Audio-to-Text Transcription 🎧📝


### Project Explanation:

Objective:  
The goal is to develop a robust system that listens to someone speaking and accurately writes down what is said.

Scope:  
1. Speech Recognition: The system will recognize different languages and handle various accents and background noises.
2. Technology: It uses advanced algorithms and machine learning techniques to understand and convert speech into text.
3. Real-time Processing: It can work almost instantly, processing speech as it happens, which is useful for live transcription or instant communication.

Usage:  
- Applications: Useful for accessibility (helping people with hearing impairments), creating transcripts of meetings or lectures, and enabling voice commands for devices.
- Implementation: It involves integrating software and possibly hardware (like microphones), ensuring everything works smoothly together.
- Output: The system provides text output that can be stored, edited, or used in other applications.

Deliverable:  
At the end of the project, you'll have a functioning system that turns spoken words into written text accurately and quickly.

### Simplified Example:

Imagine talking to your computer or phone, and it types out everything you say. That's what this project aims to achieve: turning speech into text so you can read or save it.


## Key Features

- User-friendly: Designed for ease of use, the script prompts users to enter a YouTube video URL, minimizing the need for complicated setup processes.
- Efficient Audio Extraction: The script utilizes the `pytube` library to effectively filter and download the audio stream from the specified YouTube video.
- High-Quality Transcription: The `whisper` library, a powerful speech-to-text tool, is employed to accurately transcribe the downloaded audio into text.
- Convenient Output: The transcription is saved as a text file in the same directory as the script, ensuring easy access and sharing capabilities.

## Prerequisites

1. Python 3.6+
2. `pip` to install required libraries

## Required Libraries

- `pytube`: A lightweight Python library that enables the downloading of YouTube videos and the extraction of audio streams.

- `whisper`: An advanced speech-to-text library that facilitates accurate and efficient transcription of audio files.
- `langdetect`: A language detection library ported from Google's language-detection.

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

   ```bash
   pip install pytube
   ```

   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

   ```bash
   pip install langdetect
   ```
 3. Download FFmpeg and add it to environment variables.
   - Windows: https://phoenixnap.com/kb/ffmpeg-windows

   - Mac: https://phoenixnap.com/kb/ffmpeg-mac
   
   - Ubuntu: https://phoenixnap.com/kb/install-ffmpeg-ubuntu

## Usage

1. Run the script:

   ```bash
   python youtube_audio_to_text.py
   ```

2. When prompted, enter the YouTube video URL you wish to transcribe:

   ```
   Enter the YouTube video URL: https://www.youtube.com/watch?v=XXXXXXXXXXX
   ```

3. The script will download the audio, transcribe it, detect language, and save the transcription to a text file called `output_{language}.txt`.

4. Access the transcription by opening the `output_{language}.txt` file located in the same directory as the script.



## Project Flow

1. The user inputs a YouTube video URL when prompted.
2. The `pytube` library is used to create a `YouTube` object and filter the audio stream.
3. The audio stream is downloaded as an MP3 file and saved in the `YoutubeAudios` folder.
4. The `whisper` library loads a base model and transcribes the downloaded audio into text.
5. The `langdetect` library detects the language of the transcribed text.
6. The transcription is saved to a text file named `output_{language}.txt` with the language code as part of the filename and opened for the user to view.

