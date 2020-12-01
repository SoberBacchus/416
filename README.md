
Final Computer Science Project for Bioinformatics course at Rice University.

Goal: Read map billions of reads from Illumina to various positions in the coronavirus genome for 
research applications. Metrics were as follows: Bronze 1000 reads/min. Platinum 1000000 reads/min.

Working directory contains final code for the project. Command line "python maestro.py".

Background:

Read mapping is a critical step in being able to analyze genomes successfully. Besides being a 
useful tool in reconstructing genomes and potentially checking mutations and validity of reads,
read maps can also be used to perform ancestral genomic analyses. 

Read mappers need to be fast and accurate. Current gold-standard algorithms are able to accurately
read on the orders of tens of thousands of reads per minute. In here, we are able to meet the same
precision and accuracy metrics and surpasse them, with a final speed of 1,625 reads/minute. 
