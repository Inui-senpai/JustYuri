#==================================================#
#  Just Yuri Mod - Detection System
#==================================================#
#  This file is responsible for Yuri's ability to 
#  detect windows in any supported oses.
#  
#  :D
#==================================================#

init -996 python:
    class DetectionAPI:
        detector = None
        ticks = 0

        @staticmethod
        def tick():
            if DetectionAPI.ticks % 200 == 0:
                pass
            DetectionAPI.ticks += 1

        @staticmethod
        def get_active_window():
            if not DetectionAPI.detector:
                return None
            return DetectionAPI.detector.get_active_window()
        
        @staticmethod
        def get_windows():
            if not DetectionAPI.detector:
                return []
            return DetectionAPI.detector.get_windows()

    class WindowObject:
        id = None
        title = None
        active = False
        minimized = False
        background = False
        def __init__(self, id, title):
            self.id = id
            self.title = title

    class Detector:
        def get_active_window(self):
            pass
        def get_windows(self):
            pass
    
    class WindowsDetector(Detector):
        @staticmethod
        def create(id):
            if not id:
                return None
            window = WindowObject(id, None)
            length = user32.GetWindowTextLengthW(window.id)
            if not length:
                window.title = str(id)
            else:
                buffer = ctypes.create_unicode_buffer(length := length + 1)
                user32.GetWindowTextW(window.id, buffer, length)
                window.title = str(buffer.value)
            window.minimized = user32.IsIconic(window.id) == 1
            window.background = user32.IsWindowVisible(window.id) == 0
            return window

        def get_active_window(self):
            if not persistent.enable_window_detection:
                return None
            window = WindowsDetector.create(user32.GetForegroundWindow())
            if not window:
                return None
            window.active = True
            return window

        def get_windows(self):
            if not persistent.enable_window_detection:
                return None
            windows = []
            active_window_id = user32.GetForegroundWindow()
            def callback(hwnd: int, lparam: int) -> bool:
                window = WindowsDetector.create(hwnd)
                if window:
                    window.active = window.id == active_window_id
                    windows.append(window)
                return True
            user32.EnumWindows(win_callback(callback), wintypes.LPARAM(0))
            return windows

    if renpy.windows:
        DetectionAPI.detector = WindowsDetector()
        