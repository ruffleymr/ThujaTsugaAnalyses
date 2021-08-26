//Number of population samples (demes)
2
//Population effective sizes (number of genes)
N0$
N1$
//Sample sizes
54
60
//Growth rates: negative growth implies population expansion
Gro1$
Gro2$
//Number of migration matrices : 0 implies no migration between demes
2
//migrationmatrix
0 0
0 0
//migrationmatrix
0 MIG1$
MIG2$ 0
//historical event: time, source, sink, migrants, new size, new growth rate, migr. matrix
5 historical event
Tdiv1$ 0 1 1 Resize$ 0 keep
Tmig1end$ 0 0 0 1 0 0
TexpEnd$ 0 0 0 BtnMag$ 0 1
TexpEnd$ 1 1 0 BtnMag$ 0 1
0 0 0 0 1 keep 1
//Number of independent loci [chromosome]
986
//Per chromosome: Number of linkage blocks
1
//per Block: data type, num loc. rec. rate and mut rate + optional paramters
SNP 1 0 0 0.01
