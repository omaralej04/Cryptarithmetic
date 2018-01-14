class finishStatement:

    def responseDone(state):
        finished()

    def showResponse():
        file = open("response.txt", "r")
        content = file.readlines()
        print content.rstrip()
        finished()

    def destroyTest():
        os.remove("response.txt")
        print("All data is being removed!")
        finished()
