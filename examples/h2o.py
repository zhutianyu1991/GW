from pyscf import gto, dft, scf
import gw_ac
import gw_cd

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
gw.linearized = True
gw.kernel()
print(gw.mo_energy)

# GW-CD
gw = gw_cd.GWCD(mf)
gw.kernel()
print(gw.mo_energy)
