import uhd
import numpy as np

# Wrapper class for the UHD Python Library
class SignalEmitter:
    
    waveforms = {
    "sine": lambda n, tone_offset, rate: np.exp(n * 2j * np.pi * tone_offset / rate),
    "square": lambda n, tone_offset, rate: np.sign(SignalEmitter.waveforms["sine"](n, tone_offset, rate)),
    "const": lambda n, tone_offset, rate: 1 + 1j,
    "ramp": lambda n, tone_offset, rate:
            2*(n*(tone_offset/rate) - np.floor(float(0.5 + n*(tone_offset/rate))))
    }
    
    # This method emits samples from an numpy array at a carrier frequency fc (in MHz) 
    # with a gain of sdr_gain and a sample rate of sample_rate (in MSPS)
    # for a given duration in seconds
    def emit_attack_signal_from_data(fc, sample_rate, sdr_gain, data, duration):

        channels = [0]
        freq = fc * 1e6
        sample_rate = sample_rate * 1e6
        duration = float(duration)

        usrp = uhd.usrp.MultiUSRP()

        usrp.send_waveform(data, duration, freq, sample_rate, channels, sdr_gain)
    
    # This method emits samples from a file at a carrier frequency fc (in MHz) 
    # with a gain of sdr_gain and a sample rate of sample_rate (in MSPS)
    # for a given duration in seconds
    def emit_attack_signal_from_file(fc, sample_rate, sdr_gain, file, duration):

        channels = [0]
        freq = fc * 1e6
        sample_rate = sample_rate * 1e6
        duration = float(duration)

        usrp = uhd.usrp.MultiUSRP()

        data = np.fromfile(file, dtype=np.complex64)
        usrp.send_waveform(data, duration, freq, sample_rate, channels, sdr_gain)

        
    # This method emits random noise at a carrier frequency fc (in MHz) 
    # with a gain of sdr_gain and a sample rate of sample_rate (in MSPS)
    # for a given duration in seconds
    def emit_random_noise(fc, sample_rate, sdr_gain, duration):

        channels = [0]
        freq = fc * 1e6
        sample_rate = sample_rate * 1e6
        duration = float(duration)

        usrp = uhd.usrp.MultiUSRP()

        data = np.random.normal(loc=0, scale=np.sqrt(2)/2, size=(1000000, 2)).view(np.complex64)
        usrp.send_waveform(data, duration, freq, sample_rate, channels, sdr_gain)
        
        
    # This method emits a sine wave with frequency wave_freq (in kHz) at a carrier frequency fc (in MHz) 
    # with a gain of sdr_gain and a sample rate of sample_rate (in MSPS)
    # for a given duration in seconds
    def emit_wave(fc, sample_rate, wave_freq, sdr_gain, duration):

        waveform = "sine"
        channels = [0]
        freq = fc * 1e6
        sample_rate = sample_rate * 1e6
        duration = float(duration)
        wave_freq = wave_freq * 1e3
        wave_ampl = 10

        usrp = uhd.usrp.MultiUSRP()
        data = np.array(
            list(map(lambda n: wave_ampl * SignalEmitter.waveforms[waveform](n, wave_freq, sample_rate), 
            np.arange(int(10 * np.floor(sample_rate / wave_freq)), dtype=np.complex64))), dtype=np.complex64)

        usrp.send_waveform(data, duration, freq, sample_rate, channels, sdr_gain)