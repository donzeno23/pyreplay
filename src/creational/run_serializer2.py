import songs
import serializers


def run():
    song = songs.Song('1', 'Water of Love', 'Dire Straits')
    serializer = serializers.ObjectSerializer()

    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    print(serializer.serialize(song, 'YAML'))


if __name__ == '__main__':
    run()