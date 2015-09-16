import zerorpc
import os

class HelloRPC(object):
    def hello(self, name):
        os.system("C:\\RF_Test_SauceLabs\\ExecuteTestScript.bat")
        
        return "Hello, %s" % name
s = zerorpc.Server(HelloRPC(), heartbeat=100)
s.bind("tcp://*:4245")
s.run()
