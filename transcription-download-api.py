from youtube_transcript_api import YouTubeTranscriptApi
import json

# Get transcripts for the specified video IDs
video_ids = ["d5ib3qjQkwk", "EfY_GG4cqHM"]
transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)

# Iterate through the transcripts and save them to JSON files
for i, transcript_data in enumerate(transcripts):
    # Generate a filename using the index and a prefix
    filename = f"transcript_{i}"

    # Check if the 'transcript' key exists in the transcript data
    if 'transcript' in transcript_data:
        transcript_text = transcript_data['transcript']

        with open(f'{filename}.json', 'w', encoding='utf-8') as json_file:
            json.dump(transcript_text, json_file)
    else:
        print(f"No transcript found for video ID: {video_ids[i]}")
