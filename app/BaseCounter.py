class Base:
    def __init__(self, file_path):  # Constructor to initialize name and age attributes
        self.file_path = file_path
        self.blank_lines = 0
        self.comment_lines = 0
        self.code_lines = 0
    
    def analyze_file(self):
        raise NotImplementedError("Implementation not done")

    def print_results(self):
        print("\fFinal Count for: ", self.file_path)
        print(f"Blank : {self.blank_lines}")
        print(f"Comment : {self.comment_lines}")
        print(f"Code : {self.code_lines}")
        total_lines = self.blank_lines + self.comment_lines + self.code_lines
        print(f"Total : {total_lines}")