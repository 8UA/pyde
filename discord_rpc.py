from pypresence import Presence
import time

app_id = '999212032366739516'
RPC = Presence(app_id, pipe=0)
RPC.connect()

time_start = time.time()

while 1:
        RPC.update( large_image=f"icon",
                    large_text=f"pyde",
                    details=f"pyde - Text Editor/Python IDE.", 
                    #state=f"obamam",
                    buttons=[{"label": "GitHub", "url": "https://github.com/8UA/pyde"}],
                    start=time_start )
        time.sleep(20)
