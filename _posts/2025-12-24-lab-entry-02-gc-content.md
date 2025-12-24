---
title: "Learning Lab #02: DNA Stability - Calculating GC Content"
author: zahid
date: 2025-12-24
categories: [Learning Lab, Lab Entries]
tags: [python, statistics, bioinformatics]
math: true
---

After mastering **Transcription** in my previous entry, the next logical step is to analyze the "strength" of the code. In Bioinformatics, we do this by calculating the **GC-content**.

## The Science

DNA isn't just a string; it's a physical structure. Because **G** and **C** share three hydrogen bonds compared to the two bonds in **A** and **T**, sequences with higher GC-content are more thermally stable.

The formula is a simple percentage:
$$GC\% = \frac{G + C}{A + T + G + C} \times 100$$

## The Code (Professor’s Approach)

Instead of just counting, I’ve written a function that handles any sequence length and provides a precision-rounded percentage. This combines my background in **Statistics** with new biological parameters.

```python
def calculate_gc_content(dna_seq):
    """
    Calculates the GC content percentage of a DNA sequence.
    """
    dna_seq = dna_seq.upper()
    g_count = dna_seq.count('G')
    c_count = dna_seq.count('C')
    
    total_length = len(dna_seq)
    
    if total_length == 0:
        return 0.0
        
    gc_percentage = ((g_count + c_count) / total_length) * 100
    return round(gc_percentage, 2)

# --- Test Case ---
sequence = "CCACCAGCTGCGTACG"
print(f"Sequence: {sequence}")
print(f"GC Content: {calculate_gc_content(sequence)}%")
```
