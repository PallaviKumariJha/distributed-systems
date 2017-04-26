python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. ./fibonacci.proto
python fibonacci_test_server.py $1
