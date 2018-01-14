# -*- coding: utf-8 -*-
import os
import sys
from

def initializeProgram():
    global file
    file = raw_input("INPUT A NAME FOR THE RESPONSE OR LEAVE BLANK FOR DEFAULT (response.txt) > ")
    if file == "":
        file = "response.txt"

def finished():
    print("Solver finished, say 'data' to show the result, 'delete' to destroy the response file or 'exit'")
    userR = raw_input("> ")
    if userR == "data":
        showResponse()
    elif userR == "delete":
        destroyTest()
    elif userR == "exit":
        sys.exit()

def responseFile(solution, file):
    file = open(file, "a+")
    file.write(solution + '\n')
    file.close


def solutionEngine(inputFile):
    for inputs in inputFile:
        #logic goes here
        responseFile(solution)

def inputExtractor(file):
    for data in inputFile:

solutionEngine()
