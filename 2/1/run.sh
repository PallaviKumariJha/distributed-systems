# python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. ./pattern.proto
python pattern_test_client.py $1 $2