"""An example of using an HTTP client to make a get request which returns
HTML.
"""

import colander
from apifactory import httplib, factory, spec, schemas


class QuerySchema(colander.MappingSchema):
    q = colander.SchemaNode(colander.String())


query_schema = httplib.HttpMetaSchema(query=QuerySchema())

api_search = httplib.GET('search', query_schema, schemas.RawSchema)


transport = httplib.HTTPTransport('google.com', 80)
client_mapping = {
    'search': spec.ClientSpec(api_search, httplib.DEFAULT_GET)
}

http_client = factory.build_client(client_mapping, transport)
import pdb;pdb.set_trace()

body = http_client.search(q='stars').content
print(f"Found {body.count('stars')} stars")