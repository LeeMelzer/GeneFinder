# GeneFinder
GeneFinder is a tool used to identify the gene and species of an unknown gene sequence by performing Smith-Waterman alignments of the unknown sequence with known sequences stored in a local database. The input sequence (see formatting below) will be aligned with every sequence in the database and the highest alignment score achieved will be returned, along with the corresponding species and gene. 
Note that a high alignment score does not necessarily prove a relationship. Before use, users will need to provide a single test sequence in a text file named "input.txt" and comparator sequences in a text file named "dbSequences.txt". These two files need to be stored in the same directory as GeneFinder.
Upon launch, the user will be met with a top menu pictured below:

![bandicam 2024-04-25 16-14-42-631](https://github.com/LeeMelzer/GeneFinder/assets/114274820/f02dcb61-8ab7-401d-a36f-ef3f7e1fa3f0)

Users may create a new database, add new sequences to the database (using the same format in "dbSequences.txt", delete the database, or test a sequence. Each command will have an output with feedback. 

Alignment scores will be displayed as follows:

![bandicam 2024-04-25 16-14-59-785](https://github.com/LeeMelzer/GeneFinder/assets/114274820/5fb8ee11-f94f-495f-8f5a-3d2781681536)

# File Formatting
- "input.txt" will simply be a text file with a genetic sequence on a single or multiple lines, depending on length. If the sequence is on multiple lines, the entire sequence will be recorded and used for alignment.
- "dbSequences.txt" may be one or multiple sequences in FASTA or multi-FASTA format, respectively. As the database will only hold species, specific gene, and the sequence, the first line should have two identifiers:
    1) species (or desired name) and
    2) gene separated by a single pipe "|"
- Example: >Streptococcus pyogenes|heme-binding protein Shr

Example files "input.txt" and "dbSequences.txt" have been provided in the repository for reference. Note that two these files will need to be deleted before use.

# Future Updates
This is version 1.0. The next version will have a simple gui for ease of use with expanded functionality.  
