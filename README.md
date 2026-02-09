# 🌊 Aquatic Drone Navigation - AI Exam

This project implements **Reinforcement Learning** algorithms to navigate an advanced aquatic drone through a dynamic underwater environment. The goal is to find the optimal policy to travel from a starting point to a research site, maximizing energy efficiency while avoiding obstacles and utilizing currents.

---

## 📌 Problem Description

An aquatic drone is deployed to collect data on marine biodiversity. It starts at point $S$ (near the shore) and must navigate to point $G$ (a coral reef).

### Environment Details (Grid World 10x10)
The environment is a grid where the agent must manage energy consumption and stochastic elements.

* **Start ($S$):** Position `(0, 0)`.
* **Goal ($G$):** Position `(9, 7)`. Reaching this provides a reward of **+20.0** and ends the episode.
* **Move Cost:** Standard energy cost of **-0.04** per step.

#### Terrain Types & Rewards
| Type | Symbol | Description | Effect / Reward |
| :--- | :---: | :--- | :--- |
| **Open Water** | `O` | Normal movement. | Standard cost (-0.04). |
| **Currents** | `C` | Strong ocean currents. | **Stochastic:** 80% intended move, 10% drift Left, 10% drift Right. |
| **Seaweed** | `F` | Dense vegetation. | Additional penalty of **-0.2** (Total cost: -0.24). |
| **Energy Stations** | `E` | Charging points. | Bonus reward of **+1.0** when visited. |

---

## 🧠 Algorithms Implemented

To solve this MDP (Markov Decision Process), two Dynamic Programming algorithms were implemented and compared:

### 1. Value Iteration
* **Approach:** Iteratively updates the value function $V(s)$ until the change ($\Delta$) is below a threshold (`maxDifferenza`).
* **Convergence:** Asymptotic. It stops when the values stabilize close to the optimal solution.

### 2. Policy Iteration
* **Approach:** Alternates between *Policy Evaluation* and *Policy Improvement*.
* **Convergence:** Converges to the exact optimal policy in a finite number of iterations.
* **Trade-off:** Often requires fewer iterations than Value Iteration, but each iteration is computationally more expensive.

---

## 📊 Results & Analysis

### Algorithm Comparison
Both algorithms successfully converge to the same optimal policy.
* **Value Iteration** is faster per iteration but requires more loops to reach the mathematical threshold.
* **Policy Iteration** explores options systematically and finds the exact policy with fewer total loops, though at a higher computational cost per step depending on the state space size.

### Critical Analysis: Energy Station Routing
**Question:** *Does the optimal solution guarantee that the drone passes by at least two charging stations (`E`) in every possible execution?*

**Answer: NO.**
Due to the stochastic nature of the **Currents (C)**, a deterministic path cannot be guaranteed 100% of the time.
* Specifically, at cell `(4, 1)`, the optimal action is `DOWN`.
* However, there is a **10% probability** that the current pushes the drone to the `RIGHT`.
* If this deviation occurs, the drone is forced onto a path that misses the second column of energy stations. Therefore, passing two stations is **not guaranteed** for every execution.

---

Project developed for the Artificial Intelligence course.
