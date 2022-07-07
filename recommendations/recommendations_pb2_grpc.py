# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recommendations_pb2 as recommendations__pb2


class RecommendationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_recommend_books = channel.unary_unary(
                '/recommendations.Recommendations/get_recommend_books',
                request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.BookRecommendations.FromString,
                )
        self.get_recommend_stream = channel.unary_stream(
                '/recommendations.Recommendations/get_recommend_stream',
                request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.BookRecommendation.FromString,
                )


class RecommendationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_recommend_books(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_recommend_stream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_recommend_books': grpc.unary_unary_rpc_method_handler(
                    servicer.get_recommend_books,
                    request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.BookRecommendations.SerializeToString,
            ),
            'get_recommend_stream': grpc.unary_stream_rpc_method_handler(
                    servicer.get_recommend_stream,
                    request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.BookRecommendation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recommendations.Recommendations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_recommend_books(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommendations.Recommendations/get_recommend_books',
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.BookRecommendations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_recommend_stream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/recommendations.Recommendations/get_recommend_stream',
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.BookRecommendation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)