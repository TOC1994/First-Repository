# This repository will serve as a virtual lab book for the BS32012 Bioinformatics Practical Project. 

## Aims of the practical. 
1) To develop practical skills required to effectively implement bioinformatics workflows
and data analysis, including building and importing data into a relational database, and
using the python programming language to query the database and elucidate relevant 
biological information. 

2) To develop understanding of how to work collaboratively on data analysis, through the
online repository GitHub. 

3)To understand provenance and sustainability in bioinformatics analysis.

## Files and Folders

### Images 
Contains an image used during an exercise to set up version control.

### First-Repository.md
A file added by user chrrpat while experimenting with version control. 

### GDS5047_full.soft
The full raw data file that was the subject of this practical, containing information on the differences in gene exppression between the midbrain cells of deceased cocaine abusers and control subjects.

### Learing_python.py
Code I've generated while trying to familiarise myself wiith the python programming language.

### README.md
The file you are reading at present, it details the contents of 'First-Repository'.

### age.py
A simple if/else program that when run will ask you for your age, and come back with a 
cheeky response. Created while I was learning how to code with python. 

### data.md
A file created while experimenting with version control. 

### expression.txt
A text file containing expression information extracted from the 'GDS5047_full.soft' file. 
Contains information under the fields sample ID, ID reference for a probe used in the
microarrray experiment, and recorded expression values for the different genes. 

### genes.txt
A text file containing information on the genes that were studied in the 'GDS5047_full.soft'
file. Contains the fields gene id, gene name and gene description. 

#### myparser.py
The finall edit of a parser created with the python programming language, designed to extract information
on the genes, probes, and expression values detailed in the 'GDS5047_full.soft' file and 
write them out to the files 'genes.txt', 'probes.txt', and 'expression.txt'. 

### mysql tables
The final edit of the code used to create the tables in mysql which were designed to 
hold the data extracted from the 'GDS5047_full.soft' file and held in the files 'genes.txt', 'probes.txt', and 'expression.txt'. Also contains code experimented with for editing tables after they have
been created.

### outline.md
A file created  alongside data.md while trying to master version control with git. 

### probes.txt
A text file detailing information of the probes used in the experiment, extracted from
'GDS5047_full.soft' using 'myparser.py'. Contains information under the fields of an 
ID reference for each probe, and a unique identifier for the gene that each perobe
corresponds to. 

### samples.txt
A text file containing additional information on the samples used in the microarray
experiment detailed in 'GDS5047_full.soft'. Contains information under the fields of 
sample ID (a unique identifier for each sample), whether the subject was a member of the
control group who died from natural causes, or test group who died from complications
related to cocaine abuse. The file was created directly from the 'GDS5047_full.soft' file 
using the find and replace function to replace all lines not beginning with '#' with nothing,
and to remove the unneccessary information in the remaining lines and replace it with tabs.

### thisisanewfile.md
A file added by user chrrpat during his experimentation with version control.

