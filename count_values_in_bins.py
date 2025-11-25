import numpy as np

def count_values_in_bins(data, bin_edges):
    ### Replace with your own code (begin) ###
    B = len(bin_edges) - 1
    counts = np.zeros(B, dtype=int)

    for x in data:
        for i in range(B):
            if i == B - 1:
                if bin_edges[i] <= x <= bin_edges[i + 1]:
                    counts[i] += 1
                    break
            else:
                if bin_edges[i] <= x < bin_edges[i + 1]:
                    counts[i] += 1
                    break
    return counts
    pass
    ### Replace with your own code (end)   ###

