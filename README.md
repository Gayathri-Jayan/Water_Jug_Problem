# Water Jug Problem Solver

**MFC Project**

This project solves the Water Jug Problem using Breadth-First Search (BFS). The application allows users to enter the capacities of two jugs and the required amount of water, then displays the steps needed to reach the target.

**Live Demo:** [Water Jug Problem Solver](https://water-jug-solver-zgcfjkasx5rqv2nsggwbnf.streamlit.app/)

**GitHub Repository:** [water-jug-solver](https://github.com/Gourikrishna1311/water-jug-solver)

## Features

- Enter the capacities of two water jugs and the target quantity.
- Find a solution using BFS.
- View the amount of water in each jug at every step.
- Navigate through the solution step by step.
- Visualize the state-space graph and solution path.
- Download the solution as a text file.

## Problem Description

The Water Jug Problem involves measuring a specific quantity of water using two jugs of different capacities. The available operations are filling a jug, emptying a jug, and pouring water from one jug into the other.

Each state is represented as `(x, y)`, where `x` and `y` denote the amounts of water in Jug A and Jug B, respectively.

The initial state is `(0, 0)`. The objective is to reach a state in which either jug contains the required quantity of water.

## Algorithm Used

Breadth-First Search (BFS) is used to explore the possible states of the problem. It visits states level by level and uses a queue to manage the search.

Visited states are tracked to avoid unnecessary repetition. Once the target state is found, the sequence of operations is used to display the solution.

Since every operation has equal cost, BFS finds the solution with the minimum number of operations.

## Technologies Used

- Python
- Streamlit
- NetworkX
- Matplotlib

## Project Files

| File | Purpose |
|---|---|
| `app.py` | Main application and user interface |
| `solver.py` | BFS algorithm and problem-solving logic |
| `graph_visualizer.py` | Graph visualization |
| `tests.py` | Test cases |
| `requirements.txt` | Required Python libraries |

## Installation and Execution

**1. Clone the repository**

```bash
git clone https://github.com/Gourikrishna1311/water-jug-solver.git
```

**2. Open the project folder**

```bash
cd water-jug-solver
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## Example

Consider two jugs with capacities of 4 litres and 3 litres. The target is to measure 2 litres.

| Step | Operation | State (A, B) |
|---|---|---|
| 0 | Start | (0, 0) |
| 1 | Fill Jug B | (0, 3) |
| 2 | Pour B into A | (3, 0) |
| 3 | Fill Jug B | (3, 3) |
| 4 | Pour B into A | (4, 2) |

The target is reached in four operations.

## Testing

The solver was tested using seven test cases covering different target quantities and solution conditions.

To run the tests:

```bash
python -m pytest tests.py -v
```

## Conclusion

This project demonstrates how BFS can be used to solve the Water Jug Problem by representing possible configurations as graph states. The web interface makes it easier to understand the operations and follow the solution.

**Project:** Water Jug Problem Solver  
**Subject:** MFC
