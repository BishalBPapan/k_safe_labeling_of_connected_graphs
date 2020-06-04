# k_safe_labelings_of_connected_graphs
A python implementation of the algorithm for k-safe labeling of connected graphs proposed by Bishal Basak Papan and Protik Bose Pranto. This has been done as a part of the undergraduate thesis under the supervision of Professor Dr. Md. Saidur Rahman, Department of Computer Science and Engineering, Bangladesh University of Engineering and Technology(BUET). 

The problem of k-safe labeling was introduced by Habiba et. al in 2015. In a k-safe labeling, we need to label all the vertices of a graph with distinct integers such that the labels of two adjacent vertices have a difference of at least k. The span of a k-safe labeling is the value of (maximum label used - minimum label used + 1). Here we have considered 1 as the minimum label.

In a k-safe labeling problem, we need to k-safe label a graph with the minimum span. Habiba et. al have proved that this problem is NP-hard. We are suggesting a polynomial algorithm that will perform a k-safe labeling with a span which is not greater than a certain bound.

Implementation tools and libraries:

Language: Python 3.x
Libraries: networkx

Input type:

-Simple Connected Graph
-Vertex indexed by integers, starting from 0
