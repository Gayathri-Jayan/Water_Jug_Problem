
# 💧 Water Jug Problem Solver

**MFC Project P009 | Graph Theory Lab**

An interactive web application that solves the classic Water Jug Problem using **Breadth-First Search (BFS)**. Built with Python and Streamlit, it finds the shortest sequence of operations to reach a target quantity and visualizes the solution through interactive state-space graphs and step-by-step water simulation.

**🚀 Live Demo:** [Water Jug Problem Solver](https://water-jug-solver.streamlit.app/)

**📂 GitHub Repository:** [Water Jug Problem Solver](https://github.com/Gayathri-Jayan/Water_Jug_Problem)

---

## ✨ Features

- Solve the Water Jug Problem using BFS.
- Configure the capacities of both jugs and the target quantity.
- Find a solution with the minimum number of operations.
- View water levels through live simulation.
- Navigate through solution steps using Previous and Next controls.
- Visualize the complete state-space graph.
- View the shortest solution path with highlighted transitions.
- Explore solution traces and visited states.
- Download the solution as a text file.
- Automated testing with pytest.

---

## 📸 Application Screenshots

### 1. Live Water Simulation

Observe the water levels in both jugs and navigate through the solution step by step.

![Live Water Simulation](screenshots/live-simulation.png)

### 2. State-Space Graph

Explore reachable states and transitions, including the initial state, goal states, and BFS solution transitions.

![Water Jug State-Space Graph](screenshots/state-space-graph.png)

### 3. BFS Shortest Solution Path

Visualize the shortest path from the initial state to the target state.

![BFS Shortest Solution Path](screenshots/shortest-path.png)

---

## 🧩 Problem Description

The Water Jug Problem involves measuring a specific quantity of water using two jugs of different capacities.

The permitted operations are:

1. Fill either jug completely.
2. Empty either jug.
3. Pour water from one jug into the other until the source is empty or the destination is full.

Each state is represented as `(x, y)`, where:

- `x` is the amount of water in Jug A.
- `y` is the amount of water in Jug B.

The initial state is `(0, 0)`. The objective is to reach a state in which either jug contains the required target quantity.

---

## 🧠 Algorithm Used: Breadth-First Search (BFS)

The problem is represented as a state-space graph:

- **Nodes:** Possible water configurations `(x, y)`.
- **Edges:** Valid operations that transform one state into another.
- **Initial state:** `(0, 0)`.
- **Goal state:** A state in which either jug contains the target quantity.

BFS explores states level by level using a queue. A visited-state set prevents repeated exploration, and the solution path records the operations needed to reach the target.

Since every operation has equal cost, BFS finds a solution with the minimum number of operations whenever a solution exists.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language and solver logic |
| Streamlit | Interactive web application interface |
| NetworkX | State-space graph creation and manipulation |
| Plotly | Interactive graph visualization |
| pytest | Automated testing |

---

## 📁 Project Structure

```text
water-jug-solver/
├── app.py
├── solver.py
├── graph_visualizer.py
├── test_solver.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── live-simulation.png
    ├── state-space-graph.png
    └── shortest-path.png
```

| File or Folder | Purpose |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `solver.py` | BFS algorithm and problem-solving logic |
| `graph_visualizer.py` | State-space graph and shortest-path visualization |
| `test_solver.py` | Automated tests for the solver |
| `requirements.txt` | Required Python packages |
| `screenshots/` | Application screenshots used in this README |

---

## ⚙️ Installation and Execution

### Prerequisites

- Python 3.10 or later
- Git
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Gayathri-Jayan/Water_Jug_Problem.git
```

### 2. Open the project folder

```bash
cd Water_Jug_Problem
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

---

## ▶️ Example

Consider two jugs with capacities of **6 litres** and **4 litres**, with a target of **2 litres**.

| Step | Operation | State (A, B) |
|---:|---|---|
| 0 | Initial state | `(0, 0)` |
| 1 | Fill Jug A | `(6, 0)` |
| 2 | Pour Jug A into Jug B | `(2, 4)` |

The target of 2 litres is reached in **2 operations**.

---

## 🧪 Testing

The solver has **11 automated tests passing**, covering solvable and unsolvable configurations, zero targets, jug-capacity boundaries, and other edge cases.

Run the tests using:

```bash
python -m pytest -v
```

Expected result:

```text
11 passed
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Applying graph-search algorithms to a classic problem.
- Representing configurations as graph states.
- Using BFS to find shortest paths in an unweighted graph.
- Visualizing state transitions and solution paths.
- Developing an interactive application using Streamlit.
- Testing algorithmic behavior with pytest.

---

## 🏁 Conclusion

The Water Jug Problem Solver combines graph theory, Breadth-First Search, and interactive visualization to demonstrate how search algorithms explore possible states and find shortest solutions. Its simulation and graph views make the problem easier to understand and explore.

**Project:** Water Jug Problem Solver  
**Project ID:** MFC P009  
**Subject:** MFC — Graph Theory Lab
