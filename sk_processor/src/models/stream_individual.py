from faust import Record
from models.algorithm import Algorithm

class StreamIndividual(Record,serializer="json"):
    id: str
    import_str: str
    alg_str: str
    db_training_path: str
    db_test_path: str
    parameters_str: list = Non