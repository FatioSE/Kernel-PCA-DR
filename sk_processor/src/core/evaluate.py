from multiprocessing import Process, Queue
from queue import Empty
from models.evaluation_result import EvaluationResult
from models.stream_individual import StreamIndividual

from core.evaluate_individual import evaluate_individual

def evaluate(stream_individual: StreamIndividual) -> EvaluationResult:
  