#!/usr/bin/env python
# encoding: utf-8
"""
Created on  2017/09/06 14:48

@author: Lin 

Function:

"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community
import community


df = pd.read_csv('case118.csv')
#df = pd.read_csv('case1354pegase.csv')
G = nx.Graph()
for indx,(s,t) in df[['fbus','tbus']].iterrows():
    G.add_edge(s,t)
degree = G.degree()
#btw = nx.betweenness_centrality(G)
#core = nx.core_number(G)
#df1 = pd.DataFrame(pd.Series(core), columns=['core'])
#df1['degree'] = pd.Series(degree)
#df1['betweenness'] = pd.Series(btw)
#df1.to_csv('1354node_attr.csv', index=True)
#df1.plot.scatter(x='core',y='degree',color='b')
#df1.plot.scatter(x='core',y='betweenness',color='r')
#df1.plot.scatter(x='degree',y='betweenness',s=df1['core']*100, c='core',alpha=0.5)
partition = community.best_partition(G)
modul = community.modularity(partition, G)
f = open('118community.txt','w')
for item in partition:
    f.write(str(item)+'\t'+str(partition[item])+'\n')
#partition = nx.k_clique_communities(G,4)
#or item in partition:
#    print(item,'\n')
#plt.show()
f.close()
print(modul)

