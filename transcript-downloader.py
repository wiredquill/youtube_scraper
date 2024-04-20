import os
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'

def download_transcripts(video_ids, output_dir):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    for video_id in video_ids:
        try:
            transcript_response = youtube.captions().list(
                part='snippet',
                videoId=video_id
            ).execute()

            if 'items' in transcript_response:
                # Save transcript to a file
                transcript = transcript_response['items'][0]['snippet']['transcript']
                filename = f'{video_id}_transcript.txt'
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'w') as f:
                    f.write(transcript)
                print(f'Transcript downloaded for video ID {video_id}')
            else:
                print(f'No transcript found for video ID {video_id}')

        except HttpError as e:
            print(f'Error downloading transcript for video ID {video_id}: {e}')

# Load video information from the JSON file
def load_video_info(file_path):
    with open(file_path, 'r') as f:
        video_info = json.load(f)
    return video_info

# Example usage
if __name__ == '__main__':
    video_info_file = 'video_info.json'
    output_directory = 'transcripts'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    video_info = load_video_info(video_info_file)
    video_ids = [video['video_id'] for video in video_info]

    download_transcripts(video_ids, output_directory)
