from pyscf import gto, dft, scf
from GW.mol import gw_ac
from GW.mol import gw_cd
'''
Check PySCF dev branch
from pyscf.gw import gw_ac
from pyscf.gw import gw_cd
'''

mol = gto.Mole()
mol.verbose = 4
mol.atom = '''
O  0.0000 0.0000 0.0000
H  0.7571 0.0000 0.5861
H -0.7571 0.0000 0.5861
'''
mol.basis = 'def2-svp'
mol.build()

mf = dft.RKS(mol)
mf.xc = 'pbe'
mf.kernel()

# GW-AC
gw = gw_ac.GWAC(mf)
# solve QP equation iteratively
gw.kernel()
print(gw.mo_energy)

# solve linearized QP equation
gw = gw_ac.GWAC(mf)
gw.linearized = True
gw.kernel()
print(gw.mo_energy)

# frozen O-1s core
gw = gw_ac.GWAC(mf)
gw.frozen = 1
gw.kernel()
print (gw.mo_energy)

# GW-CD
gw = gw_cd.GWCD(mf)
gw.kernel()
print(gw.mo_energy)
