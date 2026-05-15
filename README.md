# 8-Queens Genetic Algorithm Solver

A specialized Artificial Intelligence project that solves the classic **8-Queens Puzzle** using a **Genetic Algorithm (GA)**. This project demonstrates the transition from systematic uninformed search to evolutionary meta-heuristics, as explored in **Lectures** of the Autonomous Multiagent Systems course at **FCAI-CU**.

## 🧠 The AI Logic
[cite_start]Unlike standard search algorithms that maintain a single state, this solver utilizes a **Population-based Meta-heuristic**. It simulates natural selection to "evolve" a solution where 8 queens are placed on an 8x8 board such that no two queens attack each other.

### [cite_start]**The Genetic Cycle** 
1. [cite_start]**Initial Population**: Generates a set of random 8-digit chromosomes where each index is a column and the value is the row.
2. **Fitness Evaluation**: Calculates the number of **non-attacking pairs**. A perfect solution has a fitness of **28**.
3. [cite_start]**Selection**: Picks the "fittest" individuals to act as parents for the next generation.
4. [cite_start]**Crossover**: Combines the "genetic" material of two parents at a random split point.
5. [cite_start]**Mutation**: Introduces random variations to prevent the algorithm from getting stuck in local maxima.

## 🎨 UI/UX Features
* **Evolution Visualization**: A real-time GUI showing the board state of the best chromosome in each generation.
* **Fitness Tracker**: Visual feedback on the number of attacking vs. non-attacking pairs.
* **Performance Metrics**: Displays generation count and population diversity.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the GUI: `python gui.py`
3. Run the Terminal trace: `python main.py`

## 🛠 PEAS Analysis
* **Performance**: Reaching a fitness of 28 (zero clashes).
* **Environment**: 8x8 Chessboard (Static, Discrete, Deterministic).
* **Actuators**: Row position changes for each column.
* **Sensors**: Current row positions of all 8 queens.