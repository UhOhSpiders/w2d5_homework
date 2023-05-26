class Room():
    def __init__(self, room_number):
        self.room_number = room_number
        self.guests = []
        self.playlist = []
        self.capacity = 3
        self.entry_fee = 5.00
        self.till = 0.00

    def add_song_to_playlist(self, requested_song):
        self.playlist.append(requested_song)

    def fav_song_reaction(self, guest):
        for song in self.playlist:
            if guest.fav_song == song:
                return "YEAHHHHH!"

    def add_guest_to_room(self, guest):
        if len(self.guests) < self.capacity and guest.wallet >= self.entry_fee:
            guest.wallet -= self.entry_fee
            self.till += self.entry_fee
            self.guests.append(guest)  
        else:
            return("No entry")

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    