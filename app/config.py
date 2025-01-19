import os

# Configuration for the project
class Config:
    API_KEY="e14baacf7f45152ce9af0df11fa2a277372bfe86c1e6ae6bc7124ee5d31822bb"
    # API_KEY=  "6d0fbdf3b231c8a57baafdcc99b266a1b4d4dae05260086f3868294a939ce88c"
    API_ENDPOINT = "https://api.piapi.ai/api/v1/task"
    TEMP_DIR_AUDIO = "./temp/audio"
    TEMP_DIR_VIDEO = "./temp/videos"

    # Ensure directories exist
    os.makedirs(TEMP_DIR_AUDIO, exist_ok=True)
    os.makedirs(TEMP_DIR_VIDEO, exist_ok=True)
