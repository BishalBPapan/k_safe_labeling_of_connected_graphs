#!/usr/bin/env python
# coding: utf-8

# In[34]:


import networkx as nx
import operator
import random
from matplotlib import pyplot as plt
import math
from datetime import datetime
import csv
from pathlib import Path
import numpy as np
#import png


# In[35]:


n = int(input())                                                                                        #input vertex count
m = int(input())                                                                                        #input edge count
k = int(input())                                                                                        #input the value of k
#G=nx.karate_club_graph()                                                                               #to test known dataset
#G=nx.Graph()                                                                                           #initialization of graph G
#G=nx.read_edgelist("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/30_170.txt", nodetype = int)  #input graph from a file 
G=nx.gnm_random_graph(n, m)
#G =nx.path_graph(n)
n=nx.number_of_nodes(G)
m=len([e for e in G.edges])
print(nx.is_connected(G))                                                                               #dataset checking
print(nx.is_directed(G))                                                                                #dataset checking
print(nx.graph_clique_number(G))
#print(nx.graph_number_of_cliques(G))
#A = nx.find_cliques(G)
#print(A)
#print(k)


# In[36]:


# Path("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/%s_%s" %(n,m)).mkdir(parents=True, exist_ok=True)

# now = datetime.now()
# name = now.strftime("%m_%d_%Y_%H_%M_%S")
# #data_filename = "%s.txt" % name
# #output_filename ="%s.txt" % name
# #graph_data = open('E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/graph_%s.txt' % name, 'w')
# output_data= open("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/%s_%s/simulation_%s.txt" %(n,m,name), "w")
# summary_data= open("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/%s_%s/summary_%s.txt" %(n,m,name), "w")
# sumr_table_file = open ("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/%s_%s/sumr_tab_%s.csv" %(n,m,name), "w")
# summary_table = csv.writer(sumr_table_file, delimiter=',', lineterminator='\n')
# #graph_data=("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/graph_1.txt", "w")
# #output_data=("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/output_1.txt", "w")

# summary_table.writerow(["Vertex \n n", "Edge \n m", "k", "Non_edges", "Removed_edge", "Max_clique \n q", "max_degree \n d", "max_label \n I_l", "upper_bound \n S_u"])


# In[37]:


def large_clique_size(G):
    degrees = G.degree

    def _clique_heuristic(G, U, size, best_size):
        if not U:
            return max(best_size, size)
        u = max(U, key=degrees)
        U.remove(u)
        N_prime = {v for v in G[u] if degrees[v] >= best_size}
        return _clique_heuristic(G, U & N_prime, size + 1, best_size)

    best_size = 0
    nodes = (u for u in G if degrees[u] >= best_size)
    for u in nodes:
        neighbors = {v for v in G[u] if degrees[v] >= best_size}
        best_size = _clique_heuristic(G, neighbors, 1, best_size)
    return best_size


# In[38]:


E=[e for e in G.edges]                      #not necessary, only used it to debug
print(E)
q=large_clique_size(G)
q_now=nx.graph_clique_number(G)
print("MaxClique size: ",q, q_now)
# output_data.write("============= INPUT DESCRIPTION: ===============\r\n")
# output_data.write("k: %d \n" % k)
# output_data.write("Vertex_count(n): %d \n" % nx.number_of_nodes(G))
# output_data.write("Maximum Clique Size(q): %d \n" %q)
# output_data.write("Edge_count(m): %d \r\n" %len(E))
# output_data.write("Edges: \r\n")
# #graph_data.write(E)
# output_data.writelines( "(%s,%s)\n" %(item1,item2)  for (item1,item2) in E )
# output_data.write("\r\n")

# summary_data.write("============= INPUT DESCRIPTION: ===============\r\n")
# summary_data.write("k: %d \n" % k)
# summary_data.write("Vertex_count(n): %d \n" % nx.number_of_nodes(G))
# summary_data.write("Maximum Clique Size(q): %d \n" %q)
# summary_data.write("Edge_count(m): %d \n" %len(E))


