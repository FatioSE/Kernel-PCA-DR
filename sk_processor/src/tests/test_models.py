import pytest
from models.algorithm import Algorithm
from models.stream_individual import StreamIndividual
from models.evaluation_result import EvaluationResult

def test_algorithm_model():
    algorithm = Algorithm(
        "from sklearn.tree import DecisionTreeClassifier", "DecisionTreeClassifier", [])
    assert algorithm.import_str == "from sklearn.tree import DecisionTreeClassifier", "test failed"
    assert algorithm.alg_str == "DecisionTreeClassifier",