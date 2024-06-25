from googleapiclient.discovery import build
import webbrowser


def search_and_play(api_key, query):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=1
    )
    response = request.execute()

    if 'items' in response and response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        print(f"Playing: {response['items'][0]['snippet']['title']}")
        webbrowser.open(video_url)
    else:
        print("No videos found.")



