##unit testing class
import unittest
from PartA import Artist, Song, Album, Playlist

class testClass(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Taylor Swift", "13/12/1989", "USA")
        self.song = Song("Style", "Taylor Swift", 2014)
        self.album = Album("1989", "Taylor Swift", 2014)
        self.playlist = Playlist("Taylor Swift Playlist")

#check each object is an instance of a class against all classes
    def test_artist_is_instance_of_artist(self):
        self.assertIsInstance(self.artist, Artist)

    def test_song_is_instance_of_song(self):
        self.assertIsInstance(self.song, Song)

    def test_album_is_instance_of_album(self):
        self.assertIsInstance(self.album, Album)

    def test_playlist_is_instance_of_playlist(self):
        self.assertIsInstance(self.playlist, Playlist)

#check if an object is not an instance of all classes
    def test_artist_is_not_instance_of_song(self):
        self.assertNotIsInstance(self.artist, Song)

    def test_song_is_not_instance_of_album(self):
        self.assertNotIsInstance(self.song, Album)

    def test_album_is_not_instance_of_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def test_playlist_is_not_instance_of_artist(self):
        self.assertNotIsInstance(self.playlist, Artist)

# 2 unit tests to check if 2 objects are identical
    def test_identical_objects(self):
        same_song = self.song
        self.assertIs(self.song, same_song)

    def test_different_objects(self):
        different_song = self.song

#- 1 test for identical objects


#- 1 test for unidentical but similar objects


# unit tests for all methods

#unit tests for sorting methods

