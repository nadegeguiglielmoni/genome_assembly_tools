# Genome assembly tools
List of genome assembly tools

The category "Last update" takes into account commits and responses from the developers to issues.

## Genome assemblers
 
| Reads                        | Assembler                                                | Publication                      | Last update |
|:-----------------------------|:---------------------------------------------------------|:---------------------------------|:-----|
| __Short reads__              |                                                          |                                  |      | 
| __Low-accuracy long reads__  | [Canu](https://github.com/marbl/canu)                    | 10.1101/gr.215087.116            | 2021 |
|                              | [FALCON](https://github.com/PacificBiosciences/FALCON)   | 10.1038/nmeth.4035               | 2021 |
|                              | [Flye](https://github.com/fenderglass/Flye)              | 10.1038/s41587-019-0072-8        | 2022 |
|                              | [HINGE](https://github.com/HingeAssembler/HINGE)         | 10.1101/gr.216465.116            | 2021 |
|                              | [MECAT](https://github.com/xiaochuanle/MECAT)            | 10.1038/nmeth.4432               | 2019 |
|                              | [MECAT2](https://github.com/xiaochuanle/MECAT2)          | 10.1038/nmeth.4432               | 2020 |
|                              | [miniasm](https://github.com/lh3/miniasm)                | 10.1038/nmeth.4432               | 2020 |
|                              | [NECAT](https://github.com/xiaochuanle/NECAT)            | 10.1038/s41467-020-20236-7       | 2021 |
|                              | [NextDenovo](https://github.com/Nextomics/NextDenovo)    |                                  | 2022 |
|                              | [Ra](https://github.com/lbcb-sci/ra)                     | 10.1109/ISPA.2019.8868909        | 2020 |
|                              | [Raven](https://github.com/lbcb-sci/raven)               | 10.1038/s43588-021-00073-4       | 2021 |
|                              | [SMARTdenovo](https://github.com/ruanjue/smartdenovo)    | 10.20944/preprints202009.0207.v1 | 2021 |
|                              | [wtdbg](https://github.com/ruanjue/wtdbg)                |                                  | 2021 |
|                              | [wtdbg2](https://github.com/ruanjue/wtdbg2)              | 10.1038/s41592-019-0669-3        | 2021 |
| __High-accuracy long reads__ | [Flye](https://github.com/fenderglass/Flye)              | 10.1038/s41587-019-0072-8        | 2022 |
|                              | [HiCanu](https://github.com/marbl/canu)                  | 10.1101/gr.215087.116            | 2021 |
|                              | [hifiasm](https://github.com/chhylp123/hifiasm)          | 10.1038/s41592-020-01056-5       | 2022 |
|                              | [IPA](https://github.com/PacificBiosciences/pbipa)       |                                  | 2021 |
|                              | [LJA](https://github.com/AntonBankevich/LJA)             | 10.1101/2020.12.10.420448        | 2021 |
|                              | [mdBG](https://github.com/ekimb/rust-mdbg/)              | 10.1016/j.cels.2021.08.009       | 2021 |
|                              | [MBG](https://github.com/maickrau/MBG)                   | 10.1093/bioinformatics/btab004   | 2021 |
|                              | [NextDenovo](https://github.com/Nextomics/NextDenovo)    |                                  | 2022 |
|                              | [Peregrine](https://github.com/cschin/Peregrine)         |                                  | 2021 |
|                              | [Raven](https://github.com/lbcb-sci/raven)               | 10.1038/s43588-021-00073-4       | 2021 |
|                              | [wtdbg2](https://github.com/ruanjue/wtdbg2)              | 10.1038/s41592-019-0669-3        | 2021 |

## Assembly pre/post-processing

| Step               | Reads           | Tool                                                               | Publication                     | Last update |
|:-------------------|:----------------|:-------------------------------------------------------------------|:--------------------------------|:------------|
|__Long-read__       | __Short reads__ | [CoLoRMap](https://github.com/cchauve/CoLoRMap)                    | 10.1093/bioinformatics/btw463   | 2018        |
|__error correction__|                 | [Hercules](https://github.com/BilkentCompGen/Hercules)             | 10.1093/nar/gky724              | 2020        |
|                    |                 | [Jabba](https://github.com/biointec/jabba)                         | 10.1186/s13015-016-0075-7       | 2021        |
|                    |                 | [LoRDEC](https://gite.lirmm.fr/lordec/lordec-releases/-/wikis/home)| 10.1093/bioinformatics/btu538   | 2020        |
|                    |                 | [LoRMA](https://gite.lirmm.fr/lorma/lorma-releases/-/wikis/home)   | 10.1093/bioinformatics/btw321   | 2019        |
|                    |                 | [NaS](https://github.com/institut-de-genomique/NaS)                | 10.1186/s12864-015-1519-z       | 2018        |
|                    |                 | [proovread](https://github.com/BioInf-Wuerzburg/proovread)         | 10.1093/bioinformatics/btu392   | 2021        |
|                    | __Long reads__  | [Canu](https://github.com/marbl/canu)                              | 10.1101/gr.215087.116           | 2021        |
|                    |                 | [CONSENT](https://github.com/morispi/CONSENT)                      | 10.1038/s41598-020-80757-5      | 2022        |
|                    |                 | [Daccord](https://github.com/gt1/daccord)                          | 10.1101/106252                  | 2020        |
|                    |                 | [FLAS](https://github.com/baoe/FLAS)                               | 10.1093/bioinformatics/btz206   | 2019        |
|                    |                 | [HALC](https://github.com/lanl001/halc)                            | 10.1186/s12859-017-1610-3       | 2018        |
|                    |                 | [MECAT](https://github.com/xiaochuanle/MECAT)                      | 10.1038/nmeth.4432              | 2019        |
|                    |                 | [MECAT2](https://github.com/xiaochuanle/MECAT2)                    | 10.1038/nmeth.4432              | 2020        |
|                    |                 | [NECAT](https://github.com/xiaochuanle/NECAT)                      | 10.1038/s41467-020-20236-7      | 2021        |
|                    |                 | [NextDenovo](https://github.com/Nextomics/NextDenovo)              |                                 | 2022        |
|__Haplotig purging__| __Long reads__  | [HaploMerger2](https://github.com/mapleforest/HaploMerger2)        | 10.1093/bioinformatics/btx220   | 2021        |
|                    |                 | [purge_dups](https://github.com/dfguan/purge_dups)                 | 10.1093/bioinformatics/btaa025  | 2021        |
|                    |                 | [Purge Haplotigs](https://bitbucket.org/mroachawri/purge_haplotigs)| 10.1186/s12859-018-2485-7       | 2022        |
|__Scaffolding__     | __Long reads__  | [DENTIST](https://github.com/a-ludi/dentist)                       | 10.1093/gigascience/giab100     | 2022        |
|                    |                 | [LINKS](https://github.com/bcgsc/LINKS)                            | 10.1186/s13742-015-0076-3       | 2022        |
|                    | __Genetic maps__| [ALLMAPS](https://github.com/tanghaibao/jcvi/wiki/ALLMAPS)         | 10.1186/s13059-014-0573-1       | 2022        |
|                    | __Optical maps__| [AGORA](https://static-content.springer.com/esm/art%3A10.1186%2F1471-2105-13-189/MediaObjects/12859_2012_5306_MOESM3_ESM.zip)| 10.1186/1471-2105-13-189 | 2012        |
|                    |                 | [BiSCoT](https://github.com/institut-de-genomique/biscot)          | 10.7717/peerj.10150             | 2021        |
|                    |                 | [OMGS](https://github.com/ucrbioinfo/OMGS)                         | 10.1089/cmb.2019.0310           | 2021        |
|                    |                 | [SewingMachine](https://github.com/i5K-KINBRE-script-share/Irys-scaffolding/blob/master/KSU_bioinfo_lab/stitch/sewing_machine_LAB.md) | 10.1186/s12864-015-1911-8 | 2015        |
|                    |                 | [SOMA](ftp://ftp.cbcb.umd.edu/pub/software/soma)                   | 10.1093/bioinformatics/btn102   | 2008        |
|                    | __Linked reads__| [ARBitR](https://github.com/markhilt/ARBitR)                       | 10.1093/bioinformatics/btaa975  | 2021        |
|                    |                 | [Architect](https://github.com/kuleshov/architect)                 | 10.1093/bioinformatics/btw267   | 2016        |
|                    |                 | [ARCS](https://github.com/bcgsc/ARCS/)                             | 10.1093/bioinformatics/btx675   | 2022        |
|                    |                 | [ARKS](https://github.com/bcgsc/arks)                              | 10.1186/s12859-018-2243-x       | 2019        |
|                    |                 | [fragScaff](https://github.com/adeylab/fragScaff)                  | 10.1101/gr.178319.114           | 2018        |
|                    |                 | [scaff10X](https://github.com/wtsi-hpag/Scaff10X)                  |                                 | 2022        |
|                    | __Hi-C__        | [3D-DNA](https://github.com/aidenlab/3d-dna)                       | 10.1126/science.aal3327         | 2021        |
|                    |                 | [dnaTri](https://github.com/NoamKaplan/dna-triangulation)          | 10.1038/nbt.2768                | 2016        |
|                    |                 | [EndHiC](https://github.com/fanagislab/EndHiC)                     | 10.48550/arXiv.2111.15411       | 2022        |
|                    |                 | [GRAAL](https://github.com/koszullab/GRAAL)                        | 10.1038/ncomms6695              | 2018        |
|                    |                 | [HiCAssembler](https://github.com/maxplanck-ie/HiCAssembler)       | 10.1101/gad.328971.119          | 2019        |
|                    |                 | [instaGRAAL](https://github.com/koszullab/instaGRAAL)              | 10.1186/s13059-020-02041-z      | 2022        |
|                    |                 | [Lachesis](https://github.com/shendurelab/LACHESIS)                | 10.1038/nbt.2727                | 2017        |
|                    |                 | [pin_hic](https://github.com/dfguan/pin_hic)                       | 10.1186/s12859-021-04453-5      | 2021        |
|                    |                 | [SALSA2](https://github.com/marbl/SALSA)                           | 10.1371/journal.pcbi.1007273    | 2021        |
|                    |                 | [scaffHiC](https://github.com/wtsi-hpag/scaffHiC)                  |                                 | 2020        |
|                    |                 | [YaHS](https://github.com/c-zhou/yahs)                             |                                 | 2022        |
|__Gap filling__     | __Long reads__  | [Cobbler](https://github.com/bcgsc/RAILS)                          | 10.21105/joss.00116             | 2021        |
|                    |                 | [DENTIST](https://github.com/a-ludi/dentist)                       | 10.1093/gigascience/giab100     | 2022        |
|                    |                 | [FGAP](https://github.com/pirovc/fgap)                             | 10.1186/1756-0500-7-371         | 2021        |
|                    |                 | [GMcloser](https://sourceforge.net/projects/gmcloser/)             | 10.1093/bioinformatics/btv465   | 2018        |
|                    |                 | [LR_Gapcloser](https://github.com/CAFS-bioinformatics/LR_Gapcloser)| 10.1093/gigascience/giy157      | 2018        |
|                    |                 | [PBJelly](https://sourceforge.net/projects/pb-jelly/)              | 10.1371/journal.pone.0047768    | 2017        |
|                    |                 | PGcloser                                                           | 10.1177/1176934320913859        | 2020        |
|                    |                 | [TGS-GapCloser](https://github.com/BGI-Qingdao/TGS-GapCloser)      | 10.1093/gigascience/giaa094     | 2022        |
