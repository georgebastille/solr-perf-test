#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from collections import Counter

from tqdm.auto import tqdm

doc_file = "../input/HackerNewsStories.jsonl"
unigrams = Counter()
bigrams = Counter()

def extract_ngrams(toks, n):
    #toks = text.split()
    n_grams = []
    for i in range(len(toks) - n +1):
        tmp = [toks[j] for j in range(i, i+n)]
        n_grams.append(" ".join(tmp))
    return n_grams

def extract_n_from(counted, n):
    top_section = 1./10000 * len(counted)
    bottom_section = 1./100 * len(counted)
    top_section = int(top_section)
    bottom_section = int(bottom_section)
    return counted.most_common()[top_section:top_section+n],            counted.most_common()[bottom_section:bottom_section+n]

def write_out(dict_to_write, filename):
    with open(filename, "w") as out:
        for value in dict_to_write:
            out.write(f"{value[0]}\n")
    
    
if __name__ == "__main__":

    with open(doc_file, "r") as doc_handle:
        for doc_json in tqdm(doc_handle, total=1333789):
            doc_dict = json.loads(doc_json)
            title_toks = doc_dict.get("title", "").lower().split()
            unigrams.update(title_toks)
            bigrams.update(extract_ngrams(title_toks, 2))
            
    unigram_top, unigram_bottom = extract_n_from(unigrams, 1000)
    bigram_top, bigram_bottom = extract_n_from(bigrams, 1000)
    
    write_out(unigram_top, "unigram_top.txt")
    write_out(unigram_bottom, "unigram_bottom.txt")
    write_out(bigram_top, "bigram_top.txt")
    write_out(bigram_bottom, "bigram_bottom.txt")

