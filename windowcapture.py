import numpy, win32ui, win32con 


class WindowCapture:
    
    # properties
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0 
    offset_x = 0
    offset_y = 0
    
    
    #constructor
    def __init__(self, window_name=None):
        
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        
        else:
            self.hwnd = win32gui.findWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
            
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y
        
    
    def get_screenshot(self):
        
        wDC = win32gui.GetWindowDC(self.hwnd)  # RETURNS DEVICE CONTEXT OF THE WINDOW.
        dcObj = win32ui.CreateDCFromHandle(wDC)  # CREAT A DC OBJECT.
        cDC = dcObj.CreateCompatibleDC()  # 
        