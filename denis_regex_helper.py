# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:49:37 2020

@author: Lena Schmidt, lena.schmidt@bristol.ac.uk

This file contains regular expressions which define a systematic search. Lines in each cluster will be connected via "OR" searches, while clusters themselves are connected via "AND". Performance is best if your first cluster is the cluster that is likely to produce the least hits. the "NOT" cluster defines terms that must not occur in any searched entity, similar to the NOT search in ovid. 
"""
cluster_NOT_titles = []
cluster_NOT_abstracts = []

cluster_1 = [
        r'(\bbias(es)?\b)|(\bepidemiologic Bias(es?)?\b)|(\bstatistical bias(es)?\b)|(\becological bias(es)?\b)|(\becological fallac(y|ies)\b)|(\bOutcome Measurement Errors?\b)|(\btruncation bias\b)|(\bscientific bias\b)|(\bscientific bias?\b)|(\bexperimental bias?\b)|(\baggregation bias\b)|(\bsystematic bias\b)|(\brobis\b)|(\bamstar 2\b)|(\bSIGN checklist\b)|(\bBallard\b)|(\bMontgomery\b)|(\bRoB\b)|(\bROBINS.I\b)|(\bNewcastle.Ottawa.Scale\b)|(\bnos\b)|((\bQUADAS.2\b)|(\bCASP\b)|(\bJBI\b)|(\bGRADE.CERQual\b)|(\bQUIPS\b)|(\bPROBAST\b))'
        ]

cluster_2 = [
        r'(\bArtificial Intelligence\b)|(\bComputational Intelligence\b)|(\bMachine Intelligence\b)|(\bComputer Reasoning\b)|(\bAI\b)|(\bComputer Vision Systems?\b)|(\bKnowledge Acquisition\b)|(\bKnowledge Representation\b)|(\bMachine.Learning\b)|(\bDeep.Learning\b)|(\bNeural.networks?\b)|(\b(semi.)?automat(ion|ed)\b)'
        ]

#cluster_3 = [r'(inference[- ]?algorithm)|(statistic(al)?[- ]?relational[- ]?learning)|(klog)|(supervised classif)|(information[ -]?retrieval)|(word embedding)|(word2vec)|(character embedding)|((sci|al|bio|distil|span|ro)berta?)|(\bbert\b)|(specter)|(xlnet)|(transformer)|(rule[- ?]base)|(recurrent[- ?]neural[- ?]network)|(rnn|cnn|lstm|mlp|rfbn|max.ent|\blda\b|\bcrf|svm)|(random forest)|(radial basis function)|(n.ive[ -]?bayes)|(layer perceptron)|(perceptron algorithm)|(maximum entropy classif)|(long[ -]?short[ -]?term[ -]?memory)|(latent dirichlet)|(topic[ -]?model)|(decision[ -]?tree)|(conditional[ -]?random[ -]?field)|(convolutional[ -]?neural[ -]?network)|(Bidirectional Encoder Representation)|(term[ -]?recognition)|(regular.expression)|(regex)|(support[ -]?vector[ -]?machine)|(ontolog(y|ies))|(question answering)|(reading comprehension)|(predictive modelling)|(nlp)|(natural language processing)|(artificial intelligence)|(neural[ -]?network)|((active|deep|machine|supervised|transfer)[ -]?learning)|((learn|train).{1,20}algorithm)']




#print(cluster_1)
