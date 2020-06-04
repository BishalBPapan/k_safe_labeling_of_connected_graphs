#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import operator
import random


# In[2]:


k = int(input())                                                                                        #input the value of k
#G=nx.karate_club_graph()                                                                               #to test known dataset
G=nx.Graph()                                                                                            #initialization of graph G
G=nx.read_edgelist("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/2.txt", nodetype = int)   #input graph from a file 
print(nx.is_connected(G))                                                                               #dataset checking
print(nx.is_directed(G))                                                                                #dataset checking
#print(k)


# In[3]:


E=[e for e in G.edges]                                                              #not necessary, only used it to debug
E


# In[4]:


n=nx.number_of_nodes(G)
print(n)
G2=nx.complete_graph(n)                                                           #conversion to complete graph


# In[5]:


E_h=[e for e in G2.edges]                                                         #not necessary, only used to debug


# In[6]:


E_c=[e for e in nx.non_edges(G)]                                                  #edges in complement graph of G
print(len(E_c))
E_c


# In[7]:


#label_init=[v*k+1 for v in G.nodes]
label_init={vertex:vertex*k+1  for vertex in G.nodes}                            #labeling the complete graph using a dictionary
#label_init[33] = 10
print(label_init)
#max_labeled=max(label_init)
max_label=max(label_init.values())                                               #finding the maximum labeled vertex
for vertex, label in label_init.items():                                         #finding the maximum label
    if label == max_label:
        max_labeled=vertex
        break
#max_labeled = max(enumerate(label_init.values()), key=operator.itemgetter(1))[0] 
#max_label = max(enumerate(label_init.values()), key=operator.itemgetter(1))[1]   
print(max_labeled)
print(max_label)


# In[8]:


def violate_constraints(G_now, label_now, k, vertex, label_this):                                       #this function checks if a label violates the constraints of k-safe labeling
    for node in nx.all_neighbors(G_now, vertex):
        if label_this in label_now.values() or (label_now[node] > 0 and ((label_this-label_now[node] < k and label_this-label_now[node] > 0) or (label_now[node]-label_this < k and label_now[node]-label_this >0))):
            return True


# In[9]:


edge_stack = []                                                                   #stack where removed edges are pushed

while not len(E_c)==0:                                                            #first outer loop, label_init is the dictionary of the previous step
    label_p=label_init                                                            #not necessary
    nodes_reversed=[w for w in sorted(label_p, key=label_p.get, reverse=True)]    #sorting the vertices in decreasing order of labels
    for node in nodes_reversed:                                                   #taking any random edge incident to the first maximum labeled vertex
        if not len([e for e in E_c if e[0]==node or e[1]==node])==0:              #which has an incident edge in E_c
            e_incident=random.choice([e for e in E_c if e[0]==node or e[1]==node])
            break
    
    print(e_incident)
    edge_stack.append(e_incident)                                                 #adding the edge to the stack
    #print(len(E_c))
    E_c.remove(e_incident)                                                        #removing the edge from E_c
    print(len(E_c))
    #print(len(E_h))
    print(edge_stack)
    #E_cc

    if G2.has_edge(e_incident[0], e_incident[1]):
        G2.remove_edge(e_incident[0], e_incident[1])                              #removing the edge from G2
    elif G2.has_edge(e_incident[1], e_incident[0]):
        G2.remove_edge(e_incident[1], e_incident[0])
        
    #print(list(nx.non_edges(G2)))
    label_now={vertex:0  for vertex in nodes_reversed}                            #initializing the dictionary of current step with labels 0
    checked={vertex:0 for vertex in nodes_reversed}
    #label_now[e_incident[0]]=1
    #label_now[e_incident[1]]=2
    for e in edge_stack[::-1]:                                                    #inner loop 1, taking edges in the reverse order of input to stack
        #checked[e[0]]=1
        #checked[e[1]]=1
        if checked[e[0]]==0: #and checked[e[1]]==0:
            for label in range(1,max_label+1):                                    #because a vertex can be labeled with at most the max_label of the previous step
                if not violate_constraints(G2, label_now, k, e[0], label):        #if both vertices incident to the edges are unlabeled, then label both with consecutive integers
                    label_now[e[0]]=label
                    #checked[e[0]]=1
                    break
        if checked[e[1]]==0:
            for label in range(1,max_label+1):                                    #because a vertex can be labeled with at most the max_label of the previous step
                if not violate_constraints(G2, label_now, k, e[1], label):        #if both vertices incident to the edges are unlabeled, then label both with consecutive integers
                    label_now[e[1]]=label
                    #checked[e[1]]=1
                    break
        #elif checked[e[0]]==0 and not checked[e[1]]==0:                          #if only one vertex is unlabeled, label that one
        #    for label in range(1,max_label+1):  
        #        if not violate_constraints(G2, label_now, k, e[0], label):
        #            label_now[e[0]]=label
        #            checked[e[0]]=1
        #            break
        #elif checked[e[1]]==0 and not checked[e[0]]==0:                          #if only one vertex is unlabeled, label that one
        #    for label in range(1,max_label+1):  
        #        if not violate_constraints(G2, label_now, k, e[1], label):
        #            label_now[e[1]]=label
        #            checked[e[1]]=1
        #           break
        #else:
            #continue
        checked[e[0]]=1
        checked[e[1]]=1
            
    #print(checked)
    not_checked=[i for i in checked if checked[i]==0]
    print(len(not_checked))
    
    if not len(not_checked)==0:
        for node in not_checked:                                                   #inner loop 2, label the unlabeled vertices in the reverse order of labels in previous step
            #if checked[node]==0:
            checked[node]=1
            for label in range(3,max_label+1):
                if not violate_constraints(G2, label_now, k, node, label):        #------this for loop can be made efficient------#
                    label_now[node]=label
                    break
        
    flag=0                                                                        #to check if the current span is bigger than the previous span
    for vertex, label in label_now.items():
        if label == 0 and checked[vertex]==1:                                     #if one vertex is labeled as 0, that means a label more than the previous span should have been needed
            flag=1
            break
    
    if flag==0:                                                                   #flag=0 means the current span is not greater thab the previous span
        label_init=label_now                                                      #replace the previous step's dictionary with current step's dictionary
    else:
        label_init=label_init
    
    max_label=max(label_init.values())                                            #finding the maximum label in this step
    for vertex, label in label_init.items():                                      #finding the maximum labeled vertex in this step
        if label == max_label:
            max_labeled=vertex
            break
    
    print(label_init)
    print(max_labeled)                                                            #printing for debugging and testing purposes
    print(max_label)
    print()


# In[10]:


nx.draw_networkx(G, with_labels=True)                                      #drawing the graph for debugging purposes
plt.show()


# In[ ]:




