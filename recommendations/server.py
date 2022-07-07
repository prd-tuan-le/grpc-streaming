import os
import time
import hashlib
from concurrent import futures

import grpc
from faker import Faker
from faker.providers import DynamicProvider

import recommendations_pb2
import recommendations_pb2_grpc


book_provider = DynamicProvider(
    provider_name="book",
    elements=[
        "The Maltese Falcon",
        "Murder on the Orient Express",
        "The Hound of the Baskervilles",
        "The Hitchhiker's Guide to the Galaxy",
        "Ender's Game",
        "The Dune Chronicles",
        "The 7 Habits of Highly Effective People",
        "How to Win Friends and Influence People",
        "Man's Search for Meaning",
    ],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(book_provider)


class RecommendationsServicer(recommendations_pb2_grpc.RecommendationsServicer):
    """
    gRPC server for Recommendation Service
    """

    def __init__(self, port=50051, max_books=10_000_000) -> None:
        self.server_port = port
        self.max_books = max_books
        self.books = []

    def _generate_books(self):
        print(f"Generating {self.max_books} books...")
        for i in range(self.max_books):
            self.books.append(recommendations_pb2.BookRecommendation(id=i, title=fake.book()))
        print("Done!")

    def get_recommend_books(self, request, context):
        """Unary gRPC"""
        max_results = request.max_results
        books_to_recommend = []
        for i in range(max_results):
            books_to_recommend.append(recommendations_pb2.BookRecommendation(id=i, title=fake.book()))

        return recommendations_pb2.BookRecommendations(recommendations=books_to_recommend)

    def get_recommend_stream(self, request, context):
        """Streaming gRPC"""
        max_results = request.max_results

        for i in range(max_results):
            yield recommendations_pb2.BookRecommendation(id=i, title=fake.book())

    def start_server(self):
        """
        Function which actually starts the gRPC server, and preps
        it for serving incoming connections
        """
        # declare a server object with desired number
        # of thread pool workers.
        recommendation_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # add recommendations service
        recommendations_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationsServicer(), recommendation_server)

        # bind the server to the port defined above
        recommendation_server.add_insecure_port(f"[::]:{self.server_port}")

        # start the server
        recommendation_server.start()
        print("Recommendations Server running ...")

        try:
            # need an infinite loop since the above
            # code is non blocking, and if I don't do this
            # the program will exit
            while True:
                time.sleep(60 * 60 * 60)
        except KeyboardInterrupt:
            recommendation_server.stop(0)
            print("Recommendations Server Stopped ...")


curr_server = RecommendationsServicer(port=50051)
curr_server.start_server()
