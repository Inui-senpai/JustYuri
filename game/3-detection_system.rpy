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
            
    
    class BetterLinuxDetector(Detector):
        @staticmethod
        def create(window):
            window_obj = WindowObject(window.getPID(), window.title)
            window_obj.active = window.isActive
            window_obj.minimized = window.isMinimized
            window_obj.background = window.isVisible
            return window_obj
            
        def get_active_window(self):
            window = pywinctl.getActiveWindow()
            if not window:
                return None
            return BetterLinuxDetector.create(window)

        def get_windows(self):
            windows = []
            all_windows = pywinctl.getAllWindows()
            for window in all_windows:
                windows.append(BetterLinuxDetector.create(window))
            return windows

    class LinuxDetector(Detector):
        @staticmethod
        def create(id):
            window = WindowObject(id, id)
            output = subprocess.check_output(["xprop", "-id", id, "WM_NAME", "_NET_WM_NAME", "_NET_WM_STATE", "_NET_ACTIVE_WINDOW"]).decode("utf-8")
            name = None

            for line in output.splitlines():
                if "WM_NAME" in line:
                    if not "not found" in line:
                        name = line
                elif "_NET_WM_NAME" in line:
                    if not "not found" in line:
                        name = line
                elif "_NET_WM_STATE" in line:
                    if not "not found" in line:
                        window.minimized = "_NET_WM_STATE_HIDDEN" in output
            
            if name:
                name = name.split("= ")[1]
                name = regex.sub("^\"", "", name)
                window.title = regex.sub("\"$", "", name)
            else:
                window.background = True

            return window

        @staticmethod
        def get_active_id():
            output = subprocess.check_output(["xprop", "-root", "_NET_ACTIVE_WINDOW"]).decode("utf-8")
            if "not found" in output.lower():
                return None
            return output.split("# ")[1].split(", ")[0]
            
        def get_active_window(self):
            id = LinuxDetector.get_active_id()
            if id:
                window = LinuxDetector.create(id)
                window.active = True
                return window
            return None

        def get_windows(self):
            windows = []
            active_window_id = LinuxDetector.get_active_id()
            output = subprocess.check_output(["xwininfo", "-root", "-tree"]).decode("utf-8")
            for line in output.splitlines():
                line = regex.sub("^\s*", "", line)
                line = regex.sub(" .*", "", line)
                if regex.match("^0x", line):
                    window = LinuxDetector.create(line)
                    windows.append(window)
            return windows

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
    elif renpy.linux:
        display_session_type = os.environ.get("XDG_SESSION_TYPE")
        if display_session_type == "x11":
            DetectionAPI.detector = BetterLinuxDetector()
        elif display_session_type == "wayland":
            DetectionAPI.detector = LinuxDetector()
        
        