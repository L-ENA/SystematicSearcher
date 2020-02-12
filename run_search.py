# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:50:58 2019

@author: Lena Schmidt, lena.schmidt@bristol.ac.uk

a conda spec file to create an environment with all necessary libraries (win - 64) is provided in the Git repo. 

NB: if you want to search the dblp, please download the database and its dtd file and unzip it in your working directory: https://dblp.uni-trier.de/faq/How+can+I+download+the+whole+dblp+dataset

If you want to search the arxiv, a dump will be automatically created. Dates from when to scrape are defined in the optional parameter of the read_arxiv(begin_scraping = '2020-02-10', arxiv_repo ="cs") method: here scraping starts on thr 10th of Feb 2020, and we scrape the cs arxiv

With many thanks to Mahdi Sadjadi (sadjadi.seyedmahdi[AT]gmail[DOT]com) for the arxiv scraping code: https://github.com/Mahdisadjadi/arxivscraper
"""

from SystematicSearcher import *

database = "arxiv"

if database=='dblp':  
    print("Dealing with DBLP data")
    read_dblp()#read the dblp export dump###NB: if you want to search the dblp, please download the database and its dtd file and unzip it in your working directory: https://dblp.uni-trier.de/faq/How+can+I+download+the+whole+dblp+dataset
    my_df = load_pickled_db('dblp.pickle')#25 45 secs
    print('Selected database contains the following (searchable) fields: {}'.format(my_df.columns))
    search_df(my_df, field='Title')#dblp has only titles unfortunately#search the specified fild with the pre-defined systematic search and save results to spreadsheet
    
elif database == "arxiv":
    print("Dealing with arxiv data")
    read_arxiv()#reading the local arxiv dump. creates a dump if none is found. Pass optional parameter to define date from which to scrape and refer to method for more info  
    my_df = load_pickled_db('arxiv.pickle')
    print('Selected database contains the following (searchable) fields: {}'.format(my_df.columns))
    search_df(my_df, field='TiAbs')
else:
    print("No database specified")    