import datetime, random, webbrowser

# Set time alarm will go off
def set_alarm(hour, minute, am_pm):
    d = datetime.timedelta(hours = hour - datetime.datetime.now().hour,
            minutes = minute - datetime.datetime.now().minute,
            seconds = 0 - datetime.datetime.now().second)
    return d.seconds

# Gets youtube url from youtube_urls.txt and plays video in browser
def play_vid():
    f = open('youtube_urls.txt', 'r')
    contents = f.read()
    f.close()

    youtube_urls = []
    contents = contents.split('\n')

    for line in contents:
        if line != '':
            youtube_urls.append(line)

    url = youtube_urls[random.randint(0, len(youtube_urls) - 1)]

    webbrowser.open(url, new = 2)
