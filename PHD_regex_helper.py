# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:49:37 2020

@author: Lena Schmidt, lena.schmidt@bristol.ac.uk

This file contains regular expressions which define a systematic search. Lines in each cluster will be connected via "OR" searches, while clusters themselves are connected via "AND". Performance is best if your first cluster is the cluster that is likely to produce the least hits. the "NOT" cluster defines terms that must not occur in any searched entity, similar to the NOT search in ovid. 
"""
cluster_NOT_titles = []
cluster_NOT_abstracts = []

cluster_1 = [
        r'(\bpublic.health\b)|(trials?[ -]?regist)|(regist.+of clinical trial)|(clinicaltrials\.gov)|(isrctn)|(irct)|(chictr)|(pre[- ]?print)|(medrxiv)|(biorxiv)|(arxiv)|(social[ -]?media)|(twitter)|(instagram)|(tik[ -]tok)|(facebook)|(linkedin)|(snapchat)|(tumblr)|(pinterest)|(reddit)|(research[ -]?gate)|(gr[ea]y[ -]?literature)|(dissertation)|(for(um|a))|(website)|(platform)|(lifestyle)|(resource)|(news)|(patent)|(clinical guideline)|(health[ -]?technology[ -]?assessment)|(\bhta\b)|(medical guideline)'
        ]

cluster_2 = [r'(automat(ic|ed|ing) extraction)|(data[- ]?extract)|(text[- ]?(analys|min))|(text[- ]?classif)|(data[- ]?(analys|min))|(literature[- ]?min)|(automat(ed|ing|ion).{1,25}(pico|text|literature|natural language|nlp|publication|website|search|retrieve))|((pico|text|literature|natural language|nlp|publication|website|search|retrieve).{1,25}automat(ed|ing|ion))|((text|record|reference|literature|data|article|paper|post|tweet).{1,25}retrieve)|((text|record|reference|literature|data|article|paper|post|tweet).{1,25}search)|((text|record|reference|literature|data|article|paper|post|tweet).{1,25}download)|(search.{1,25}(text|record|reference|literature|data|article|paper|post|tweet))|(retrieve.{1,25}(text|record|reference|literature|data|article|paper|post|tweet))|(download.{1,25}(text|record|reference|literature|data|article|paper|post|tweet))']

cluster_3 = [r'(inference[- ]?algorithm)|(statistic(al)?[- ]?relational[- ]?learning)|(klog)|(supervised classif)|(information[ -]?retrieval)|(word embedding)|(word2vec)|(character embedding)|((sci|al|bio|distil|span|ro)berta?)|(\bbert\b)|(specter)|(xlnet)|(transformer)|(rule[- ?]base)|(recurrent[- ?]neural[- ?]network)|(rnn|cnn|lstm|mlp|rfbn|max.ent|\blda\b|\bcrf|svm)|(random forest)|(radial basis function)|(n.ive[ -]?bayes)|(layer perceptron)|(perceptron algorithm)|(maximum entropy classif)|(long[ -]?short[ -]?term[ -]?memory)|(latent dirichlet)|(topic[ -]?model)|(decision[ -]?tree)|(conditional[ -]?random[ -]?field)|(convolutional[ -]?neural[ -]?network)|(Bidirectional Encoder Representation)|(term[ -]?recognition)|(regular.expression)|(regex)|(support[ -]?vector[ -]?machine)|(ontolog(y|ies))|(question answering)|(reading comprehension)|(predictive modelling)|(nlp)|(natural language processing)|(artificial intelligence)|(neural[ -]?network)|((active|deep|machine|supervised|transfer)[ -]?learning)|((learn|train).{1,20}algorithm)']




#print(cluster_1)
