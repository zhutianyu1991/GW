from pyscf.pbc import gto, dft, scf, df
from pyscf.pbc.lib import chkfile
import os
from GW.pbc import krgw_ac
from GW.pbc import krgw_cd
'''
Check PySCF dev branch
from pyscf.pbc.gw import krgw_ac
from pyscf.pbc.gw import krgw_cd
'''

# This example takes a few minutes
cell = gto.Cell()
cell.build(unit = 'angstrom',
        a = '''
            0.000000     1.783500     1.783500
            1.783500     0.000000     1.783500
            1.783500     1.783500     0.000000
        ''',
        atom = 'C 1.337625 1.337625 1.337625; C 2.229375 2.229375 2.229375',
        dimension = 3,
        max_memory = 2000,
        verbose = 4,
        pseudo = 'gth-pade',
        basis='gth-dzv',
        precision=1e-10)

kpts = cell.make_kpts([2,2,2],scaled_center=[0,0,0])
gdf = df.GDF(cell, kpts)
gdf_fname = 'gdf_ints_222.h5'
gdf._cderi_to_save = gdf_fname
if not os.path.isfile(gdf_fname):
    gdf.build()

chkfname = 'diamond_222.chk'
if os.path.isfile(chkfname):
    kmf = dft.KRKS(cell, kpts)
    kmf.xc = 'pbe'
    kmf.with_df = gdf
    kmf.with_df._cderi = gdf_fname
    data = chkfile.load(chkfname, 'scf')
    kmf.__dict__.update(data)
else:
    kmf = dft.KRKS(cell, kpts)
    kmf.xc = 'pbe'
    kmf.with_df = gdf
    kmf.with_df._cderi = gdf_fname
    kmf.conv_tol = 1e-12
    kmf.chkfile = chkfname
    kmf.kernel()

# GW-AC
gw = krgw_ac.KRGWAC(kmf)
# without finite size corrections
gw.fc = False
nocc = gw.nocc
gw.kernel(kptlist=[0],orbs=range(0,nocc+3))
print(gw.mo_energy)

# with finite size corrections
gw.fc = True
gw.kernel(kptlist=[0],orbs=range(0,nocc+3))
print(gw.mo_energy)

# GW-CD with fc
gw = krgw_cd.KRGWCD(kmf)
gw.fc = True
gw.kernel(kptlist=[0],orbs=range(0,nocc+3))
print(gw.mo_energy)
