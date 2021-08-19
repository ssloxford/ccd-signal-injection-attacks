import glob
import sys
sys.path.append("../lib/")

import pandas as pd
import os
import numpy as np
import cv2

class EvaluationUtils:
    
    # This method takes an object, converts it into a dict and stores it into a CSV file
    def save_results(file_name, results):
        if len(results) > 0:
            data_frame = pd.DataFrame(columns=results[0].to_dict().keys())
            for result in results:
                data_frame = data_frame.append(result.to_dict(), ignore_index=True)

            # Check if file exists, if so, append the file.
            # If not, create a new one.
            if os.path.isfile(file_name):
                data_frame.to_csv(file_name, mode='a', header=False, index=False)
            else:
                data_frame.to_csv(file_name, index=False)
                
                    
    # This method checks if an image metric has already been calculated to prevent duplicates 
    def check_if_image_metrics_already_calculated(file_name, attack_setting):
        if os.path.isfile(file_name):
            data = pd.read_csv(file_name, delimiter=",")
            number_of_entries = len(data.loc[(data['camera'] == attack_setting.camera) & (data['distance'] == attack_setting.distance) & (data['fc'] == attack_setting.fc) & (data['wave_freq'] == attack_setting.wave_freq) & (data['camera_gain'] == attack_setting.camera_gain) & (data['sdr_gain'] == attack_setting.sdr_gain)])
            if number_of_entries > 0:
                return True
        return False
     
        
    # This method reads all legitimate and malicious frames from a given path    
    def get_all_frames_at(path):
        legitimate_frames_path = f"{path}/l_*.png"
        malicious_frames_path = f"{path}/m_*.png"

        legitimate_frames = sorted(glob.glob(legitimate_frames_path))
        malicious_frames = sorted(glob.glob(malicious_frames_path))
        
        return legitimate_frames, malicious_frames
    
    
    # This method takes an input image and extracts an attack signal (i.e., luma Y for each pixel)
    # The extracted values represent the amplitude of the attack signal
    def sample_input_image(image_name, scale=100):
        
        # Camera specific parameters
        camera_resolution_width = 1280
        camera_resolution_height = 980
        camera_resolution = camera_resolution_width * camera_resolution_height

        # Read the input image
        img = cv2.imread(image_name)
        img_height, img_width = img.shape[:2]

        # Optional: Scale the input image 
        width = int(img.shape[1] * scale / 100)
        height = int(img.shape[0] * scale / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Prepare an array where the amplitude values for each pixel will be stored
        amplitude_values = []

        pixel_i = 0
        # Iterate over the pixel rows
        for row_i in range(camera_resolution_height):
            if (pixel_i * row_i) >= camera_resolution:
                break

            # Iterate over the pixel columns
            for pixel_i in range(camera_resolution_width):
                if (pixel_i * row_i) >= camera_resolution:
                    break

                # Check if the current row/column is outside of the input image
                # If so, apply padding
                if pixel_i < width and row_i < height:
                    pixel_row = img[row_i]
                    pixel = pixel_row[pixel_i]

                    # Calculate Luma Y for each pixel of the input image
                    amplitude_values.append(0.2126 * (pixel[0]/255) + 0.7152 * (pixel[1]/255) + 0.0722 * (pixel[2]/255))
                else:
                    # Apply padding, by setting the amplitude of the attack signal to 0
                    amplitude_values.append(0)

        return np.asarray(amplitude_values).astype('float32')