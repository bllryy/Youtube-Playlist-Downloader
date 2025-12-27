import yt_dlp
import os


# TODO make a thingy so that if the video is not avaible in my country then bypass

# make the output dir

output_dir = "YouTube_Downloads"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

urls = [
    "https://soundcloud.com/hedrabionics/sets/63-1a",
    ]

ydl_opts = {
        'format': 'bestaudio/best',  # Download best audio quality
        'extractaudio': True,        # Extract audio only
        'audioformat': 'mp3',        # Convert to MP3
        'audioquality': '320',       # Audio quality (128, 192, 256, 320)
        'outtmpl': os.path.join(output_dir, '%(playlist_title)s/%(title)s.%(ext)s'),  # output template
        'ignoreerrors': True,        # Continue on errors
        'no_warnings': False,        # Show warnings
        'extractflat': False,        # Download individual videos, not just metadata
        'writethumbnail': True,     # Set to True for thumbnails
        'writeinfojson': False,      # Set to True for metadata JSON files
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', # HAS TO BE SYNCED AS ABOVE
        }],
    }

# Download each playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for i, url in enumerate(urls, 1):
        if url.strip():  # Skip empty URLs
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

    print(f" Done! Files saved in: {output_dir}")


if __name__ == "__main__":
    # Optional: Filter out empty URLs
    valid_urls = [url for url in urls if url.strip()]

    if not valid_urls:
        print("No valid URLs found. Please add your YouTube playlist URLs to the 'urls' list.")
    else:
        print(f"Found {len(valid_urls)} playlist(s) to download")

        download_playlists_as_mp3(valid_urls, output_dir="YouTube_Downloads")
