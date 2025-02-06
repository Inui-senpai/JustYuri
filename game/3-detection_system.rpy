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

    class LinuxDetector(Detector):
        @staticmethod
        def create(window):
            id = window.get_full_property(linux_display.intern_atom("_NET_WM_PID", False), 0)
            if not id:
                return None

            window_obj = WindowObject(id.value[0], str(id.value[0]))
            name = window.get_full_property(linux_display.intern_atom("WM_NAME", False), 0)
            if not name:
                name = window.get_full_property(linux_display.intern_atom("_NET_WM_NAME", False), 0)

            if name:
                window_obj.title = name.value.decode("utf-8")
            else:
                window_obj.background = True
            
            state_prop = window.get_wm_state()
            if state_prop:
                window_obj.minimized = state_prop.state == IconicState

            return window_obj
        
        @staticmethod
        def get_children(window, active_id, windows):
            window_obj = LinuxDetector.create(window)
            if window_obj:
                window_obj.active = True if active_id and window_obj.id == active_id else False
                windows.append(window_obj)

            children = window.query_tree().children
            for child in children:
                LinuxDetector.get_children(child, active_id, windows)


        def get_active_window(self):
            if not persistent.enable_window_detection:
                return None

            active_windows = linux_root.get_full_property(linux_display.intern_atom("_NET_ACTIVE_WINDOW"), 0)
            if not active_windows:
                return None

            window = LinuxDetector.create(linux_display.create_resource_object("window", active_windows.value[0]))
            if not window:
                return None

            window.active = True
            return window

        def get_windows(self):
            if not persistent.enable_window_detection:
                return []

            windows = []
            active_window = self.get_active_window()
            children = linux_root.query_tree().children
            for child in children:
                LinuxDetector.get_children(child, active_window.id if active_window else None, windows)
                
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
                return []
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
    persistent.enable_window_detection = True
    if renpy.windows:
        DetectionAPI.detector = WindowsDetector()
    elif renpy.linux:
        DetectionAPI.detector = LinuxDetector()