import networkx as nx
import matplotlib.pyplot as plt

def display_permutation_graph(n, perm_string):
    """
    takes in size n (less than 10 for now)

    and perm string (one line notation permutation)
    """
    if n >= 10:
        raise ValueError("n must be less than 10")
    if len(perm_string) != n:
        raise ValueError(f"permutation string not of length {n}")
    if not all(c.isdigit() and 1 <= int(c) <= n for c in perm_string):
        raise ValueError(f"all digits must be between 1 and {n}")
    

    perm = [int(x) for x in perm_string]
    G = nx.DiGraph()
    
    for i in range(n):
        G.add_edge(i+1, perm[i])
    pos = nx.spring_layout(G,k=1.5)
    plt.figure(figsize=(5, 5))
    
    # draw graph
    nx.draw(G, pos, 
           node_color='lightblue',
           node_size=500,
           with_labels=True,
           arrows=True,
           arrowsize=20,
           edge_color='gray',
           font_size=16,
           font_weight='bold')

    # generate canonical cycle notation
    cycles = get_cycles(n, perm_string)
    canonical_notation = get_canonical_notation(cycles)
    
    # generate caption
    plt.figtext(0.5, 0.01, f"Permutation: {perm_string} | Canonical Cycle Notation: {canonical_notation}",
                ha="center", fontsize=14, bbox={"facecolor":"lightgray", "alpha":0.5, "pad":5})
    
    plt.title(f"permutation: {perm_string}")
    plt.show()

# get cycles
def get_cycles(n, perm_string):
    perm = [int(x) for x in perm_string]
    G = nx.DiGraph([(i+1, perm[i]) for i in range(n)])
    cycles = list(nx.simple_cycles(G))
    return cycles
def get_canonical_notation(cycles):
    """
    Converts cycles to canonical cycle notation
    """
    processed_cycles = []
    for cycle in cycles:
        max_elem = max(cycle)
        max_pos = cycle.index(max_elem)
    
        rotated_cycle = cycle[max_pos:] + cycle[:max_pos]        
        processed_cycles.append((max_elem, rotated_cycle))

    processed_cycles.sort()  

    if not processed_cycles:
        return "()"
    
    result = ""
    for _, cycle in processed_cycles:
        result += "(" + " ".join(map(str, cycle)) + ")"
    
    return result if result else "()"

# test usage
display_permutation_graph(7, "3275461")
