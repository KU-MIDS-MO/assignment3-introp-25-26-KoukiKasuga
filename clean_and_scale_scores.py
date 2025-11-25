import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    ### Replace with your own code (begin) ###
    scores = scores.copy()
    scores[scores < min_score] = min_score
    scores[scores > max_score] = max_score
    scaled = (scores - min_score) / (max_score - min_score)
    return scaled
    pass
    ### Replace with your own code (end)   ###