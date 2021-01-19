# Decomposition-Algorithms-for-Scalable-Quantum-Annealing
Exact graph decomposition algorithms for MaxClique and Minimum Vertex Cover problems. The aim of this project is to create graph decomposition algorithms for specific problems, which generate sub-problems that are small enough to be able to be solved on modern quantum annealers. 

```DBK``` in ```DBK.py``` performs graph decomposition for the Maximum Clique problem. 

```DBR``` in ```DBR.py``` performs graph decomposition for the Minimum Vertex Cover problem. 

Each of these functions use a user specified solver function. In order to validate the correctness of the algorithm, we can use an exact solver function. The purpose of these algorithms is to use a quantum annealer as the solver. 

```validate_DBK.py``` imports DBK and validates the algorithm using the exact solver provided in the ```networkx``` package

```validate_DBR.py``` does the same except with DBR

# Los Alamos National Laboratory Open Source Release
C19111 Decomposition Algorithms for Scalable Quantum Annealing

