import threading
import Helper

class NumberGenerator:
    def __init__(self):
        self.result = None

    def generateNumber(self):
        # Generate a number here
        self.result = Helper.generatePrime()

    def get_result(self):
        return self.result

def worker(obj):
    """Thread worker function"""
    obj.generateNumber()

pGenerator = NumberGenerator()
qGenerator = NumberGenerator()

# Create a new thread and start it
threadP = threading.Thread(target=worker, args=(pGenerator,))
threadQ = threading.Thread(target=worker, args=(qGenerator,))
threadP.start()
threadQ.start()

# Wait for the thread to finish
threadP.join()
threadQ.join()
        
p = pGenerator.get_result()