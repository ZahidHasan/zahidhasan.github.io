---
title: "Learning Lab #01: Transcription - The Software of Life"
author: author_id
date: 2025-12-25
categories: [Learning Lab, Lab Entries]
tags: [python, bioinformatics, biology]
pin: false
---

> "In Computer Science, we move data between buffers. In Biology, we call this Transcription."

## 🧬 The biological Logic

Transcription is the process where a DNA sequence is copied into a new molecule of messenger RNA (mRNA). The main difference? RNA uses **Uracil (U)** instead of **Thymine (T)**.

## 💻 The Implementation

I've written this Python function with a **validation step**. As a former Professor, I know that your results are only as good as your data—so we must ensure our sequence only contains `A, C, G, T`.

```python
def dna_to_rna(dna_sequence):
    # 1. Standardize input
    dna = dna_sequence.upper().strip()
    
    # 2. Validation (Data Integrity)
    valid_bases = set("ACGT")
    if not set(dna).issubset(valid_bases):
        raise ValueError("Invalid DNA sequence! Only A, C, G, T allowed.")
    
    # 3. Transcription Logic
    return dna.replace("T", "U")

# Testing the Lab Entry
try:
    my_dna = "ATGCGTACGT"
    print(f"Original DNA: {my_dna}")
    print(f"Transcribed RNA: {dna_to_rna(my_dna)}")
except ValueError as e:
    print(e)
``

🧠 Reflection
This was my first step back into the "Alphabet of DNA." It's a simple string replacement, but it represents the first hurdle in my journey to bridge CSE and Biology.

Status: Module 1 - [x] Lab 01: Transcription Complete.