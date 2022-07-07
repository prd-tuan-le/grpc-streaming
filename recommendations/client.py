import grpc
import uvicorn
import requests
from fastapi import FastAPI, status, HTTPException
from google.protobuf.json_format import MessageToJson, MessageToDict

from recommendations_pb2_grpc import RecommendationsStub
from recommendations_pb2 import RecommendationRequest


maxMsgLength = 1024 * 1024 * 1000


class RecommendationClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and the
        # the port to which the client should connect
        # to.
        self.host = "localhost"
        self.server_port = 50051

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
            f"{self.host}:{self.server_port}",
            options=[
                ("grpc.max_message_length", maxMsgLength),
                ("grpc.max_send_message_length", maxMsgLength),
                ("grpc.max_receive_message_length", maxMsgLength),
            ],
        )

        # bind the client to the server channel
        self.stub = RecommendationsStub(self.channel)

    def get_recommendations(self, max_results=10):
        recommendations_request = RecommendationRequest(user_id=1, max_results=max_results)
        recommendations_response = self.stub.get_recommend_books(recommendations_request)
        recommendations = recommendations_response
        return recommendations

    def get_streaming_recommendations(self, max_results=1_000_000):
        """
        Client function to call the rpc for GetDStream
        """
        request = RecommendationRequest(user_id=1, max_results=max_results)
        recommendations = self.stub.get_recommend_stream(request)

        with open("recommend_books_from_server.txt", "w", encoding="utf-8") as fd:
            for recommend_book in recommendations:
                fd.write(f"{recommend_book.id}, {recommend_book.title}\n")
                print(recommend_book)


app = FastAPI()
curr_client = RecommendationClient()


@app.get("/")
def hello():
    return {"message": "Hello, World"}


@app.get("/grpc/stream/{num_of_books}")
def grpc_stream(num_of_books: int = 1, name="World"):
    curr_client.get_streaming_recommendations(num_of_books)
    return {"message": f"Hello, {name}"}


@app.get("/grpc/{num_of_books}")
def grpc_unary(num_of_books: int = 1, name="World"):
    recommendations = curr_client.get_recommendations(num_of_books)
    return MessageToDict(recommendations)


@app.get("/rest/{num_of_books}")
def grpc_rest(num_of_books: int = 1, name="World"):
    url = f"http://localhost:50052/rest/{num_of_books}"
    resp = requests.get(url)

    if resp.ok:
        return {"recommendations": resp.json()}
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="ERROR")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3333)
