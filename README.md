# Decomposition Algorithms for Scalable Quantum Annealing (DASQA)
Exact graph decomposition algorithms for MaxClique and Minimum Vertex Cover problems. The aim of this project is to create graph decomposition algorithms for specific problems, which generate sub-problems that are small enough to be able to be solved on modern quantum annealers. 

```DBK``` in ```DBK.py``` performs graph decomposition for the Maximum Clique problem. 

```DBR``` in ```DBR.py``` performs graph decomposition for the Minimum Vertex Cover problem. 

Each of these functions use a user specified solver function. In order to validate the correctness of the algorithm, we can use an exact solver function. The purpose of these algorithms is to use a quantum annealer as the solver. 

```validate_DBK.py``` imports DBK and validates the algorithm using the exact solver provided in the ```networkx``` package

```validate_DBR.py``` does the same except with DBR

## How to cite Decomposition Algorithms for Scalable Quantum Annealing (DASQA)?
```latex
@inproceedings{pelofske2019solving,
  title={Solving large maximum clique problems on a quantum annealer},
  author={Pelofske, Elijah and Hahn, Georg and Djidjev, Hristo},
  booktitle={International Workshop on Quantum Technology and Optimization Problems},
  pages={123--135},
  year={2019},
  organization={Springer}
}

@inproceedings{pelofske2019solving,
  title={Solving large minimum vertex cover problems on a quantum annealer},
  author={Pelofske, Elijah and Hahn, Georg and Djidjev, Hristo},
  booktitle={Proceedings of the 16th ACM International Conference on Computing Frontiers},
  pages={76--84},
  year={2019}
}

@article{pelofske2021decomposition,
  title={Decomposition algorithms for solving NP-hard problems on a quantum annealer},
  author={Pelofske, Elijah and Hahn, Georg and Djidjev, Hristo},
  journal={Journal of Signal Processing Systems},
  volume={93},
  number={4},
  pages={405--420},
  year={2021},
  publisher={Springer}
}
```

## Authors
- [Elijah Pelofske](mailto:epelofske@lanl.gov): Information Sciences, Los Alamos National Laboratory
- [Georg Hahn](mailto:ghahn@hsph.harvard.edu): T.H. Chan School of Public Health, Harvard University
- [Hristo Djidjev](mailto:djidjev@lanl.gov): Information Sciences, Los Alamos National Laboratory

## Copyright Notice:
© 2020. Triad National Security, LLC. All rights reserved.
This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos
National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S.
Department of Energy/National Nuclear Security Administration. All rights in the program are
reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear
Security Administration. The Government is granted for itself and others acting on its behalf a
nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare
derivative works, distribute copies to the public, perform publicly and display publicly, and to permit
others to do so.

**LANL C Number: C19111**

## License:
This program is open source under the BSD-3 License.
Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and
the following disclaimer.

2.Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.

3.Neither the name of the copyright holder nor the names of its contributors may be used to endorse
or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
