# import os
# import requests
# import librosa

# from config import Config

# def generate_video_with_kling_api(prompt, aspect_ratio="1:1", duration=5):
#     """
#     Call the Kling API to generate a video based on the prompt.

#     Args:
#         prompt (str): Final prompt for the video generation.
#         aspect_ratio (str): Aspect ratio for the video (default: 1:1).
#         duration (int): Duration of the video in seconds.

#     Returns:
#         str: Path to the generated video file.
#     """
#     payload = {
#         "model": "kling",
#         "task_type": "video_generation",
#         "input": {
#             "prompt": prompt,
#             "negative_prompt": "",
#             "cfg_scale": 0.5,
#             "duration": duration,
#             "aspect_ratio": aspect_ratio,
#             "camera_control": {
#                 "type": "simple",
#                 "config": {
#                     "horizontal": 0,
#                     "vertical": 0,
#                     "pan": 0,
#                     "tilt": 0,
#                     "roll": 0,
#                     "zoom": 0
#                 }
#             },
#             "mode": "std"
#         },
#         "config": {
#             "service_mode": ""
#         }
#     }
#     headers = {
#         'x-api-key': Config.API_KEY,
#         'Content-Type': 'application/json'
#     }
#     try:
#         response = requests.post(Config.API_ENDPOINT, json=payload, headers=headers)
#         if response.status_code == 100000:
#             video_path = os.path.join(Config.TEMP_DIR_VIDEO, "generated_video.mp4")
#             with open(video_path, "wb") as f:
#                 f.write(response.content)
#             return video_path
#         else:
#             raise RuntimeError(f"Failed to generate video: {response.text}")
#     except Exception as e:
#         raise RuntimeError(f"Error during video generation: {str(e)}")



# import os
# import requests
# import librosa
# from config import Config

# def generate_video_with_kling_api(prompt, aspect_ratio="1:1", duration=5, timeout=60):
#     """
#     Call the Kling API to generate a video based on the prompt.

#     Args:
#         prompt (str): Final prompt for the video generation.
#         aspect_ratio (str): Aspect ratio for the video (default: 1:1).
#         duration (int): Duration of the video in seconds.
#         timeout (int): Maximum time in seconds to wait for a response from the API.

#     Returns:
#         str: Path to the generated video file.
#     """
#     payload = {
#         "model": "kling",
#         "task_type": "video_generation",
#         "input": {
#             "prompt": prompt,
#             "negative_prompt": "",
#             "cfg_scale": 0.5,
#             "duration": duration,
#             "aspect_ratio": aspect_ratio,
#             "camera_control": {
#                 "type": "simple",
#                 "config": {
#                     "horizontal": 0,
#                     "vertical": 0,
#                     "pan": 0,
#                     "tilt": 0,
#                     "roll": 0,
#                     "zoom": 0
#                 }
#             },
#             "mode": "std"
#         },
#         "config": {
#             "service_mode": ""
#         }
#     }
#     headers = {
#         'x-api-key': Config.API_KEY,
#         'Content-Type': 'application/json'
#     }
#     try:
#         response = requests.post(Config.API_ENDPOINT, json=payload, headers=headers, timeout=timeout)
#         if response.status_code == 200:
#             video_path = os.path.join(Config.TEMP_DIR_VIDEO, "generated_video.mp4")
#             with open(video_path, "wb") as f:
#                 f.write(response.content)
#             return video_path
#         else:
#             raise RuntimeError(f"Failed to generate video: {response.text}")
#     except requests.exceptions.Timeout:
#         raise RuntimeError(f"The request to the API timed out after {timeout} seconds.")
#     except Exception as e:
#         raise RuntimeError(f"Error during video generation: {str(e)}")











# import os
# import requests
# from config import Config

# def generate_video_with_kling_api(prompt, negative_prompt="", aspect_ratio="16:9", duration=5, timeout=300):
#     """
#     Call the new Segmind API to generate a video based on the prompt.

#     Args:
#         prompt (str): Final prompt for the video generation.
#         negative_prompt (str): Negative prompt to exclude specific elements (default: "").
#         aspect_ratio (str): Aspect ratio for the video (default: "16:9").
#         duration (int): Duration of the video in seconds (default: 5).
#         timeout (int): Maximum time in seconds to wait for a response from the API.

