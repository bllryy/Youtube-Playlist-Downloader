# Youtube-Playlist-Downloader
Utilizing python yt-dlp to make it easier to download youtube playlists. Essential for archiving youtube channels and downloading songs to load onto your phone.
# Before Running 
```pip-install yt-dlp --break-system-packages```

# SoundCloud Download
- Install the librarys
- https://github.com/soundcloud/soundcloud-python: pip install soundcloud. Refer to their documentation for alternate installation methods
- Then get client id
- https://developers.soundcloud.com/

## Downloading a track
```
$ python download.py -h
usage: download.py [-h] [--track TRACK] [--playlist PLAYLIST] --id ID
                   [--override]

Download a SoundCloud sound or a complete playlist

optional arguments:
  -h, --help            show this help message and exit
  --track TRACK, -s TRACK  Download a single track
  --playlist PLAYLIST, -p PLAYLIST
                        Download all tracks from a public playlist
  --id ID, -i ID        Client ID
  --override, -d        Override file if it exists. Defaults to false
```

- or ```$ python download.py --id my_id --track https://soundcloud.com/dj-crontab/indiscriminate-killers```

- the track will be a mp3 folder under the current dir

## Download playlist 
- To download all tracks from a playlist, make sure the playlist URL is accessible without password
- For ex:
```
$ python download.py --id my_id --playlist https://soundcloud.com/its-me/sets/my-list/sharecode
Found: 'Execute Every Minute'
File already exists, skipped
Found: 'Indiscriminate Killers'
Found: 'Above & Beyond pres. OceanLab - Satellite (ilan Bluestone Remix) [Out Now]'
Error: could not download
Found: 'Missiles at a Wedding - Heavy'
Found: 'CASHMERE'
Downloaded: 3, Skipped: 1, Errors: 1
```

- *for some reason titles cant be downloaded*

- The track will be downloaded to a folder named ```mp3/playlist_title``` under the current directory

## Download all playlists
- To download everything from a user
- ```$ python download.py --id my_id --all http://soundcloud.com/some-user```

### And there is a test file just in case :)

```
$ py.test -q tests
.
1 passed in 0.08 seconds
```

