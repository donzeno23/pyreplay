import serializer_demo as sd


def run():
    song = sd.Song('1', 'Water of Love', 'Dire Straits')
    serializer = sd.SongSerializer()

    print(serializer.serialize(song, 'JSON'))
    # '{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

    print(serializer.serialize(song, 'XML'))
    # '<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

    print(serializer.serialize(song, 'YAML'))

if __name__ == '__main__':
    run()