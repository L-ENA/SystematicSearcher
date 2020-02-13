# SystematicSearcher

What does it do?

This repository contains a Python package to help conducting systematic literature searches on databases that do not provide advanced search interfaces. An implementation for the "DBLP" and "arXiv" databases is already included. It can download and parse data from these databases or use existing database dumps. After running a systematic search, it exports results to spreadsheets (more export options to be implemented).

How does this work?

The systematic search is implemented via clusters of regular expressions which mimic boolean searches on ovid/medline. Each regex corresponds with one part of a search cluster, and a search cluster generally corresponds with a broader concept.See "regex_helper.py" for examples. Regexes from a cluster are automatically chained up to form "OR" type of searches. Clusters are then applied as "AND" type of searches to records from a database. It is also possible to filter by publication date and to use a "NOT" component to exclude records by keyword.

The final search results are exported to the working directory as "results.csv", along with "excluded_dates.csv" - records excluded because they were not published in the right timeframe, and "excluded_via_NOT-search.csv" - records excluded becasue they contained terms for exclusion, similar to ovids "NOT" search function.

Quick start:
Clone this repo, or simply download all its files into one local directory.

Using 'spec-file.txt' or 'environment.yml' one can recreate a conda environment with all necessary packages to run this code (for example in the Spyder editor). This spec-file is for windows, but all necessary packages can also be installed manually on linux systems. See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.htm

An example script to scrape the computer science arXiv and to implement the systematic search defined in the file "regex_helper.py" from this repository is given below:

```python
from SystematicSearcher import *

database = "arxiv"#define which database to search

if database=='dblp':  
    print("Dealing with DBLP data")
    read_dblp()#read the dblp export dump###NB: if you want to search the dblp, please download the database and its dtd file and unzip it in your working directory: https://dblp.uni-trier.de/faq/How+can+I+download+the+whole+dblp+dataset
    my_df = load_pickled_db('dblp.pickle')#25 45 secs
    print('Selected database contains the following (searchable) fields: {}'.format(my_df.columns))
    search_df(my_df, field='Title')#dblp has only titles unfortunately#search the specified fild with the pre-defined systematic search and save results to spreadsheet
    
elif database == "arxiv":
    print("Dealing with arxiv data")
    read_arxiv(begin_scraping = '2020-02-02')#reading the local arxiv data. if there is no data, it scrapes it from arxiv api  
    my_df = load_pickled_db('arxiv.pickle')
    print('Selected database contains the following (searchable) fields: {}'.format(my_df.columns))
    search_df(my_df, field='TiAbs')
else:
    print("No database specified")    
    
```    


