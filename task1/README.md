## Task 1: Counting islands
The program calculates number of islands in a matrix MxN that represents map. 1 - island; 0 - ocean.
Depth First Search algorithm is used to solve the task.
Two input methods are supported:
* console
* `.txt` file  

To specify a method one should set `MODE` and `DATA_PATH` variables in the `config.py` (by default, method is console).

**Structure of `.txt` file**
```angular2html
3 3  - matrix size M N
0 1 0
0 0 0
0 1 1
2   - expected number of islands
```

### Requirements
* Python 3.10

### How to run
1. Set execution mode as described above
2. Run `islands_counter.py`

