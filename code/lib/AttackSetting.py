class AttackSetting:
    
    camera = ""
    distance = 0
    fc = 0
    wave_freq = 0
    camera_gain = 0.0
    sdr_gain = 0
    
    previous = ""
    current = ""
    
    def __init__(self, camera, distance, fc, wave_freq, camera_gain, sdr_gain, previous="", current=""):
        self.camera = camera
        self.distance = distance
        self.fc = fc
        self.wave_freq = wave_freq
        self.camera_gain = camera_gain
        self.sdr_gain = sdr_gain
        self.previous = previous
        self.current = current
    
    def to_dict(self):
        return self.__dict__
        
        
class AttackResult(AttackSetting):
    
    ssim = 0.0
    ms_ssim = 0.0
    linf = 0.0
    l1 = 0.0
    l2 = 0.0
    uqi = 0.0
    
    def __init__(self, attack_setting):
        super().__init__(attack_setting.camera, attack_setting.distance, attack_setting.fc, attack_setting.wave_freq, attack_setting.camera_gain, attack_setting.sdr_gain, attack_setting.previous, attack_setting.current)
        
    def to_dict(self):
        return self.__dict__
    
    def print(self):
        print(f"For camera {self.camera}, distance {self.distance}cm, fc {self.fc}MHz, wave freq {self.wave_freq}, camera gain {self.camera_gain}, SDR gain {self.sdr_gain}")
        
        
