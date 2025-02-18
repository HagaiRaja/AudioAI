import pygame
import time

class AudioPlayer():
    def __init__(self, file_path=None):
        """Initializes the audio player with the given audio file path."""
        self.file_path = file_path
        pygame.mixer.init()
        if file_path != None:
            self.open(file_path)
        self.duration_str, self.duration_seconds = 0, 0
        self.is_playing = False
        self.current_time = 0

    def open(self, file_path):
        """Opens a new audio file."""
        self.file_path = file_path
        pygame.mixer.music.load(self.file_path)
        self.sound = pygame.mixer.Sound(self.file_path)
        self.duration_str, self.duration_seconds = self.get_duration()

    def get_duration(self):
        """Loads audio and returns duration in hh:mm:ss format."""
        duration_seconds = int(self.sound.get_length())
        hh, mm, ss = duration_seconds // 3600, (duration_seconds % 3600) // 60, duration_seconds % 60
        if hh == 0:
            return f"{mm:02}:{ss:02}", duration_seconds
        return f"{hh:02}:{mm:02}:{ss:02}", duration_seconds

    def get_current_time_str(self):
        """Returns the current time in hh:mm:ss format."""
        hh, mm, ss = self.current_time // 3600, (self.current_time % 3600) // 60, self.current_time % 60
        if len(self.duration_str) == 5:
            return f"{mm:02}:{ss:02}"
        return f"{hh:02}:{mm:02}:{ss:02}"

    def play(self, starts=None):
        """Plays the audio file."""
        self.is_playing = True
        if starts is not None:
            self.current_time = starts
            pygame.mixer.music.play(start=starts)
        else:
            pygame.mixer.music.play()

    def pause(self):
        """Pauses the audio playback."""
        self.is_playing = False
        pygame.mixer.music.pause()

    def resume(self):
        """Resumes the audio playback."""
        self.is_playing = True
        pygame.mixer.music.unpause()

    def stop(self):
        """Stops the audio playback."""
        self.is_playing = False
        pygame.mixer.music.stop()

# Example usage
if __name__ == "__main__":
    file_path1 = "sounds/test 1/Vivek Podcast.mp3"
    file_path2 = "sounds/test 1/Jokowi Mata Najwa.mp3"

    audio = AudioPlayer(file_path1)
    
    duration_str, _ = audio.get_duration()
    print("Audio Duration:", duration_str)
    
    audio.play()
    time.sleep(5)  # Play for 5 seconds
    audio.pause()
    time.sleep(2)  # Pause for 2 seconds
    audio.resume()
    time.sleep(3)  # Play for 3 more seconds
    audio.play(10)  # Jump to 10 seconds
    time.sleep(5)  # Play for 5 seconds
    audio.stop()
