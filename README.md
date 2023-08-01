
# Genome assembly tools

List of genome assembly tools based on the one presented in the review: "A deep dive into genome assemblies of non-vertebrate animals." Guiglielmoni N, Rivera-Vicéns R, Koszul R, Flot J-F. Peer Community Journal, 2022. [doi:10.24072/pcjournal.128](https://peercommunityjournal.org/articles/10.24072/pcjournal.128/)

## Contributing

Adding a software can be done by adding a line in the corresponding CSV file:
* [data/assemblers.csv](data/assemblers.csv) for genome assemblers.
* [data/processors.csv](data/processors.csv) for assembly pre- or post-processing tools.

Modifications to this readme should be done in the template file of the corresponding section (see [templates](templates)).
Every month, a Github action automatically updates the README using the data and templates, fetching the latest commit date for each software.

## Table of contents
* [Genome assemblers](#Genome-assemblers)
  * [Sanger reads](#Sanger-reads)
  * [High-accuracy short reads](#High-accuracy-short-reads)
  * [Low-accuracy long reads](#Low-accuracy-long-reads)
  * [High-accuracy long reads](#High-accuracy-long-reads)
* [Assembly pre and post-processing](#Assembly-pre-and-post-processing)
  * [Long-read error correction](#Long-read-error-correction)
  * [Polishing](#Polishing)
  * [Haplotig purging](#Haplotig-purging)
  * [Scaffolding](#Scaffolding)
  * [Gap filling](#Gap-filling)


## Genome assemblers

### Sanger reads
 
| Assembler | Publication | Last update |
|:----------|:------------|:------------|
| [ARACHNE]() | 10.1101/gr.208902 |  |
| [Atlas](https://www.hgsc.bcm.edu/software/atlas-2) | 10.1101/gr.2264004 | 2013 |
| [CAP3](https://faculty.sites.iastate.edu/xqhuang/cap3-assembly-program) | 10.1101/gr.9.9.868 |  |
| [Celera]() | 10.1093/bioinformatics/btn074 |  |
| [Euler]() | 10.1073/pnas.171285098 |  |
| [JAZZ]() | 10.1126/science.1072104 |  |
| [Minimus]() | 10.1186/1471-2105-8-64 |  |
| [phrap]() | 10.1101/gr.8.3.186 |  |
| [Phusion]() | 10.1101/gr.731003 |  |
| [TIGR]() | 10.1089/gst.1995.1.9 |  |


### High-accuracy short reads

| Assembler | Publication | Last update |
|:----------|:------------|:------------|
| [ABySS](https://github.com/bcgsc/abyss) | 10.1101/gr.214346.116 | 2023-5 |
| [ALLPATHS](https://software.broadinstitute.org/allpaths-lg/blog/?page_id=12) | 10.1101/gr.7337908 | 2008 |
| [BASE](https://github.com/dhlbh/BASE) | 10.1186/s12864-016-2829-5 | 2016-1 |
| [CABOG](http://wgs-assembler.sourceforge.net) | 10.1093/bioinformatics/btn548 | 2008 |
| [Edena](http://www.genomic.ch/edena.php) | 10.1101/gr.072033.107 | 2013 |
| [EPGA](https://github.com/bioinfomaticsCSU/EPGA) | 10.1093/bioinformatics/btu762 | 2017-4 |
| [Euler-SR](http://web.archive.org/web/20110720080755/http://euler-assembler.ucsd.edu/euler-sr.1.1.2.tgz) | 10.1101/gr.7088808 | 2011 |
| [Gossamer]() | 10.1093/bioinformatics/bts297 | 2012 |
| [IDBA](https://github.com/loneknightpy/idba) | 10.1007/978-3-642-12683-3_28 | 2016-12 |
| [ISEA]() | 10.1109/TCBB.2016.2550433 |  |
| [JR-Assembler]() | 10.1073/pnas.1314090110 |  |
| [LightAssembler]() | 10.1093/bioinformatics/btw470 |  |
| [Meraculous]() | 10.1371/journal.pone.0023501 |  |
| [Minia](https://github.com/GATB/minia) | 10.1186/1748-7188-8-22 | 2022-2 |
| [Mira]() | 10.1.1.23.7465 |  |
| [Newbler]() |  |  |
| [PCAP](https://faculty.sites.iastate.edu/xqhuang/pcap-assembly-program) | 10.1101/gr.1390403 |  |
| [PE-Assembler]() | 10.1093/bioinformatics/btq626 |  |
| [PERGA]() | 10.1371/journal.pone.0114253 |  |
| [Platanus]() | 10.1101/gr.170720.113 |  |
| [QSRA]() | 10.1186/1471-2105-10-69 |  |
| [Ray]() | 10.1089/cmb.2009.0238 |  |
| [Readjoiner]() | 10.1186/1471-2105-13-82 |  |
| [SGA]() | 10.1101/gr.126953.111 |  |
| [SHARCGS]() | 10.1101/gr.6435207 |  |
| [SOAPdenovo]() | 10.1101/gr.097261.109 |  |
| [SOAPdenovo2]() | 10.1186/2047-217X-1-18 |  |
| [SPAdes]() | 10.1089/cmb.2012.0021 |  |
| [SparseAssembler]() | 10.1186/1471-2105-13-S6-S1 |  |
| [SSAKE]() | 10.1093/bioinformatics/btl629 |  |
| [SUTTA]() | 10.1093/bioinformatics/btq646 |  |
| [VCAKE]() | 10.1093/bioinformatics/btm451 |  |
| [Velvet]() | 10.1002/0471250953.bi1105s31 |  |
| [Taipan]() | 10.1093/bioinformatics/btp374 |  |

### Low-accuracy long reads

| Assembler | Publication | Last update |
|:----------|:------------|:------------|
| [Canu](https://github.com/marbl/canu) | 10.1101/gr.215087.116 | 2023-7 |
| [FALCON](https://github.com/PacificBiosciences/FALCON) | 10.1038/nmeth.4035 | 2018-4 |
| [Flye](https://github.com/fenderglass/Flye) | 10.1038/s41587-019-0072-8 | 2023-5 |
| [GoldRush](https://github.com/bcgsc/goldrush) | 10.1101/2022.10.25.513734 | 2023-6 |
| [HINGE](https://github.com/HingeAssembler/HINGE) | 10.1101/gr.216465.116 | 2019-1 |
| [MECAT](https://github.com/xiaochuanle/MECAT) | 10.1038/nmeth.4432 | 2019-2 |
| [MECAT2](https://github.com/xiaochuanle/MECAT2) | 10.1038/nmeth.4432 | 2020-4 |
| [miniasm](https://github.com/lh3/miniasm) | 10.1038/nmeth.4432 | 2019-10 |
| [NECAT](https://github.com/xiaochuanle/NECAT) | 10.1038/s41467-020-20236-7 | 2021-3 |
| [NextDenovo](https://github.com/Nextomics/NextDenovo) |  | 2023-7 |
| [Ra](https://github.com/lbcb-sci/ra) | 10.1109/ISPA.2019.8868909 | 2018-12 |
| [Raven](https://github.com/lbcb-sci/raven) | 10.1038/s43588-021-00073-4 | 2023-6 |
| [SMARTdenovo](https://github.com/ruanjue/smartdenovo) | 10.20944/preprints202009.0207.v1 | 2021-2 |
| [wtdbg](https://github.com/ruanjue/wtdbg) |  | 2017-3 |
| [wtdbg2](https://github.com/ruanjue/wtdbg2) | 10.1038/s41592-019-0669-3 | 2020-12 |

### High-accuracy long reads 

| Assembler | Publication | Last update |
|:----------|:------------|:------------|
| [Flye](https://github.com/fenderglass/Flye) | 10.1038/s41587-019-0072-8 | 2023-5 |
| [HiCanu](https://github.com/marbl/canu) | 10.1101/gr.215087.116 | 2023-7 |
| [hifiasm](https://github.com/chhylp123/hifiasm) | 10.1038/s41592-020-01056-5 | 2023-7 |
| [IPA](https://github.com/PacificBiosciences/pbipa) |  | 2022-3 |
| [LJA](https://github.com/AntonBankevich/LJA) | 10.1101/2020.12.10.420448 | 2022-1 |
| [mdBG](https://github.com/ekimb/rust-mdbg/) | 10.1016/j.cels.2021.08.009 | 2023-1 |
| [MBG](https://github.com/maickrau/MBG) | 10.1093/bioinformatics/btab004 | 2023-5 |
| [NextDenovo](https://github.com/Nextomics/NextDenovo) |  | 2023-7 |
| [Peregrine](https://github.com/cschin/Peregrine) |  | 2022-2 |
| [Raven](https://github.com/lbcb-sci/raven) | 10.1038/s43588-021-00073-4 | 2023-6 |
| [verkko](https://github.com/marbl/verkko) | 10.1101/2022.06.24.497523 | 2023-7 |
| [wtdbg2](https://github.com/ruanjue/wtdbg2) | 10.1038/s41592-019-0669-3 | 2020-12 |
## Assembly pre and post-processing

### Long-read error correction
 
| Reads | Tool  | Publication | Last update |
|:------|:------|:------------| ----------- |
| __Long reads__ | [Canu](https://github.com/marbl/canu) | 10.1101/gr.215087.116 | 2023-7 |
|  | [CONSENT](https://github.com/morispi/CONSENT) | 10.1038/s41598-020-80757-5 | 2021-9 |
|  | [Daccord](https://github.com/gt1/daccord) | 10.1101/106252 | 2018-9 |
|  | [FLAS](https://github.com/baoe/FLAS) | 10.1093/bioinformatics/btz206 | 2019-2 |
|  | [HALC](https://github.com/lanl001/halc) | 10.1186/s12859-017-1610-3 | 2018-5 |
|  | [MECAT](https://github.com/xiaochuanle/MECAT) | 10.1038/nmeth.4432 | 2019-2 |
|  | [MECAT2](https://github.com/xiaochuanle/MECAT2) | 10.1038/nmeth.4432 | 2020-4 |
|  | [NECAT](https://github.com/xiaochuanle/NECAT) | 10.1038/s41467-020-20236-7 | 2021-3 |
|  | [NextDenovo](https://github.com/Nextomics/NextDenovo) |  | 2023-7 |
| __Short reads__ | [CoLoRMap](https://github.com/cchauve/CoLoRMap) | 10.1093/bioinformatics/btw463 | 2018-3 |
|  | [Hercules](https://github.com/BilkentCompGen/Hercules) | 10.1093/nar/gky724 | 2018-8 |
|  | [HG-CoLoR](https://github.com/morispi/HG-CoLoR) | 10.1093/bioinformatics/bty521 | 2021-1 |
|  | [Jabba](https://github.com/biointec/jabba) | 10.1186/s13015-016-0075-7 | 2018-6 |
|  | [LoRDEC](https://gite.lirmm.fr/lordec/lordec-releases/-/wikis/home) |  10.1093/bioinformatics/btu538 | 2020 |
|  | [LoRMA](https://gite.lirmm.fr/lorma/lorma-releases/-/wikis/home) | 10.1093/bioinformatics/btw321 | 2019 |
|  | [NaS](https://github.com/institut-de-genomique/NaS) | 10.1186/s12864-015-1519-z | 2017-3 |
|  | [proovread](https://github.com/BioInf-Wuerzburg/proovread) | 10.1093/bioinformatics/btu392 | 2019-5 |
|  | [Ratatosk](https://github.com/DecodeGenetics/Ratatosk) | 10.1186/s13059-020-02244-4 | 2023-7 |

### Polishing

| Reads | Tool  | Publication | Last update |
|:------|:------|:------------| ----------- |
| __Long reads__ | [Arrow]() |  | 2014 |
|  | [CONSENT](https://github.com/morispi/CONSENT) | 10.1038/s41598-020-80757-5 | 2021-9 |
|  | [GoldRush](https://github.com/bcgsc/goldrush) | 10.1101/2022.10.25.513734 | 2023-6 |
|  | [Quiver]() |  | 2014 |
| __Long reads + short reads__ | [ Hapo-G](https://github.com/institut-de-genomique/HAPO-G) | 10.1093/nargab/lqab034 | 2023-1 |
|  | [HyPo](https://github.com/kensung-lab/hypo) | 10.1101/2019.12.19.882506 | 2020-2 |
|  | [Racon](https://github.com/isovic/racon) | 10.1101/gr.214270.116 | 2020-8 |
| __Short reads__ | [ntEdit](https://github.com/bcgsc/ntEdit) | 10.1093/bioinformatics/btz400 | 2023-6 |
|  | [Pilon](https://github.com/broadinstitute/pilon) | 10.1371/journal.pone.0112963 | 2021-1 |
|  | [POLCA](https://github.com/alekseyzimin/masurca) | 10.1371/journal.pcbi.1007981 | 2023-3 |
|  | [Apollo](https://github.com/CMU-SAFARI/Apollo) | 10.1093/bioinformatics/btaa179 | 2020-5 |

### Haplotig purging

| Reads | Tool  | Publication | Last update |
|:------|:------|:------------| ----------- |
| __Long reads__ | [HaploMerger2](https://github.com/mapleforest/HaploMerger2) | 10.1093/bioinformatics/btx220 | 2016-12 |
|  | [purge_dups](https://github.com/dfguan/purge_dups) | 10.1093/bioinformatics/btaa025 | 2022-6 |
|  | [Purge Haplotigs](https://bitbucket.org/mroachawri/purge_haplotigs) |  10.1186/s12859-018-2485-7 | 2023-6 |
| __Long reads + short reads__ | [Redundans](https://github.com/lpryszcz/redundans) | 10.1093/nar/gkw294 | 2023-7 |

### Scaffolding

| Reads | Tool  | Publication | Last update |
|:------|:------|:------------| ----------- |
| __Genetic maps__ | [ ALLMAPS](https://github.com/tanghaibao/jcvi/wiki/ALLMAPS) | 10.1186/s13059-014-0573-1 | 2022 |
| __Hi-C__ | [3D-DNA](https://github.com/aidenlab/3d-dna) | 10.1126/science.aal3327 | 2019-8 |
|  | [dnaTri](https://github.com/NoamKaplan/dna-triangulation) | 10.1038/nbt.2768 | 2015-7 |
|  | [EndHiC](https://github.com/fanagislab/EndHiC) | 10.48550/arXiv.2111.15411 | 2022-10 |
|  | [GRAAL](https://github.com/koszullab/GRAAL) | 10.1038/ncomms6695 | 2020-1 |
|  | [HiCAssembler](https://github.com/maxplanck-ie/HiCAssembler) | 10.1101/gad.328971.119 | 2019-11 |
|  | [msscaf](https://github.com/mzytnicki/msscaf) |  | 2022-10 |
|  | [instaGRAAL](https://github.com/koszullab/instaGRAAL) | 10.1186/s13059-020-02041-z | 2023-1 |
|  | [Lachesis](https://github.com/shendurelab/LACHESIS) | 10.1038/nbt.2727 | 2017-12 |
|  | [pin_hic](https://github.com/dfguan/pin_hic) | 10.1186/s12859-021-04453-5 | 2021-12 |
|  | [SALSA2](https://github.com/marbl/SALSA) | 10.1371/journal.pcbi.1007273 | 2022-4 |
|  | [scaffHiC](https://github.com/wtsi-hpag/scaffHiC) |  | 2022-12 |
|  | [YaHS](https://github.com/c-zhou/yahs) |  | 2023-6 |
| __Linked reads__ | [ ARBitR](https://github.com/markhilt/ARBitR) | 10.1093/bioinformatics/btaa975 | 2020-10 |
|  | [Architect](https://github.com/kuleshov/architect) | 10.1093/bioinformatics/btw267 | 2016-10 |
|  | [ARCS](https://github.com/bcgsc/ARCS/) | 10.1093/bioinformatics/btx675 | 2023-4 |
|  | [ARKS](https://github.com/bcgsc/arks) | 10.1186/s12859-018-2243-x | 2019-12 |
|  | [fragScaff](https://github.com/adeylab/fragScaff) | 10.1101/gr.178319.114 | 2018-11 |
|  | [scaff10X](https://github.com/wtsi-hpag/Scaff10X) |  | 2022-1 |
|  | [SpLitteR](https://github.com/ablab/spades/releases/tag/splitter-paper) |  | 2022-12 |
|  | [msscaf](https://github.com/mzytnicki/msscaf) |  | 2022-10 |
| __Long reads__ | [DENTIST](https://github.com/a-ludi/dentist) | 10.1093/gigascience/giab100 | 2022-10 |
|  | [FinisherSC](https://github.com/kakitone/finishingTool) | 10.1093/bioinformatics/btv280 | 2016-11 |
|  | [gapless]() | 10.1101/2022.03.08.483466 |  |
|  | [GoldRush](https://github.com/bcgsc/goldrush) | 10.1101/2022.10.25.513734 | 2023-6 |
|  | [LINKS](https://github.com/bcgsc/LINKS) | 10.1186/s13742-015-0076-3 | 2023-7 |
|  | [LRScaf](https://github.com/shingocat/lrscaf) | 10.1186/s12864-019-6337-2 | 2021-11 |
|  | [npScarf](https://github.com/mdcao/npScarf) | 10.1038/ncomms14515 | 2019-10 |
|  | [PBJelly](https://sourceforge.net/projects/pb-jelly/) | 10.1371/journal.pone.0047768 | 2017 |
|  | [RAILS](https://github.com/bcgsc/RAILS) | 10.21105/joss.00116 | 2023-2 |
|  | [SLR](https://github.com/luojunwei/SLR) | 10.1186/s12859-019-3114-9 | 2020-8 |
|  | [msscaf](https://github.com/mzytnicki/msscaf) |  | 2022-10 |
|  | [SMIS](https://github.com/wtsi-hpag/smis) |  | 2018-2 |
|  | [SMSC](https://github.com/UTbioinf/SMSC) | 10.1186/s12864-017-4271-8 | 2019-9 |
|  | [SSPACE-LongRead]() | 10.1186/1471-2105-15-211 | 2014 |
| __Mate pairs__ | [BATISCAF]() | 10.1101/330472 |  |
|  | [BESST]() | 10.1186/1471-2105-15-281 |  |
|  | [BOSS]() | 10.1093/bioinformatics/btw597 |  |
|  | [GRASS]() | 10.1093/bioinformatics/bts175 |  |
|  | [MIP]() | 10.1093/bioinformatics/btr562 |  |
|  | [Opera]() | 10.1089/cmb.2011.0170 |  |
|  | [ScaffMatch]() | 10.1093/bioinformatics/btv211 |  |
|  | [ScaffoldScaffolder]() | 10.1093/bioinformatics/btv548 |  |
|  | [SCARPA]() | 10.1093/bioinformatics/bts716 |  |
|  | [SCOP]() | 10.1093/bioinformatics/bty773 |  |
|  | [SLIQ]() | 10.1089/cmb.2011.0263 |  |
|  | [SOPRA]() | 10.1186/1471-2105-11-345 |  |
|  | [SSPACE]() | 10.1093/bioinformatics/btq683 |  |
|  | [WiseScaffolder]() | 10.1186/s12859-015-0705-y |  |
| __Optical maps__ | [ AGORA](https://static-content.springer.com/esm/art%3A10.1186%2F1471-2105-13-189/MediaObjects/12859_2012_5306_MOESM3_ESM.zip) |  10.1186/1471-2105-13-189 | 2012 |
|  | [BiSCoT](https://github.com/institut-de-genomique/biscot) | 10.7717/peerj.10150 | 2020-11 |
|  | [OMGS](https://github.com/ucrbioinfo/OMGS) | 10.1089/cmb.2019.0310 | 2018-11 |
|  | [SewingMachine](https://github.com/i5K-KINBRE-script-share/Irys-scaffolding/blob/master/KSU_bioinfo_lab/stitch/sewing_machine_LAB.md) | 10.1186/s12864-015-1911-8 | 2015 |
|  | [SOMA](ftp://ftp.cbcb.umd.edu/pub/software/soma) | 10.1093/bioinformatics/btn102 | 2008 |
| __Short reads__ | [Bambus]() | 10.1101/gr.1536204 |  |

### Gap filling

| Reads | Tool  | Publication | Last update |
|:------|:------|:------------| ----------- |
| __Long reads__ | [Cobbler](https://github.com/bcgsc/RAILS) | 10.21105/joss.00116 | 2023-2 |
|  | [DENTIST](https://github.com/a-ludi/dentist) | 10.1093/gigascience/giab100 | 2022-10 |
|  | [FGAP](https://github.com/pirovc/fgap) | 10.1186/1756-0500-7-371 | 2017-12 |
|  | [FinisherSC](https://github.com/kakitone/finishingTool) | 10.1093/bioinformatics/btv280 | 2016-11 |
|  | [gapless]() | 10.1101/2022.03.08.483466 |  |
|  | [GMcloser](https://sourceforge.net/projects/gmcloser/) | 10.1093/bioinformatics/btv465 | 2018 |
|  | [LR_Gapcloser](https://github.com/CAFS-bioinformatics/LR_Gapcloser) |  10.1093/gigascience/giy157 | 2018-9 |
|  | [PBJelly](https://sourceforge.net/projects/pb-jelly/) | 10.1371/journal.pone.0047768 | 2017 |
|  | [PGcloser]() | 10.1177/1176934320913859 | 2020 |
|  | [TGS-GapCloser](https://github.com/BGI-Qingdao/TGS-GapCloser) | 10.1093/gigascience/giaa094 | 2023-4 |
|  | [YAGCloser](https://github.com/merlyescalona/yagcloser) |  | 2023-2 |
| __Short reads__ | [GapFiller]() | 10.1186/gb-2012-13-6-r56 |  |
|  | [GAPPadder]() | 10.1186/s12864-019-5703-4 |  |
|  | [Sealer]() | 10.1186/s12859-015-0663-4 |  |
