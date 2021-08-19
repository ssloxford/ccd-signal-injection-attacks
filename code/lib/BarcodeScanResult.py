class BarcodeScanResult():

    def __init__(self, freq, exposure, camera_gain, total_detected, total_correct, frames_collected, expected_barcodes):
        # If freq is 0, no attack happened
        self.freq = freq
        self.exposure = exposure
        self.camera_gain = camera_gain
        self.detected = total_detected
        self.wrong = total_detected - total_correct
        self.correct_detected = total_correct
        self.expected_barcodes = frames_collected * expected_barcodes
        self.missed = max(0, self.expected_barcodes - total_detected)
        self.appeared = max(0, total_detected - self.expected_barcodes)
        self.frames_collected = frames_collected
        self.detection_rate = (self.correct_detected / self.expected_barcodes) * 100
        
    def to_dict(self):
        return self.__dict__