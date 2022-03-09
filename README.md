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

| Step               | Reads         | Tool                                                               | Publication                     | Last update |
|:-------------------|:--------------|:-------------------------------------------------------------------|:--------------------------------|:------------|
|__Haplotig purging__| __Long reads__| [HaploMerger2](https://github.com/mapleforest/HaploMerger2)        | 10.1093/bioinformatics/btx220   | 2021        |
|                    |               | [purge_dups](https://github.com/dfguan/purge_dups)                 | 10.1093/bioinformatics/btaa025  | 2021        |
|                    |               | [Purge Haplotigs](https://bitbucket.org/mroachawri/purge_haplotigs)| 10.1186/s12859-018-2485-7       | 2022        |
|__Scaffolding__     | __Hi-C__      | [3D-DNA](https://github.com/aidenlab/3d-dna)                       | 10.1126/science.aal3327         | 2021        |
|                    |               | [dnaTri](https://github.com/NoamKaplan/dna-triangulation)          | 10.1038/nbt.2768                | 2016        |
|                    |               | [EndHiC](https://github.com/fanagislab/EndHiC)                     | 10.48550/arXiv.2111.15411       | 2022        |
|                    |               | [GRAAL](https://github.com/koszullab/GRAAL)                        | 10.1038/ncomms6695              | 2018        |
|                    |               | [HiCAssembler](https://github.com/maxplanck-ie/HiCAssembler)       | 10.1101/gad.328971.119          | 2019        |
|                    |               | [Lachesis](https://github.com/shendurelab/LACHESIS)                | 10.1038/nbt.2727                | 2017        |
|                    |               | [instaGRAAL](https://github.com/koszullab/instaGRAAL)              | 10.1186/s13059-020-02041-z      | 2022        |
|                    |               | [pin_hic](https://github.com/dfguan/pin_hic)                       | 10.1186/s12859-021-04453-5      | 2021        |
|                    |               | [SALSA2](https://github.com/marbl/SALSA)                           | 10.1371/journal.pcbi.1007273    | 2021        |
|                    |               | [scaffHiC](https://github.com/wtsi-hpag/scaffHiC)                  |                                 | 2020        |
|                    |               | [YaHS](https://github.com/c-zhou/yahs)                             |                                 | 2022        |
