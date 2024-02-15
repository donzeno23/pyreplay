# The Serializer interface is an abstract concept 
# due to the dynamic nature of the Python language

import json
import xml.etree.ElementTree as et

# NOTE: The new design of Factory Method allows the application 
# to introduce new features by adding new classes, 
# as opposed to changing existing ones. 
# You can serialize other objects by implementing the 
# Serializable interface on them. 
# You can support new formats by implementing the 
# Serializer interface in another class.

# TODO: The missing piece is that SerializerFactory has 
# to change to include the support for new formats. 
# This problem is easily solved with the new design because 
# SerializerFactory is a class.

# TODO: The current implementation of SerializerFactory 
# needs to be changed when a new format is introduced. 
# Your application might never need to support any additional 
# formats, but you never know.

class SerializerFactory:
    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


factory = SerializerFactory()

# Use generic serializer
# NOTE: there is no need for a SongSerializer class anymore
class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()

# Concrete class
class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


# Concrete class
class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')