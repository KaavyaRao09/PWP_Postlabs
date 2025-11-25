# import soundfile as sf
# import matplotlib.pyplot as plt
# import numpy as np
# from pydub import AudioSegment

# # Load audio file
# audio, sample_rate = sf.read(r'E:\Marwadi\B.Tech\SEM 3\Python\Lab Manual\audio.wav')
# sf.write(r'new_audio_file.wav', audio, sample_rate)

# Load audio file
#audio, sample_rate = sf.read('audio_file.wav')
# Create time axis
# time = np.arange(0, len(audio)) / sample_rate
# # Plot audio signal
# plt.plot(time, audio)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.show()


# Add fade in effect
# audio_fade_in = audio.fade_in(2000)  # 2 seconds

# Export audio file with fade in effect
# audio_fade_in.export('audio_file_fade_in.wav', format='wav')

