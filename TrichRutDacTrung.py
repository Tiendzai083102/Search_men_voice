from pydub import AudioSegment
import numpy as np

'''
    Trích rút đặc trưng
'''
def features(file):
    audio_file = readFileAudio(file)
    frames = audioFraming(audio_file)
    features = []
    for frame in frames:
        if(checkSilence(frame)):
            z = zeroCrossingRate(frame)
            ae = averageEnergy(frame)
            af = averageFrequency(frame)
            vf = frequencyVariation(frame)
            sc = spectralCentroid(frame)
            features.append([ae, z, af, vf, sc])
    return features

'''
    Sử dụng AudioSegment để đọc file âm thanh từ đường dẫn
'''
def readFileAudio(fileName):
    # Load audio file
    audio_file = AudioSegment.from_file(fileName)

    # Convert to mono channel
    audio_file = audio_file.set_channels(1)

    return audio_file

'''
    Chia file âm thanh thành các đoạn có độ dài 0.5s, mỗi đoạn cách nhau 0.25s
    VD: file âm thanh 10s -> Chia được thành 39 frame
'''
def audioFraming(audio_file):
    # Set frame length and hop length in milliseconds
    frame_length = 25 #Do dai: 0.5s
    hop_length =  17.5#Khoang cach giua cac frame: 0.25s

    # Calculate number of frames
    num_frames = int(len(audio_file) / hop_length) - 1

    # Initialize empty list for frames
    frames = []

    # Cut audio file into frames
    for i in range(num_frames):
        start_time = i * hop_length
        end_time = start_time + frame_length
        frame = audio_file[start_time:end_time]
        frames.append(frame)
    
    return frames

'''
    Kiểm tra đoạn âm thanh có phải im lặng ko
    Nếu >= 80% đoạn âm thanh im lặng thì đoạn âm thanh đó im lặng
'''
def checkSilence(audio):
    samples = np.array(audio.get_array_of_samples())

    # ngưỡng độ lớn tạm dừng (silence threshold)
    threshold = 280

    # Tính toán số mẫu (samples) trong file âm thanh có độ lớn dưới ngưỡng độ lớn tạm dừng
    silence_samples = len(np.where(abs(samples) < threshold)[0]) 

    # Tính toán tỷ lệ âm lặng (silence ratio) của file âm thanh
    silence_ratio = silence_samples / len(samples)
    if(silence_ratio >= 0.8):
        return False
    return True

'''
    Tính tốc độ qua điểm 0
'''
def zeroCrossingRate(audio):
    # Extract samples from audio file
    samples = np.array(audio.get_array_of_samples())

    # Calculate zero crossing rate
    zero_crossings = np.where(np.diff(np.sign(samples)))[0]
    zero_crossing_rate = len(zero_crossings) / len(samples)

    # Return zero crossing rate
    return zero_crossing_rate

'''
    Tính năng lượng trung bình
'''
def averageEnergy(audio):
    # Calculate RMS energy
    rms_energy = audio.rms

    # Return RMS energy
    return rms_energy

'''
    Tính tần số trung bình
'''
def averageFrequency(audio):
    # chuyển đổi tín hiệu âm thanh sang miền tần số
    samples = np.array(audio.get_array_of_samples())
    frequencies = np.fft.fftfreq(len(samples), d=1.0/audio.frame_rate)
    spectral = np.fft.fft(samples)

    # tính trung bình các tần số
    avg_freq = np.abs(spectral).dot(np.abs(frequencies)) / np.sum(np.abs(spectral))

    return avg_freq

'''
    Tính độ biến thiên tần số
'''
def frequencyVariation(audio):
    # chuyển đổi tín hiệu âm thanh sang miền tần số
    samples = np.array(audio.get_array_of_samples())
    frequencies = np.fft.fftfreq(len(samples), d=1.0/audio.frame_rate)
    spectral = np.fft.fft(samples)

    # tính độ biến thiên tần số
    diff_freq = np.abs(np.diff(spectral))
    mean_diff_freq = np.mean(diff_freq, axis=0)
    return mean_diff_freq
def spectralCentroid(audio):
    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())
    
    # Compute the Fourier Transform of the audio samples
    spectral = np.fft.fft(samples)
    
    # Compute the frequencies corresponding to the Fourier Transform components
    frequencies = np.fft.fftfreq(len(samples), d=1.0/audio.frame_rate)
    
    # Take the magnitude of the spectral components
    magnitudes = np.abs(spectral)
    
    # Calculate the spectral centroid
    spectral_centroid = np.sum(frequencies * magnitudes) / np.sum(magnitudes)
    
    return spectral_centroid