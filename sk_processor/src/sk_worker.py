import faust
from models.stream_individual import StreamIndividual

from core.evaluate import evaluate

app = faust.App('sk-processor-app', broker='kafka://kafka-server:9092',store="memory://")
topic = app.topic('sk-individual-topi