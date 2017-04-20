# Author: Pallavi
# Created on : 7th February 2017
# Modified on:

# pattern RPC client

# Standard library imports
import json
import sys

# Imports from third party packages
import grpc

# Imports from current project
import pattern_pb2

def print_char(response):
    S_VAL = response.challenge.start
    E_VAL = response.challenge.end
    P_VAL = response.challenge.step
    P_VAL = int(P_VAL)
    length = ord(E_VAL) - ord(S_VAL)
    # put upperCase and lower case checks
    if length == 0:
        print "length is zero"
    else:
        value = ' '.join(chr(c) for c in range(ord(S_VAL), ord(E_VAL)+1, P_VAL))
        return value

def run():
    host = sys.argv[1]
    port = sys.argv[2]
    channel = grpc.insecure_channel('%s:%s' % (host, port))
    stub = pattern_pb2.PatternGenTestStub(channel)
    success = True
    response = stub.GetChallenge(pattern_pb2.ChallengeRequest())

    # call function to get the answer
    ansToChallenge = print_char(response)

    response = stub.GetChallenge(pattern_pb2.ChallengeRequest(solution=ansToChallenge))
    
    # got correct answer for first challenge
    # keep solving until client passes all test
    while response.correct:
        ansToChallenge = print_char(response)
        response = stub.GetChallenge(pattern_pb2.ChallengeRequest(solution=ansToChallenge))

        if response.status_msg:
            if response.status_msg == "Yaay! All challenges solved!":
                print response.status_msg
                break;

    if response.correct:
        print("Success")
    else:
        print("Failure")
    return


if __name__ == "__main__":
    run()
