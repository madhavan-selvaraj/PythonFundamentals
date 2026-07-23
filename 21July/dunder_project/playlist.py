class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return str(self.__dict__)


class PlayList:
    def __init__(self):
        self.song = []

    def __add__(self, song):
        self.song.append(song)
        return self

    def __sub__(self, song):
        if song in self.song:
            self.song.remove(song)
        return self

    def __contains__(self, item):
        return item in self.song

    def __len__(self):
        return len(self.song)

    def __iter__(self):
        yield from self.song

    def __str__(self):
        result = ""
        for song in self.song:
            result += (
                f"{song.song_id} | {song.title} | {song.artist} | {song.duration} min\n"
            )
        return result


user1 = PlayList()
song1 = Song(1, "4 peru", "Sai abhayankar", 3.22)
song2 = Song(2, "Ordinary person", "Anirudh", 4.22)
song3 = Song(3, "Minnale", "GV", 3.45)
song4 = Song(4, "Maya Nadhi", "SaNa", 4.50)

user1 = user1 + song1
user1 = user1 + song2
user1 = user1 + song3
user1 = user1 + song4


print(user1)