#     Returns:
#         str: Path to the generated video file or an error message.
#     """
#     api_key = Config.API_KEY  # Your API key stored in a configuration file
#     api_endpoint = "https://api.segmind.com/v1/kling-1.6-text2video"

#     payload = {
#         "prompt": prompt,
#         "negative_prompt": negative_prompt,
#         "cfg_scale": 0.5,
#         "mode": "std",
#         "aspect_ratio": aspect_ratio,
#         "duration": duration
#     }

#     headers = {
#         'x-api-key': api_key,
#         'Content-Type': 'application/json'
#     }

#     try:
#         response = requests.post(api_endpoint, json=payload, headers=headers, timeout=timeout)

#         if response.status_code == 200:
#             video_path = os.path.join(Config.TEMP_DIR_VIDEO, "generated_video.mp4")
#             with open(video_path, "wb") as f:
#                 f.write(response.content)
#             return f"Video successfully saved at: {video_path}"
#         else:
#             return f"API returned an error: {response.status_code} - {response.text}"
#     except requests.exceptions.Timeout:
#         return f"The request to the API timed out after {timeout} seconds."
#     except Exception as e:
#         return f"Error during video generation: {str(e)}"


# # Example usage
# if __name__ == "__main__":
#     # Example prompt and parameters
#     prompt = "a Shih Tzu puppy playing in a sunny garden"
#     negative_prompt = "No artificial objects, no people"
#     aspect_ratio = "16:9"
#     duration = 5  # 5 seconds video

#     result = generate_video_with_kling_api(
#         prompt=prompt,
#         negative_prompt=negative_prompt,
#         aspect_ratio=aspect_ratio,
#         duration=duration
#     )
#     print(result)






# import os
# import requests
# import time
# from config import Config

# def generate_video_with_kling_api(prompt, negative_prompt="", aspect_ratio="16:9", duration=5, timeout=600):
#     """
#     Call the Segmind API to generate a video and handle the response.

#     Args:
#         prompt (str): Final prompt for the video generation.
#         negative_prompt (str): Negative prompt to exclude specific elements (default: "").
#         aspect_ratio (str): Aspect ratio for the video (default: "16:9").
#         duration (int): Duration of the video in seconds (default: 5).
#         timeout (int): Maximum time in seconds to wait for a response from the API.

#     Returns:
#         str: Path to the generated video file or an error message.
#     """
#     api_key = Config.API_KEY
#     api_endpoint = "https://api.segmind.com/v1/kling-1.6-text2video"
#     check_status_interval = 10  # Time interval to check task status in seconds

#     payload = {
#         "prompt": prompt,
#         "negative_prompt": negative_prompt,
#         "cfg_scale": 0.5,
#         "mode": "std",
#         "aspect_ratio": aspect_ratio,
#         "duration": duration
#     }

#     headers = {
#         'x-api-key': api_key,
#         'Content-Type': 'application/json'
#     }

#     try:
#         # Step 1: Submit the request
#         response = requests.post(api_endpoint, json=payload, headers=headers, timeout=30)
#         if response.status_code != 200:
#             raise RuntimeError(f"API Error: {response.status_code} - {response.text}")

#         response_data = response.json()
#         task_id = response_data.get("data", {}).get("task_id")
#         if not task_id:
#             raise RuntimeError("Failed to retrieve task ID from API response.")

#         print(f"Task submitted successfully. Task ID: {task_id}")

#         # Step 2: Poll the task status
#         status_endpoint = f"{api_endpoint}/{task_id}"
#         start_time = time.time()
#         while True:
#             if time.time() - start_time > timeout:
#                 raise RuntimeError(f"The request to the API timed out after {timeout} seconds.")

#             status_response = requests.get(status_endpoint, headers=headers)
#             if status_response.status_code != 200:
#                 raise RuntimeError(f"Failed to check task status: {status_response.text}")

#             status_data = status_response.json()
#             task_status = status_data.get("data", {}).get("status", "")
#             video_url = status_data.get("data", {}).get("output", {}).get("video_url", "")

