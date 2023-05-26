import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.song_1 = Song("Teenage Dirtbag")
        self.song_2 = Song("All Star")
        self.song_3 = Song("Say My Name")
        self.guest_1 = Guest("John", 40.00, self.song_1)
        self.guest_2 = Guest("Bob", 30.00, self.song_3)
        self.guest_3 = Guest("Paul", 3.00, self.song_1)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    def test_song_has_name(self):
        self.assertEqual("Teenage Dirtbag", self.song_1.song_name)

    def test_add_songs_to_playlist(self):
        self.room.add_song_to_playlist(self.song_1)
        self.room.add_song_to_playlist(self.song_2)
        self.assertEqual(2, len(self.room.playlist))

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.assertEqual(2, len(self.room.guests))

    def test_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_2)
        self.room.remove_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_room_at_capacity(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(3, len(self.room.guests))

    def test_charge_entry_fee_integration(self):
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(35.00, self.guest_1.wallet)

    def test_guest_cant_afford(self):
        self.room.add_guest_to_room(self.guest_3)
        self.assertEqual(0, len(self.room.guests))

    def test_guest_has_fav_song(self):
        self.assertEqual("Teenage Dirtbag", self.guest_1.fav_song.song_name)

    def test_fav_song_reaction(self):
        self.room.add_song_to_playlist(self.song_1)
        self.room.add_song_to_playlist(self.song_2)
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual("YEAHHHHH!", self.room.fav_song_reaction(self.guest_1))

    def test_no_fav_song_reaction(self):
        self.room.add_song_to_playlist(self.song_1)
        self.room.add_song_to_playlist(self.song_2)
        self.room.add_guest_to_room(self.guest_2)
        self.assertEqual(None, self.room.fav_song_reaction(self.guest_2))

    def test_room_till(self):
        self.room.add_guest_to_room(self.guest_1)
        self.room.add_guest_to_room(self.guest_1)
        self.assertEqual(10.00, self.room.till)