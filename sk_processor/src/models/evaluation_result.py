class EvaluationResult:

    def __init__(self, individual_id: str, accuracy_test: float = -1.0, f1_test: float = -1.0):
        self.individual_id = individual_id
