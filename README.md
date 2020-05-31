# MindPy
Repository containing source code of terminal based mind mapping application - `MindPy`.

# What is MindPy?
`MindPy` is terminal based tool which lets you create mind maps.

For a long time author of this tool searched for good and free mind mapping tool - without success. As he works mostly without GUI, the idea to write his own mapping tool which will be only console oriented was obvious. The efforts of his work you may find in this repository.

# Installation
Unfortunately, for now `MindMap` is not accessible from any package manager.

One of the biggest advantages of described tool is the fact it does not require installing any specific packages - it uses only Python standard library.
`requirements.txt` file is neccessary only for testing and contributing purposes.

How to install:  
_NOTE: You have to have python 3.x installed_
1. Clone the repository:  
`git clone https://github.com/lowerbyte/MindPy.git`
2. Enter the directory:  
`cd MindPy/`
3. Run `MindPy`:  
`python MindPy.py`

# Documentation
The best is to use either `--help` or `-h`:  
`python MindPy.py -h`  
The second way is typing `:h` directly in `MindPy`.

# Contributing
Feel free to cintribute to this piece of software.
Before creating a PR, run:  
`flake8` and `pytest`

![pic](/blob/readme_pic.png)