# In[39]:


n=nx.number_of_nodes(G)
print(n)
G2=nx.complete_graph(n)                                                           #conversion to complete graph


# In[40]:


E_c=[e for e in nx.non_edges(G)]                                                  #edges in complement graph of G
non_edge_cnt=len(E_c)
print(len(E_c))
print(E_c)
# output_data.write("No. of edges to remove: %d\n" %len(E_c))
# output_data.write("Non_edges: \r\n")
# #graph_data.write(E_c)
# output_data.writelines( "(%s,%s)\n" %(item1,item2)  for (item1,item2) in E_c)
# output_data.write("\r\n\n")

# summary_data.write("No. of edges to remove: %d\r\n\n" %len(E_c))


# In[41]:


#label_init=[v*k+1 for v in G.nodes]
label_init={vertex:vertex*k+1  for vertex in G2.nodes}                           #labeling the complete graph using a dictionary
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
max_degree = sorted([d for n, d in G2.degree()], reverse=True)[0]
print("Degrees: ")
print(sorted([d for n, d in G2.degree()], reverse=True))
print("Max Degree: ", max_degree)
print("Max Labeled: ",max_labeled)
print("Max Label: ",max_label)
# output_data.write("============ OUTPUT DESCRIPTION: ================\r\n\n")
# output_data.write("ITERATION 0: \r\n")
# output_data.write("Initial_labels: \r\n{")
# #output_data.write(label_init)
# output_data.writelines( "%d: %d\n" %(item1,item2)  for item1,item2 in label_init.items())
# output_data.write("}\r\n")
# output_data.write("max_labeled_vertex: %d \n" %max_labeled)
# output_data.write("max_label: %d \n" %max_label)
# output_data.write("max_degree: %d \r\n" %max_degree)

# summary_data.write("============ OUTPUT DESCRIPTION: ================\r\n\n")
# summary_data.write("<<----------------- Iteration: 0 ----------------->>\r\n")
# summary_data.write("max_labeled_vertex: %d \n" %max_labeled)
# summary_data.write("max_label: %d \r\n" %max_label)
# summary_data.write("max_degree: %d \r\n" %max_degree)

# summary_table.writerow([n, len(E), k, non_edge_cnt, "_", n, max_degree, max_label, max_label])


# In[42]:


def violate_constraints(G_now, label_now, k, vertex, label_this):                                       #this function checks if a label violates the constraints of k-safe labeling
    for node in nx.all_neighbors(G_now, vertex):
        if label_this in label_now.values() or (label_now[node] > 0 and ((label_this-label_now[node] < k and label_this-label_now[node] > 0) or (label_now[node]-label_this < k and label_now[node]-label_this >0))):
            return True


# In[43]:


def non_over_max_cliques(G_now, max_clique_size):
    checked = []
    all_cliques=list(nx.find_cliques(G_now))
    maxm=max_clique_size
    non_overlap_cnts=0
    while maxm>=3:
        found=0
        for clique in all_cliques:
            if len(clique)==maxm:
                found=1
                flag=0
                for vertex in clique:
                    if vertex in checked:
                        flag=1
                        break
                if flag==0:
                    non_overlap_cnts+=1
                    print("Non overlapping clique of size ", len(clique), ": ", clique)
                    for vertex in clique:
                        checked.append(vertex)
                all_cliques.remove(clique)
        if found==0:
            print("Non overlapping clique count of size ", maxm, ", is: ", non_overlap_cnts)
        maxm=maxm-1


# In[44]:


edge_stack = []                                                                   #stack where removed edges are pushed
same_count =0
i=0
edge_checked=set()
flag_o=0
clique_same_count=1
curr_bound=0
clique_unchanged=0
clique_changed_flag=0
clique_diff=0

while not len(E_c)==0:                                                            #first outer loop, label_init is the dictionary of the previous step
    q_old=nx.graph_clique_number(G2)
    i+=1
    label_init={node: label for node, label in sorted(label_init.items(), key=lambda item: item[1], reverse=True)}
    label_p=label_init                                                            #not necessary
