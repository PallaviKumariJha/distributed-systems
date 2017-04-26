# Author: Pallavi
# Created on : 7th February 2017
# Modified on:

# fibonacciRPC server
# Most of the following code is inspired 
#from the sample code provided for client challenge

# Standard library imports
import concurrent
import json
import os
import sys
import time

# Imports from third party packages
import grpc

# Imports from current project
import fibonacci_pb2

class ChallengeServer(fibonacci_pb2.FibonacciComputerServicer):
    def __init__(self):
        super(ChallengeServer, self).__init__()
        self.current_count = 0
        self.success_msg = "Yaay! All challenges solved!"
        self.trial_count = 50
        return

    # takes the request finds the nth fibonacci
    def GetNthFibonacciNumber (self, request, context):
        n = (request.number -1)
        a, b = 0, 1
        if n == 0:
            response = 0
        elif n == 1:
            response = 1
        else:
            while n > 0:
                a, b = b, a + b
                n = n-1
            response = a
        response = fibonacci_pb2.FibResponse(
                    # covert long to str type
                    number = str(response)
                   )
        return response

  
def serve():
    if len(sys.argv) != 2:
        print("Usage: %s Give port number" % (sys.argv[0]))
        sys.exit(1)

    port = int(sys.argv[1])
    if port < 1 or port >= pow(2, 16):
        print("Port number should lie between 1 and 65535")
        sys.exit(1)
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    fibonacci_pb2.add_FibonacciComputerServicer_to_server(ChallengeServer(), server)
    server.add_insecure_port('[::]:%d' % (port))
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

    return


if __name__ == "__main__":
    serve()
