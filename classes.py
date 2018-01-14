class finishStatement:

    def responseDone(state):
        if state:
            finished()
        else:
            print "The program didn't end with a solution! Halting"

    def showResponse(response):
        content = open(response, "r")
        content.readlines()
        print content.rstrip()
        finished()

    def destroyTest(response):
        os.remove(response)
        print("All data is being removed!")
        finished()

class infoProcessing:

    #Extracts the inputs to process
    def extract(inputs):
        with open(inputs) as f:
            content = f.readlines()
            content = [x.strip('\n') for x in f.readlines()]
        return content

    def compare(inputs, outputs):
        #todo