#     output_data.write("==============START of ITERATION: %d============= \r\n" %i)
#     summary_data.write("<<----------------- Iteration: %d ----------------->> \r\n" %i)
#     output_data.write("Initially: \r\n{")
#     #output_data.write(label_p)
#     output_data.writelines( "%d: %d, \n" %(item1,item2)  for item1,item2 in label_p.items())
#     output_data.write("}\r\n")
    nodes_reversed=[node for node in label_init]                           #sorting the vertices in decreasing order of labels
#     output_data.write("Nodes reversed based on previous labels: \r\n[")
#     #output_data.write(nodes_reversed)
#     output_data.writelines( "%s, " %item  for item in nodes_reversed)
#     output_data.write("]\r\n")
#     #node_now=0
    #node_conn=0
    e_incident=None
    flag_i=0
    #for node in nodes_reversed:                                                   
        #if not node in edge_checked:                                                  #taking any random edge incident to the first maximum labeled vertex
        #if not len([e for e in E_c if e[0]==node or e[1]==node])==0:                   #which has an incident edge in E_c
            #e_incident=[e for e in E_c if e[0]==node or e[1]==node][len([e for e in E_c if e[0]==node or e[1]==node])-1]
            #break
            
    for e in E_c:
        if not e[0] in edge_checked and not e[1] in edge_checked:
            e_incident=e
            #edge_checked.append(e[0])
            #edge_checked.append(e[1])
            edge_checked.add(e[0])
            edge_checked.add(e[1])
            break
    
    '''if e_incident==None:
        for e in E_c:
            if e[0] in edge_checked and not e[1] in edge_checked:
                e_incident=e
                edge_checked.append(e[1])
                break
            elif not e[0] in edge_checked and e[1] in edge_checked:
                e_incident=e
                edge_checked.append(e[0])
                break
                
    for v in range(0, n):
        if not v in edge_checked and not len([e for e in E_c if e[0]==v or e[1]==v])==0:
            flag_i=1
            break
            
    if flag_i==0:
        edge_checked=[]'''
    
    if e_incident==None:
        if not len(edge_checked)==n:
            for e in E_c:
                if e[0] in edge_checked and e[1] in edge_checked:
                    e_incident=e
                    break
        else:
            edge_checked=set()
                
    if e_incident==None:
        edge_checked=set()
        continue
            
    print(edge_checked)
    
    #max_l=0
    #for node, label in label_init.items():
        #if ((node_now,node) in E_c or (node,node_now) in E_c) and abs(label_init[node_now]-label_init[node])>max_l:
            #max_l=abs(label_init[node_now]-label_init[node])
            #node_conn=node
    
    #print(node_now,node_conn)
    #if (node_now,node_conn) in E_c:
        #edge_stack.append((node_now,node_conn))
        #E_c.remove((node_now,node_conn))
        #G2.remove_edge(node_now, node_conn)
    #elif (node_conn,node_now) in E_c:
        #edge_stack.append((node_conn,node_now))
        #E_c.remove((node_conn,node_now))
        #G2.remove_edge(node_conn, node_now)
    
    print("Edge incident: ", e_incident)
    edge_stack.append(e_incident)                                                 #adding the edge to the stack
    #print(len(E_c))
    E_c.remove(e_incident)                                                        #removing the edge from E_c
    #print(len(E_h))
    #output_data.write(edge_stack)
    #E_cc

    if G2.has_edge(e_incident[0], e_incident[1]):
        G2.remove_edge(e_incident[0], e_incident[1])                              #removing the edge from G2
        #output_data.write("Removed edge: (%d,%d)\r\n" %(e_incident[0],e_incident[1]))
        #summary_data.write("Removed edge: (%d,%d)\r\n" %(e_incident[0],e_incident[1]))
    elif G2.has_edge(e_incident[1], e_incident[0]):
        G2.remove_edge(e_incident[1], e_incident[0])
        #output_data.write("Removed edge: (%d,%d)\r\n" %(e_incident[1],e_incident[0]))
        #summary_data.write("Removed edge: (%d,%d)\r\n" %(e_incident[1],e_incident[0]))
        
    print(edge_stack)
    #output_data.write("Stack currently: \r\n[")
    #output_data.writelines( "(%d, %d), \n" %(item1,item2)  for (item1,item2) in edge_stack)
    #output_data.write("]\r\n")
    print("Remaining edges:", len(E_c))
    #output_data.write("Remaining edges to remove: %d \r\n" %len(E_c))
    
    #q_now=large_clique_size(G2)
    q_now=nx.graph_clique_number(G2)
    #print(large_clique_size(G2))
    #print(list(nx.non_edges(G2)))
    label_now={vertex:0  for vertex in nodes_reversed}                            #initializing the dictionary of current step with labels 0
    checked={vertex:0 for vertex in nodes_reversed}
    #label_now[e_incident[0]]=1
    #label_now[e_incident[1]]=2
    #if same_count == 0:
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
    #output_data.write("Unchecked edges after end vertices: %d \r\n" %len(not_checked))
    
    #if same_count==0:
        #minm=3
    #else:
        #minm=1
    
    if not len(not_checked)==0:
        for node in not_checked:                                                   #inner loop 2, label the unlabeled vertices in the reverse order of labels in previous step
            #if checked[node]==0:
            checked[node]=1
            for label in range(3,max_label+1):
                if not violate_constraints(G2, label_now, k, node, label):        #------this for loop can be made efficient------#
                    label_now[node]=label
                    break
                    
    max_degree = sorted([d for n, d in G2.degree()], reverse=True)[0]
    print("Degrees: ")
    print(sorted([d for n, d in G2.degree()], reverse=True))
    nparr=np.array(G2.degree())
    #print("Std_dev of degrees: ", np.std(nparr))
    #print("Triangles: ", nx.triangles(G2))
    #print("Min_Triangles: ", min((nx.triangles(G2)).values()))
    #print("Max_Triangles: ", max((nx.triangles(G2)).values()))
    #print("Avg Triangles: ", float(sum((nx.triangles(G2)).values()) / len(nx.triangles(G2))))
    #print("Maximal Cliques: ", list(nx.find_cliques(G2)))
    
    #if q_now<=(math.floor(nx.number_of_nodes(G2)/2))+1:
        #non_over_max_cliques(G2, q_now)
    #same_count=0
    flag=0                                                                        #to check if the current span is bigger than the previous span
    for vertex, label in label_now.items():
        if label == 0 and checked[vertex]==1:                                     #if one vertex is labeled as 0, that means a label more than the previous span should have been needed
            flag=1
            break
    
    if flag==0:                                                                   #flag=0 means the current span is not greater thab the previous span
        label_init=label_now                                                      #replace the previous step's dictionary with current step's dictionary
        #same_count=0
    else:
        #same_count=1
        label_init=label_init
    
    max_label=max(label_init.values())                                            #finding the maximum label in this step
    for vertex, label in label_init.items():                                      #finding the maximum labeled vertex in this step
        if label == max_label:
            max_labeled=vertex
            break
    
    upper_bound=0
    upper_bound_new=0
    
    if q_now==q_old and q_now>=int(nx.number_of_nodes(G2)/2) and clique_changed_flag==0:
        clique_unchanged=q_old
        clique_diff=q_old-int(nx.number_of_nodes(G2)/2)
        clique_changed_flag=1
        
    #if n-q_now>q_now:
        #upper_bound=math.ceil(((n-q_now)/q_now)*(q_now-1)*k)
    #else:
        #upper_bound=math.ceil((n/q_now)*(q_now-1)*k)  +(math.floor((clique_same_count)/q_now))*(k-1)
    #if not q_now==q_old:
        #upper_bound=(k-1)*q_now+n+1
        #curr_bound=(k-1)*q_now+n+1
    #else:
        #upper_bound=curr_bound
    #upper_bound=math.ceil(((n-q_now)/q_now)*(q_now-1)*k)
    if q_now>=clique_unchanged:
        upper_bound=(k-1)*q_now+n+1-k
    else:
        upper_bound=(k-1)*clique_unchanged+n+1-k
    #elif q_now<int(nx.number_of_nodes(G2)/2):
        #if q_now<=int(max_degree/2):
            #upper_bound=min((k-1)*(int(nx.number_of_nodes(G2)/2))+n+1-k, (max_degree-q_now+1)*k+n)
            #upper_bound=min((k-1)*(int(nx.number_of_nodes(G2)/2))+n+1-k, (max_degree-q_now+1)*k+n)+clique_changed_flag*(clique_unchanged-int(nx.number_of_nodes(G2)/2))*k
            #upper_bound_new=(k-1)*q_now+n+1-k+clique_diff*k
            #upper_bound=min((k-1)*(int(nx.number_of_nodes(G2)/2))+n+1-k, q_now*k+(int(max_degree/q_now))*k+max_degree-q_now+(int(n/max_degree))*k)
            #upper_bound=min((k-1)*clique_unchanged+n+1-k, (max_degree-q_now)*k+1+(max(int(n/(max_degree-(max_degree % 2))), (int(max_degree/(q_now-(q_now % 2))))))*k+n)
            #print("------------------------", (max_degree-q_now-1)*k+1+(int(n/max_degree))*k+n)
        #else:
            #upper_bound=max_degree*k+n
