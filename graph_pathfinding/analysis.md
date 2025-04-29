## Analysis of DFS and BFS Results

### Task

Compare the results of DFS and BFS algorithms for the given graph. Highlight the differences in the obtained paths and explain why the paths differ.

### Graph Structure

The graph represents a network of connections between characters:

**Nodes:**
Luke, Leia, Han, Aragorn, Legolas, Neo

**Edges:**

- Luke — Leia
- Luke — Han
- Leia — Han
- Han — Aragorn
- Leia — Aragorn
- Aragorn — Legolas
- Aragorn — Neo
- Legolas — Neo

### Results

**DFS path from Luke to Neo:**  
`['Luke', 'Han', 'Aragorn', 'Neo']`

**BFS path from Luke to Neo:**  
`['Luke', 'Leia', 'Aragorn', 'Neo']`

### Analysis and Explanation

- **Depth-First Search (DFS):**  
  DFS explores as deep as possible along one path before backtracking. In this case, it starts from "Luke", chooses "Han" first, then continues to "Aragorn", and finally reaches "Neo". It does not guarantee the shortest path, but finds a valid one based on the order of neighbor traversal.

- **Breadth-First Search (BFS):**  
  BFS explores all neighbors level by level. It starts from "Luke", checks both "Leia" and "Han", but chooses "Leia" first. From "Leia", it goes to "Aragorn", and then to "Neo". This results in a path that is also four nodes long, but follows a different route. BFS guarantees the shortest path in terms of number of edges, which is useful in unweighted graphs.

### Conclusion

Although both algorithms returned paths of the same length (4 nodes), the sequences differ:

- DFS returned: `Luke → Han → Aragorn → Neo`
- BFS returned: `Luke → Leia → Aragorn → Neo`

The difference arises due to the traversal strategies of the algorithms:

- DFS prioritizes depth and follows one path deeply before trying alternatives.
- BFS prioritizes breadth and explores all neighbors on the current level before going deeper.

This explains why the paths are different even though they both lead to the correct destination.
