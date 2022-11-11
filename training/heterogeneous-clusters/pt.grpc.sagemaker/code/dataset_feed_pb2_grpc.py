# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dataset_feed_pb2 as dataset__feed__pb2


class DatasetFeedStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_examples = channel.unary_stream(
                '/DatasetFeed/get_examples',
                request_serializer=dataset__feed__pb2.Dummy.SerializeToString,
                response_deserializer=dataset__feed__pb2.Example.FromString,
                )
        self.shutdown = channel.unary_unary(
                '/DatasetFeed/shutdown',
                request_serializer=dataset__feed__pb2.Dummy.SerializeToString,
                response_deserializer=dataset__feed__pb2.Dummy.FromString,
                )


class DatasetFeedServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_examples(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasetFeedServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_examples': grpc.unary_stream_rpc_method_handler(
                    servicer.get_examples,
                    request_deserializer=dataset__feed__pb2.Dummy.FromString,
                    response_serializer=dataset__feed__pb2.Example.SerializeToString,
            ),
            'shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.shutdown,
                    request_deserializer=dataset__feed__pb2.Dummy.FromString,
                    response_serializer=dataset__feed__pb2.Dummy.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DatasetFeed', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasetFeed(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_examples(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/DatasetFeed/get_examples',
            dataset__feed__pb2.Dummy.SerializeToString,
            dataset__feed__pb2.Example.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatasetFeed/shutdown',
            dataset__feed__pb2.Dummy.SerializeToString,
            dataset__feed__pb2.Dummy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)