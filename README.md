# Code Line Counter
## Overview
The Code Line Counter is a Python program designed to analyze and count the number of lines of code in a given file or folder. This program takes input of a file or folder path and outputs details of lines of code, comment and blank lines of the particular file/s.

## Features
Counts the total number of lines in a specified file or recursively in a folder.
Supports Python and Java and is extensible to use various other languages if required.
Provides a breakdown of lines into categories: code lines, comment lines, and blank lines.

## Installation

```
git clone <git url>

```

## Usage

```

cd cloc
python3 main.py

```

You will get 3 inputs as below

```
[1] Count Lines for a Folder

[2] Count Lines for a Single File

[q] Quit
```

On selecting any one, you have to enter a valid path like below

```

What would like to do?
1

Count Lines for a Folder


Please input folder path: 
testData/

```

# Output

```


Final Count for:  testData/python/test.py
Blank : 1
Comment : 1
Code : 4
Total : 6

Final Count for:  testData/java/test.java
Blank : 3
Comment : 3
Code : 6
Total : 12

```

# Run Tests

```

python3 -m unittest tests/*

```