#             if task_status == "completed" and video_url:
#                 print("Task completed. Downloading video...")
#                 break
#             elif task_status == "failed":
#                 raise RuntimeError("Video generation failed. Please try again.")
#             else:
#                 print(f"Task status: {task_status}. Checking again in {check_status_interval} seconds...")
#                 time.sleep(check_status_interval)

#         # Step 3: Download the video
#         temp_video_path = os.path.join(Config.TEMP_DIR_VIDEO, "generated_video.mp4")
#         video_response = requests.get(video_url, stream=True)
#         with open(temp_video_path, "wb") as f:
#             for chunk in video_response.iter_content(chunk_size=8192):
#                 f.write(chunk)

#         print(f"Video successfully saved at: {temp_video_path}")
#         return temp_video_path

#     except requests.exceptions.Timeout:
#         raise RuntimeError(f"The request to the API timed out after {timeout} seconds.")
#     except Exception as e:
#         raise RuntimeError(f"Error during video generation: {str(e)}")












import os
import requests
import time
from config import Config  # Ensure Config contains API_KEY and TEMP_DIR_VIDEO

def generate_video_with_kling_api(prompt, negative_prompt="", aspect_ratio="1:1", duration=5, timeout=1800):
    """
    Call the video generation API and handle the response, including polling for status.

    Args:
        prompt (str): Final prompt for the video generation.
        negative_prompt (str): Negative prompt to exclude specific elements (default: "").
        aspect_ratio (str): Aspect ratio for the video (default: "1:1").
        duration (int): Duration of the video in seconds (default: 5).
        timeout (int): Maximum time in seconds to wait for a response from the API (default: 1800).

    Returns:
        str: Path to the generated video file or an error message.
    """
    api_endpoint = Config.API_ENDPOINT
    headers = {
        'x-api-key': Config.API_KEY,
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "kling",
        "task_type": "video_generation",
        "input": {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "cfg_scale": 0.5,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
            "camera_control": {
                "type": "simple",
                "config": {
                    "horizontal": 0,
                    "vertical": 0,
                    "pan": 0,
                    "tilt": 0,
                    "roll": 0,
                    "zoom": 0
                }
            },
            "mode": "std"
        },
        "config": {
            "service_mode": "",
            "webhook_config": {
                "endpoint": "",
                "secret": ""
            }
        }
    }

    try:
        # Step 1: Submit the request
        response = requests.post(api_endpoint, json=payload, headers=headers, timeout=30)
        if response.status_code != 200:
            raise RuntimeError(f"API Error: {response.status_code} - {response.text}")

        response_data = response.json()
        task_id = response_data.get("data", {}).get("task_id")
        if not task_id:
            raise RuntimeError("Failed to retrieve task ID from API response.")

        print(f"Task submitted successfully. Task ID: {task_id}")

        # Step 2: Poll for task status
        status_endpoint = f"{api_endpoint}/{task_id}"
        start_time = time.time()
        polling_interval = 15  # Initial polling interval in seconds

        while True:
            if time.time() - start_time > timeout:
                raise RuntimeError(f"The request to the API timed out after {timeout} seconds.")

            status_response = requests.get(status_endpoint, headers=headers, timeout=30)
            if status_response.status_code != 200:
                raise RuntimeError(f"Failed to check task status: {status_response.text}")

            status_data = status_response.json()
            task_status = status_data.get("data", {}).get("status", "")
            video_url = status_data.get("data", {}).get("output", {}).get("video_url", "")

            if task_status == "completed" and video_url:
                print("Task completed. Downloading video...")
                break
            elif task_status == "failed":
                raise RuntimeError("Video generation failed. Please try again.")
            else:
                print(f"Task status: {task_status}. Checking again in {polling_interval} seconds...")
                time.sleep(polling_interval)

        # Step 3: Download the video
        temp_video_path = os.path.join(Config.TEMP_DIR_VIDEO, "generated_video.mp4")
        video_response = requests.get(video_url, stream=True)
        with open(temp_video_path, "wb") as f:
            for chunk in video_response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Video successfully saved at: {temp_video_path}")
        return temp_video_path

    except requests.exceptions.Timeout:
        raise RuntimeError(f"The request to the API timed out after {timeout} seconds.")
    except Exception as e:
        raise RuntimeError(f"Error during video generation: {str(e)}")