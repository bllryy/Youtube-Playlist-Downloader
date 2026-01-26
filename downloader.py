import yt_dlp
import os

output_dir = "YouTube_Downloads"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

urls = [
    "https://www.youtube.com/playlist?list=PLkpecPbvtxXw_rpbQMX8J62Fs6dAMiQHt",
]

ydl_opts = {
    'format': 'ba',
    'outtmpl': os.path.join(output_dir, '%(playlist_title)s/%(title)s.%(ext)s'),
    'ignoreerrors': True,
    'no_warnings': False,
    'extractflat': False,
    'writethumbnail': False,
    'writeinfojson': False,
    'cookiefile': 'cookies.txt',
    'extractor_args': {
        'youtube': {
            'player_client': ['android_creator'],
        }
    },
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for i, url in enumerate(urls, 1):
        if url.strip():
            try:
                print(f"\n{'='*50}")
                print(f"Downloading playlist {i}/{len(urls)}")
                print(f"URL: {url}")
                print(f"{'='*50}")
                ydl.download([url])
                print(f"✓ Playlist {i} completed successfully")
            except Exception as e:
                print(f"✗ Error downloading playlist {i}: {str(e)}")
                continue

print(f"Done! Files saved in: {output_dir}")
