# PrintY

Recursively concatenates files in directory to indented
markdown code-blocks, with filenames as headers.

**If you want to print a bunch of code out on paper - this is the tool for you!**

## Installation

Requires **python3** and **docopt** to be installed,
the file is self contained so just drop it somewhere.

    pip install docopt

    # make it executable
    chmod +x printy.py

## Usage

In this example I'm using a testfolder with the following structure:

    testfolder
    ├── subfolder
    │   └── testfile3.txt
    ├── testfile1.txt
    └── testfile2.txt

To use `printy.py`, simply:

    ./printy.py testfolder

The ouput will be:

---

# testfolder

## testfolder/testfile1.txt

    Contents of testfile1.txt

## testfolder/testfile2.txt

    Contents of testfile2.txt

## testfolder/subfolder/testfile3.txt

    Contents of testfile3.txt

