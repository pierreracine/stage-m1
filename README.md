# stage-m1

Repertoire for my stage in M1 theorical chemistry and modelisation.
Supervised by Pierre-François Loos.

Subject : how good are excited-state geometries within the Bethe-Salperter formalism ?
The goal is to compare energies of diatomic molecules, computed by TD-DFT or by BSE@GWA.

The first part of these scripts is dedicated to the (TD) DFT computations. Giving the 2 atoms, basis set and functionnal,
it creates input files for gaussian 16, runs them, extracts informations about energies and symmetry and plot the energy of
singlets and triplets states. Smooth plots were obtained by scan calculation and polynomial interpolation between each
point using scipy.interpolate.
