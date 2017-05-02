from elasticsearch_dsl import DocType, Integer, GeoPoint, Field

class String(Field):
    _param_defs = {
        'fields': {'type': 'field', 'hash': True},
        'analyzer': {'type': 'analyzer'},
    }
    name = 'string'

class RestaurantIndex(DocType):
    pk = Integer()
    name = String(fields={'raw': String(index="not_analyzed")})
    address = String(fields={'raw': String(index="not_analyzed")})
    location = GeoPoint()
    class Meta:
        index = 'commandus'
