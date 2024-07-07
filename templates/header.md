
# Genome assembly tools

If you appreciate this work, please cite: "A deep dive into genome assemblies of non-vertebrate animals." Guiglielmoni N, Rivera-Vicéns R, Koszul R, Flot J-F. Peer Community Journal, 2022. [doi:10.24072/pcjournal.128](https://peercommunityjournal.org/articles/10.24072/pcjournal.128/)

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

