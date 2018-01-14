# -*- coding: utf-8 -*-
import os
import sys
import re
from classes import *

state = finishStatement
info = infoProcessing

inputs = "inputs.txt"
outputs = "outputs.txt"

def initializeProgram():
    global response
    response = raw_input("INPUT A NAME FOR THE RESPONSE OR LEAVE BLANK FOR DEFAULT (response.txt) > ")
    if response == "":
        response = "response.txt"
    solutionEngine()

def solutionEngine():
    info.extract(inputs)
    contentFile = inputs

    for case in inputs:
        #ex "WHAT + WAS + THY == CAUSE"
        regex = re.compile('[^a-zA-Z ]')
        regex.sub('', case)


    info.extract(outputs)
    contentFile = outputs

    info.compare(solution, outputs)

    #Writes a solution
    responseFile(solution)
    #Declares if the solution is ready
    state.responseDone(state)

def responseFile(solution):
    fileResponse = open(response, "a+")
    fileResponse.write(solution + '\n')
    fileResponse.close

def finished():
    print("Solver finished, say 'data' to show the result, 'delete' to destroy the response file or 'exit'")
    userR = raw_input("> ")
    if userR == "data":
        state.showResponse()
    elif userR == "delete":
        state.destroyTest()
    elif userR == "exit":
        sys.exit()

initializeProgram()
