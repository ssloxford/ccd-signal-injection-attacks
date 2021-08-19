class ImageMetrics:
    
    camera = ""
    distance = 0
    fc = 0
    wave_freq = 0
    camera_gain = 0
    sdr_gain = 0
    
    ssim_min = 0
    ssim_mean = 0
    ssim_max = 0
    ssim_median = 0
    ssim_std = 0
    
    ms_ssim_min = 0
    ms_ssim_mean = 0
    ms_ssim_max = 0
    ms_ssim_median = 0
    ms_ssim_std = 0
    
    linf_min = 0
    linf_mean = 0
    linf_max = 0
    linf_median = 0
    linf_std = 0
    
    l1_min = 0
    l1_mean = 0
    l1_max = 0
    l1_median = 0
    l1_std = 0
    
    l2_min = 0
    l2_mean = 0
    l2_max = 0
    l2_median = 0
    l2_std = 0
    
    uqi_min = 0
    uqi_mean = 0
    uqi_max = 0
    uqi_median = 0
    uqi_std = 0
    
    values = 0
    
    def __init__(self, camera):
        self.camera = camera
    
    def to_dict(self):
        return self.__dict__