#     else:
#         upper_bound=(k-1)*int(clique_unchanged/2)+n+1-k
    
    if q_now==q_old:
        clique_same_count+=1
    else:
        #print("clique_same_count= ", clique_same_count)
        clique_same_count=1
    
    print("Initial label: ", label_init)
#     output_data.write("Labels in this iteration: \r\n{")
#     #output_data.write(label_init)
#     output_data.writelines( "%d: %d, \n" %(item1,item2)  for item1,item2 in label_init.items())
#     output_data.write("}\r\n")
    print("Maximum labeled vertex: ", max_labeled)                                               #printing for debugging and testing purposes
#     output_data.write("Current Maximum labeled vertex: %d \r\n" %max_labeled)
#     summary_data.write("Current Maximum labeled vertex: %d \r\n" %max_labeled)
    print("Maximum Degree=",max_degree)
#     output_data.write("Maximum Degree: %d \n" %max_degree)
#     summary_data.write("Current Degree: %d \n" %max_degree)
    print("Maximum=",max_label)
#     output_data.write("Current Maximum label: %d \n" %max_label)
#     summary_data.write("Current Maximum label: %d \n" %max_label)
    print("Clique=",q_now)
#     output_data.write("Current Maximum Clique Size: %d \r\n" %q_now)
#     summary_data.write("Current Maximum Clique Size: %d \r\n" %q_now)
    print("Upper Bound=",upper_bound)
#     print("New Upper Bound=",upper_bound_new)
#     print("Clique_unchanged=", clique_unchanged)
    print()
#     output_data.write("\r\n")
#     summary_data.write("\r\n")
#     output_data.write("============end of iteration: %d =========== \r\n" %(i+1))
    
#     summary_table.writerow([n, len(E), k, len(E_c), e_incident, q_now, max_degree, max_label, upper_bound])
    #image_file = open ("E:/Papan(F)/Books/Thesis materials/Algo_python_simulation/Random_choice_edges/%s_%s/%s_step_%s.png" %(n,m,name,i), 'wb')
    
    #nx.draw_circular(G2, labels=label_init)                                      #drawing the graph for debugging purposes
    plt.show()
    #plt.savefig(image_file)
    plt.close()
    #image_file.close()


# In[45]:


# output_data.close()
# summary_data.close()
# sumr_table_file.close()


# In[46]:


nx.draw_networkx(G, with_labels=True)                                      #drawing the graph for debugging purposes
plt.show()


# In[ ]:





# ##### 
