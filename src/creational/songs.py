class Song:
    '''
    The Song class implements the Serializable interface 
    by providing a .serialize(serializer) method
    '''
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        '''
        the Song class uses the serializer object to write 
        its own information without any knowledge of the format
        '''
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)