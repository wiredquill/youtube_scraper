from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'UC...'

def get_channel_videos(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the playlist ID of the channel's uploaded videos
    channels_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Get the videos from the playlist
    videos = []
    next_page_token = None

    while True:
        playlist_items_response = youtube.playlistItems().list(
            playlistId=playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos.extend(playlist_items_response['items'])
        next_page_token = playlist_items_response.get('nextPageToken')

        if not next_page_token:
            break

    return videos

def print_video_info(videos):
    for video in videos:
        title = video['snippet']['title']
        description = video['snippet']['description']

        print(f'Title: {title}')
        print(f'Description: {description}')
        print('---')

# Example usage
videos = get_channel_videos(API_KEY, CHANNEL_ID)
print_video_info(videos)
