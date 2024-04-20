import requests
from bs4 import BeautifulSoup

# Set your YouTube API key here:
api_key = 'YOUR_API_KEY'

# Set the YouTube channel ID here:
channel_id = 'CHANNEL_ID'

# Set the search query here:
search_query = 'series'

url = f'https://www.youtube.com/channel/{channel_id}/videos'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    video_list = []

    for video in soup.find_all('ytd-video-renderer'):
        title = video.select_one('.title').text.strip()
        description = video.select_one('.description').text.strip()

        if search_query.lower() in title.lower():
            video_dict = {
                'Title': title,
                'Description': description
            }
            video_list.append(video_dict)

        elif search_query.lower() in description.lower():
            video_dict = {
                'Title': title,
                'Description': description
            }
            video_list.append(video_dict)

    for tag in soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-video-renderer'}):
        tags = [tag.text.strip() for tag in tag.parent.select('.tag')]

        if search_query.lower() in [tag.lower() for tag in tags]:
            title = tag.parent.select_one('.title').text.strip()
            description = tag.parent.select_one('.description').text.strip()

            video_dict = {
                'Title': title,
                'Description': description
            }
            video_list.append(video_dict)

    print(video_list)
else:
    print(f'Failed to retrieve the channel videos: {response.status_code}')
