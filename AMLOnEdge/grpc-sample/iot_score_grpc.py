import pandas
# from sklearn.externals import joblib
import joblib
from sklearn.linear_model import Ridge
from azureml.core.model import Model
import sklearn.tree.tree

# Service
from concurrent import futures
import logging
import grpc
import anomalydetection_pb2
import anomalydetection_pb2_grpc


def init():
    global model
    # this is a different behavior than before when the code is run locally, even though the code is the same.
    # model_path = Model.get_model_path('model.pkl')
    # deserialize the model file back into a sklearn model
    model = joblib.load('/models/model.pkl')


class ModelService(anomalydetection_pb2_grpc.ModelServiceServicer):

    def Inference(self, request, context):
        pred = []
        pred.append(1)
        ModelResult = True
        try:
            input_df = pandas.DataFrame([[request.machine.temperature, request.machine.pressure,
                                          request.ambient.temperature, request.ambient.humidity]])
            pred = model.predict(input_df)
            #print("Prediction is ", pred[0])
        except Exception as e:
            result = str(e)
            #print(result)

        if pred[0] == 1:
            ModelResult = True
        else:
            ModelResult = False

        res = anomalydetection_pb2.InferenceRes()
        res.machine.CopyFrom(request.machine)
        res.ambient.CopyFrom(request.ambient)
        res.anomaly = ModelResult

        return res


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    anomalydetection_pb2_grpc.add_ModelServiceServicer_to_server(ModelService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    init()

    # Service
    logging.basicConfig()
    serve()
