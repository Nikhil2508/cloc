from app.BaseCounter import Base
import ast

class PythonCounter(Base):
    FILE_EXTENSION = ".py"
    def analyze_file(self):
        with open(self.file_path, 'r') as file:
            inside_multi_line_comment = False
            for line in file:
                line = line.strip()

                if not line:
                    self.blank_lines += 1
                elif line.startswith('#'):
                    if not self.check_valid_comment(line[1:]):
                        self.comment_lines += 1
                elif '"""' in line or "'''" in line:
                    if inside_multi_line_comment:
                        inside_multi_line_comment = False
                    else:
                        inside_multi_line_comment = True
                        if not self.check_valid_comment(line[1:]):
                            self.comment_lines += 1
                elif inside_multi_line_comment:
                    if not self.check_valid_comment(line[1:]):
                        self.comment_lines += 1
                else:
                    self.code_lines += 1
        return self
    
    def check_valid_comment(self,line):
        try:
            ast.parse(line)
            return True
        except SyntaxError:
            return False