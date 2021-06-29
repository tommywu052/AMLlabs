from __future__ import print_function
import logging
import grpc
import anomalydetection_pb2
import anomalydetection_pb2_grpc

# data
import pandas


def run():
    # data
    temp_data = pandas.read_csv('temperature_data.csv')

    print(temp_data.iloc[0])

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = anomalydetection_pb2_grpc.ModelServiceStub(channel)
        # Request
        req = anomalydetection_pb2.InferenceReq()
        req.machine.temperature = temp_data.iloc[0]['machine_temperature']
        req.machine.pressure = temp_data.iloc[0]['machine_pressure']
        req.ambient.temperature = temp_data.iloc[0]['ambient_temperature']
        req.ambient.humidity = temp_data.iloc[0]['ambient_humidity']
        req.anomaly = True

        InferenceResult = stub.Inference(req)
    print("Grpc: ModelService client received: ")
    print(InferenceResult)
    print('Inference: Anomaly result: ' + str(InferenceResult.anomaly))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run()
