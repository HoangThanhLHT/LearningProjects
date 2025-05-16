import yt_dlp
from yt_dlp import YoutubeDL

def youtube_to_mp3(urls):
        # save video/playlist as .mp3 save to ./download
    opts = {
        'extract_flat': 'discard_in_playlist',
        'final_ext': 'mp3',
        'format': 'ba[acodec^=mp3]/ba/b',
        'fragment_retries': 10,
        'ignoreerrors': 'only_download',
        'noprogress': True,
        'paths': {'home': './download'},
        'postprocessors': [{'actions': [(yt_dlp.postprocessor.metadataparser.MetadataParserPP.interpretter,
                                'title',
                                '%(artist)s - %(title)s')],
                                'key': 'MetadataParser',
                                'when': 'pre_process'},
                            {'key': 'FFmpegExtractAudio',
                                'nopostoverwrites': False,
                                'preferredcodec': 'mp3',
                                'preferredquality': '5'},
                            {'key': 'FFmpegConcat',
                                'only_multi_video': True,
                                'when': 'playlist'}],
        'quiet': False,
        'retries': 10}


    with YoutubeDL(opts) as yt:
        yt.download(urls)

def main():
    urls = input('Enter link video/playlist: ')
    youtube_to_mp3(urls)
    print('Finish! Check ./download')

if __name__ == "__main__":
    main()
