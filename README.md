# GW
Gaussian-based O(N<sup>4</sup>) G<sub>0</sub>W<sub>0</sub> codes for molecules and periodic systems implemented in PySCF \
Reference:\
All-electron Gaussian-based G<sub>0</sub>W<sub>0</sub> for Valence and Core Excitation Energies of Periodic Systems, T. Zhu and G. K.-L. Chan, arXiv: 2007.03148 (2020)

Molecules:
- gw_ac.py: molecular G<sub>0</sub>W<sub>0</sub> code using analytic continuation scheme
- gw_cd.py: molecular G<sub>0</sub>W<sub>0</sub> code using contour deformation scheme
- ugw_ac.py: molecular spin-unrestricted G<sub>0</sub>W<sub>0</sub> code using analytic continuation scheme

Solids:
- krgw_ac.py: PBC G<sub>0</sub>W<sub>0</sub> code using analytic continuation scheme
- krgw_cd.py: PBC G<sub>0</sub>W<sub>0</sub> code using contour deformation scheme
- kugw_ac.py: PBC spin-unrestricted G<sub>0</sub>W<sub>0</sub> code using analytic continuation scheme
