python early:
    from pypresence import Presence

    client_id = '1322302098385276988'
    RPC = Presence(client_id)
    connected = False
    presence_details = None
    presence_large_image = None
    presence_large_text = None
    presence_small_image = None
    presence_icon = None
    presence_start_time = int(time.time())

    def connect_to_discord():
        global connected
        try:
            RPC.connect()
            connected = True
            print("Discord RPC Connected") #Debug message
        except Exception as e:
            print(f"Failed to connect to Discord: {e}") #Debug message
            connected = False
    
    def update_presence(details = None, large_image = "icon_large", large_text = "Like our little secret sneak peek?", small_image = None, small_text = None):
        global connected, presence_details, presence_large_image, presence_large_text, presence_small_image, presence_small_text
        if not connected:
            connect_to_discord()  # Try to connect if not already

        if connected:
            if presence_details != details or presence_large_image != large_image or presence_large_text != large_text or presence_small_image != small_image or presence_small_text != small_text:
                presence_details = details
                presence_large_image = large_image
                presence_large_text = large_text
                presence_small_image = small_image
                presence_small_text = small_text

                if details == None:
                    details = "Spending time with " + ("his" if persistent.male else "her" if persistent.male == False else "their") + " " + (persistent.yuri_nickname if persistent.yuri_nickname else "Yuri")
                try:
                    RPC.update(details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text, start=presence_start_time)
                    print("Updating discord presence")
                except Exception as e:
                    print(f"Failed to update presence: {e}")
                    connected = False # We probably lost connection, set to false

    update_presence(details="Launching Just Yuri...")
        