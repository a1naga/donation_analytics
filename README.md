# Donation Analytics
This is a donation analytics program that reads the donation data from an input file, calculates the running percentiles for repeated donations for a recipient and outputs the calculated values for each repeat donation from a donor. A donor is identified as donor name, zip code. Percentile calculation is done for each [recipient, zip code, year] combination. The program accepts donation input file, file to read percentile value, output file name.

## Usage

```bash
$ python ./src/data_fetcher.py <itcont.txt> <percentile.txt> <output file path>
```

or if the input files are available in input directory under project root

```bash
$ ./run.sh
```
