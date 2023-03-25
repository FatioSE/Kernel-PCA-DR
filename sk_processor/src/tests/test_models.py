import pytest
from models.algorithm import Algorithm
from models.stream_individual import StreamIndividual
from models.evaluation_result import EvaluationResult

def test_algorithm_model():
    algorithm = Algorithm(
        "from sklearn.tree import DecisionTreeClassifier", "DecisionTreeClassifier", [])
    assert algorithm.import_str == "from sklearn.tree import DecisionTreeClassifier", "test failed"
    assert algorithm.alg_str == "DecisionTreeClassifier",  "test failed"
    assert len(algorithm.parameters_str) == 0, "teste failed"


def test_algorithm_from_stream_algorithm():
    stream_algorithm = StreamIndividual(id="1",
                                        import_str="from sklearn.tree import DecisionTreeClassifier",
                                        alg_str="DecisionT