from faust import Record
from models.algorithm import Algorithm

class StreamIndividual(Record,serializer="json"):
    id: str
    import_str: str
    al