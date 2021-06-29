# build environment
FROM python:3.6.13-stretch as builder

RUN mkdir app
WORKDIR app
COPY hooks .
COPY iot_score_grpc.py .
COPY anomalydetection_pb2.py .
COPY anomalydetection_pb2_grpc.py .

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install pyinstaller
RUN pyinstaller --name worker --additional-hooks-dir=hooks iot_score_grpc.py

# production environment
FROM ubuntu:xenial

EXPOSE 50051

RUN mkdir /models
RUN mkdir /usr/app
COPY --from=builder /app/dist/worker /usr/app
COPY azureml /usr/app/azureml
COPY model.pkl /models

CMD ["/usr/app/worker"]
