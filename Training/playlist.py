import random

playlist = []
polarity = -1


def addSong():
    global playlist

    title = input("The Song Name:")
    artist = input("The Artist Name:")
    duration = input("The Duration(mins):")
    song = (title, artist, duration)
    playlist.append(song)


def display():
    for song in playlist:
        print(f"{song[0]} - by {song[1]}. Lenght:- {song[2]}")


def shuffle():
    global shuffle
    random.shuffle(playlist)


def sort():
    global polarity
    x = input(
        """Select the order:
            1) Title
            2) Artist
            3) Duration
           :"""
    )
    x = int(x) - 1
    for i in range(len(playlist)):
        for j in range(i, len(playlist)):
            if polarity != x:
                if playlist[i][x] > playlist[j][x]:
                    playlist[i], playlist[j] = playlist[j], playlist[i]
            else:
                if playlist[i][x] < playlist[j][x]:
                    playlist[i], playlist[j] = playlist[j], playlist[i]
    polarity = x if polarity != x else -1


def run():
    runner = True
    while runner:
        print(
            """What would you like to do?
            1) Add a song
            2) Display Playlist
            3) Suffle
            4) Reorder
            5) Exit"""
        )
        x = int(input("Your Choice:"))
        match x:
            case 1:
                addSong()
            case 2:
                display()
            case 3:
                shuffle()
            case 4:
                sort()
            case 5:
                runner = False


run()
