from app.BaseCounter import Base

class JavaCounter(Base):
    FILE_EXTENSION = ".java"

    def analyze_file(self):
        with open(self.file_path, 'r') as file:
            inside_multi_line_comment = False
            for line in file:
                line = line.strip()
                if not line:
                    self.blank_lines += 1
                elif line.startswith('//'):
                    self.comment_lines += 1
                elif '/*' in line:
                    self.comment_lines += 1
                    inside_multi_line_comment = True
                elif '*/' in line:
                    self.comment_lines += 1
                    inside_multi_line_comment = False
                elif inside_multi_line_comment:
                    self.comment_lines += 1
                else:
                    self.code_lines += 1
        return self
