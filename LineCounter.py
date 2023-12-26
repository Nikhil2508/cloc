from app.utils import constants
from optparse import OptionParser
import os
import re
from app.JavaCounter import JavaCounter
from app.PythonCounter import PythonCounter

def addOptions():
    parser = OptionParser()
    parser.add_option('-p','--path', dest='path', help='Please provide a valid path')
    parser.add_option('-c','--choice', dest='choice', help='Please provide type of operation choice')
    return parser

def analyze_directory(directory_path, syntax_analyzer_classes):
    total_blank_lines = 0
    total_comment_lines = 0
    total_code_lines = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            for syntax_analyzer_class in syntax_analyzer_classes:
                if file.endswith(syntax_analyzer_class.FILE_EXTENSION):
                    file_path = os.path.join(root, file)
                    analyzer = syntax_analyzer_class(file_path)
                    obj = analyzer.analyze_file()
                    analyzer.print_results()
                    

if __name__ == "__main__":
    parser = addOptions()
    options, args = parser.parse_args()
    directory_path = options.path
    choice = options.choice
    if choice == str(1):
        syntax_analyzer_classes = constants.VALID_EXTENSIONS_CLASSES
        analyze_directory(directory_path, syntax_analyzer_classes)
    if choice == str(2):
        filename, file_extension = os.path.splitext(directory_path)
        obj = {}
        if file_extension == constants.VALID_EXTENSIONS.get("JAVA").get("extension"):
            obj = constants.VALID_EXTENSIONS.get("JAVA").get("class")(directory_path).analyze_file()
        if file_extension == constants.VALID_EXTENSIONS.get("PYTHON").get("extension"):
            obj = constants.VALID_EXTENSIONS.get("PYTHON").get("class")(directory_path).analyze_file()
        obj.print_results()