import zerorpc
import os

class HelloRPC(object):
    def hello(self, name):
        os.system("C:\\Wizard_Latest\\ExecuteTestScript.bat")
        
        return "Hello, %s" % name
s = zerorpc.Server(HelloRPC(), heartbeat=None)
s.bind("tcp://*:4245")
s.run()
