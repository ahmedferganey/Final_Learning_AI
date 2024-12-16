import sounddevice as sd
import numpy as np
import time
from ring_buffer import RingBuffer


class AudioInputHandler:
    """
    Captures live audio and buffers it into a RingBuffer.
    
    This class is responsible for:
    - Capturing live audio data from the default input device.
    - Using a callback mechanism to process audio chunks in real-time.
    - Writing audio data into a thread-safe RingBuffer to ensure non-blocking audio handling.
    - Allowing access to buffered audio data for further analysis or processing.
    """
    
    def __init__(self):
        """
        Initializes the AudioInputHandler instance.
        
        Sets up a RingBuffer with a maximum size that corresponds to approximately
        10 seconds of audio data at a 16 kHz sampling rate. This buffer will store
        audio chunks received from the live audio stream.
        """
        self.ring_buffer = RingBuffer(max_size=160000)  # 10 seconds at 16kHz sampling rate

    def audio_callback(self, indata, frames, time, status):
        """
        Callback function to handle incoming audio data from the live audio stream.
        
        Args:
            indata (numpy.ndarray): The incoming audio chunk data from the audio stream.
            frames (int): The number of audio frames in the chunk.
            time (TimeStruct): Timestamp-related information.
            status (AudioStreamStatus): Status information about the audio stream.
        
        Functionality:
            - Logs the audio stream status if an issue occurs.
            - Extracts only the mono audio channel from the stereo input (or defaults if single-channel).
            - Ignores silent chunks by checking the audio amplitude threshold (0.01).
            - Writes valid, non-empty audio data into the RingBuffer for processing or analysis.
        """
        if status:  # Log audio stream status if any error/warning is encountered
            print(f"Audio stream status: {status}")

        # Extract mono audio data from the first channel (assume single-channel input stream)
        audio_data = indata[:, 0]
        
        # Avoid saving audio chunks that are silent (below a given threshold)
        if np.max(np.abs(audio_data)) > 0.01:
            # Write valid audio data into the ring buffer
            self.ring_buffer.write(audio_data.copy())
            print(f"Buffered audio chunk: {audio_data[:10]}")  # Log first 10 values of the chunk for debugging purposes

    def get_ring_buffer(self):
        """
        Provides external access to the RingBuffer instance.

        Returns:
            RingBuffer: The ring buffer instance that stores audio data captured by the callback.
        """
        return self.ring_buffer

    def stream_audio(self):
        """
        Sets up and runs the live audio stream using sounddevice's InputStream.

        This function performs the following:
            - Sets up the audio stream with specific sampling rate, buffer size, and audio channels.
            - Attaches the `audio_callback` method to handle incoming audio chunks.
            - Keeps the application running in a loop to maintain continuous audio streaming.
        """
        with sd.InputStream(
            samplerate=16000,         # Sampling rate set at 16 kHz
            blocksize=1024,          # Number of frames processed per callback
            dtype="float32",         # Data type for the audio stream
            channels=1,              # Mono audio stream
            callback=self.audio_callback  # Set the callback function for processing audio
        ):
            print("Listening for live audio...")
            
            # Keep the application running to maintain the audio stream.
            # The time.sleep() prevents busy looping.
            while True:
                time.sleep(0.1)
