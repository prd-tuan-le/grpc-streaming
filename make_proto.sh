python -m grpc_tools.protoc \
    -I protobufs \
    --proto_path=protobufs \
    --python_out=recommendations \
    --grpc_python_out=recommendations \
    protobufs/recommendations.proto
