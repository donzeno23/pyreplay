import serializers
import songs
import yaml_serializer


def run():
    song = songs.Song('1', 'Water of Love', 'Dire Straits')
    serializer = serializers.ObjectSerializer()

    print(serializer.serialize(song, 'JSON'))
    # {"id": "1", "title": "Water of Love", "artist": "Dire Straits"}

    print(serializer.serialize(song, 'XML'))
    # <song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>

    print(serializer.serialize(song, 'YAML'))
    # {artist: Dire Straits, id: '1', title: Water of Love}


if __name__ == '__main__':
    run()