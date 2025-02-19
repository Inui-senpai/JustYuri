init python:
    import time
    import sys
    import os

    # Construct the absolute path to the python-packages directory
    packages_dir = os.path.join(renpy.config.gamedir, "python-packages")
    sys.path.append(packages_dir)

    from pypresence import Presence

    client_id = '1322302098385276988'  # Replace with your Client ID
    RPC = Presence(client_id)
    connected = False

    def connect_to_discord():
        global connected
        try:
            RPC.connect()
            connected = True
            print("Discord RPC Connected") #Debug message
        except Exception as e:
            print(f"Failed to connect to Discord: {e}") #Debug message
            connected = False

    def update_presence(details="Playing Just Yuri", large_image="icon_large"):
        global connected
        if not connected:
            connect_to_discord()  # Try to connect if not already

        if connected:
            try:
                start_time = int(time.time())
                RPC.update(details=details,
                           large_image=large_image,
                           start=start_time)
                print("Discord RPC Updated") #Debug
            except Exception as e:
                print(f"Failed to update presence: {e}") #Debug message
                connected = False # We probably lost connection, set to false

    def initial_presence():
        update_presence(details="Just started playing", large_image="icon_large")