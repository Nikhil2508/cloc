from app.JavaCounter import JavaCounter
from app.PythonCounter import PythonCounter

VALID_EXTENSIONS = {
    "JAVA": {
        "class": JavaCounter,
        "extension": ".java"
    },
    "PYTHON": {
        "class": PythonCounter,
        "extension": ".py"
    }
}


TEST_DATA = {
    "python" : 'testData/python/test.py',
    "java" : 'testData/java/test.java'
}

VALID_EXTENSIONS_CLASSES = [JavaCounter, PythonCounter]
