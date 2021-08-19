import sys
sys.path.append("/home/code/lib/")

from SignalEmitter import SignalEmitter
from EvaluationUtils import EvaluationUtils
import numpy as np
from scipy import signal
import argparse

def interpolate_attack_signal(attack_signal, input_image):
    # Interpolation Factor used to match the attack signal symbol rate to the USRP sample rate
    interpolation_factor = 2.657874685
  
    # Resample the attack signal using the interpolation factor specified above
    resampled = signal.resample(attack_signal, int(len(attack_signal)*interpolation_factor))
    # Save the resampled signal to a file
    resampled.tofile(f'{input_image}.dat')
    
    return resampled

def run_attack_chain(fc, input_image, sample_rate, sdr_gain, duration):
    # Extract the attack signal from an input image
    attack_signal = EvaluationUtils.sample_input_image(input_image)
    # Resample the attack signal
    attack_signal = interpolate_attack_signal(attack_signal, input_image)
    # Emit the attack signal with the USRP
    SignalEmitter.emit_attack_signal_from_file(fc, sample_rate, sdr_gain, f'{input_image}.dat', duration)
    
    
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='Run a signal injection attack against a CCD Image Sensor End-2-End.')
    parser.add_argument('--freq', '-f', type=int, help='Carrier Wave Frequency (fc).', required=True)
    parser.add_argument('--input_image', '-i', type=str, help='Path to the input image that will be injected.', required=True)
    parser.add_argument('--sample_rate', '-s', type=int, help='Sample Rate of the USRP.', required=False, default=50)
    parser.add_argument('--duration', '-d', type=int, help='Attack duration in seconds.', required=False, default=10)
    parser.add_argument('--sdr_gain', '-g', type=int, help='Gain of the USRP. Maximum is 32.', required=False, default=0)
    args = parser.parse_args()
    
    run_attack_chain(args.freq, args.input_image, args.sample_rate, args.sdr_gain, args.duration)
