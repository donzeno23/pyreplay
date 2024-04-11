'''
Supporting Additional Formats

You want your designs to be flexible, 
and as you will see, supporting additional formats 
without changing SerializerFactory is relatively easy.

The idea is to provide a method in SerializerFactory 
that registers a new Serializer implementation for the 
format we want to support:
'''

import json
import xml.etree.ElementTree as et

'''
By implementing Factory Method using an Object Factory
and providing a registration interface, you are able to 
support new formats without changing any of the existing 
application code. 

This minimizes the risk of breaking existing features or 
introducing subtle bugs.
'''
class SerializerFactory:

    def __init__(self):
        # The registration information is stored in the _creators dictionary
        self._creators = {}

    def register_format(self, format, creator):
        '''
        method allows registering new formats by specifying a 
        format value used to identify the format and a creator object
        '''
        # creator object is the class name of the concrete Serializer
        # NOTE: because all the Serializer classes provide a default .__init__() to initialize the instances
        self._creators[format] = creator

    def get_serializer(self, format):
        '''
        method retrieves the registered creator and creates 
        the desired object. If the requested format has not been 
        registered, then ValueError is raised
        '''
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

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

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
