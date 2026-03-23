#imported random to shuffle the playlist.
import random

class Artist:
    def __init__(self, name, dob, country, albums=None, songs=None):
        # I save the basic artist information when I create the object.
        self.name = name
        self.dob = dob
        self.country = country

        if albums is not None:
            self.albums = albums
        else:
            # If no albums are given, I create an empty list for them.
            self.albums = []

        if songs is not None:
            self.songs = songs
        else:
            # If no songs are given, I create an empty list for them.
            self.songs = []

    def display_info(self):
        # I print the artist details and show album and song names from the lists.
        print("Artist Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Country:", self.country)
        print("Albums:", [album.album_title for album in self.albums])
        print("Songs:", [song.song_title for song in self.songs])

    def add_album(self, album):
        # album object into the artist's album list.
        self.albums.append(album)

    def add_song(self, song):
        # song object into the artist's song list.
        self.songs.append(song)


class Song:
    def __init__(self, song_title, artist_name, year_of_release):

        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release

    def display_info(self):
        # I print the values stored in this song object.
        print("Song Title:", self.song_title)
        print("Artist Name:", self.artist_name)
        print("Year of Release:", self.year_of_release)


class Album:
    def __init__(self, album_title, artist_name, year_of_release, songs=None):
        # I save the album details when I create the object.
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        if songs is not None:
            self.songs = songs
        else:
            # If no songs are passed in, I start with an empty song list.
            self.songs = []

    def display_info(self):
        # I print the album details and only show the titles of songs in the album.
        print("Album Title:", self.album_title)
        print("Artist Name:", self.artist_name)
        print("Year of Release:", self.year_of_release)
        print("Songs:", [song.song_title for song in self.songs])

    def add_song(self, title, release_year):
        # I create a new Song using this album's artist name, then store it in the album.
        new_song = Song(title, self.artist_name, release_year)
        self.songs.append(new_song)


class Playlist:
    def __init__(self, playlist_title, songs=None):
        # I save the playlist title when I create the object.
        self.playlist_title = playlist_title
        if songs is not None:
            self.songs = songs
        else:
            # If no songs are given, I start with an empty playlist.
            self.songs = []

    def add_song(self, song):
        # I add a song object into the playlist list.
        self.songs.append(song)

    def print_all_song(self):
        # I loop through the playlist and print each song title.
        for song in self.songs:
            print(song.song_title)

    def sort_playlist(self, order='ASC'):
        # I sort the playlist by song title and reverse it only for descending order.
        if order == 'DES':
            self.songs.sort(key=lambda song: song.song_title, reverse=True)
        else:
            self.songs.sort(key=lambda song: song.song_title)

    def shuffle_playlist(self):
        # I change the order of the songs randomly.
        random.shuffle(self.songs)

#sample objects to demonstrate that all classes and methods work.
artist1 = Artist("Taylor Swift", "13/12/1989", "USA")

album1 = Album("1989", "Taylor Swift", 2014)

song1 = Song("Style", "Taylor Swift", 2014)
song2 = Song("Blank Space", "Taylor Swift", 2014)

album1.add_song("Shake It Off", 2014)
album1.add_song("Bad Blood", 2014)

artist1.add_album(album1)
artist1.add_song(song1)
artist1.add_song(song2)

playlist1 = Playlist("Taylor Swift Playlist")

for song in album1.songs:
    playlist1.add_song(song)

playlist1.add_song(song1)
playlist1.add_song(song2)

#testing display methods

artist1.display_info()
album1.display_info()
song1.display_info()
song2.display_info()

#testing the advanced features
print("Playlist songs:")
playlist1.print_all_song()

print("Sorted playlist ASC:")
playlist1.sort_playlist("ASC")
playlist1.print_all_song()

print("Shuffled playlist:")
playlist1.shuffle_playlist()
playlist1.print_all_song()
