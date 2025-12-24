---
title: Bridging Logic and Life - My Transition into Bioinformatics
author: <author_id>
date: 2025-12-24
categories: [Bioinformatics, Machine Learning]
tags: [python, genomics, research, resilience]
math: true
---

> "Where code meets curiosity, pain transforms into purpose."

For years, my world was defined by the abstract logic of **Computer Science**—Human-Computer Interaction in Italy, Statistics in Austria, and lecturing as an Assistant Professor. But life has a way of shifting our focus. After facing profound personal loss to Covid and Cancer, and navigating my own recovery from a brain injury, I decided to point my technical compass toward a new North: **Bioinformatics**.

## Why Bioinformatics?

Bioinformatics is the ultimate intersection of my previous research in **Machine Learning** and **Statistics**. It is the art of treating the biological code (DNA) with the same rigor we treat software source code. 

In my transition, I’ve realized that the challenges I face with memory and hippocampal sclerosis actually give me a unique perspective on **Data Redundancy** and **Error Correction**—core concepts in both neurology and genomics.

## The Project: Analyzing the Digital Code of Life

My first step into this field involves using Python to analyze genomic sequences. In bioinformatics, we often deal with strings of nucleotides (A, C, G, T). Even a simple analysis, like calculating **GC Content**, can tell us a lot about the stability of a DNA molecule.

Below is a snippet of how I am using `Biopython` to parse biological data:

```python
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# A sample DNA sequence
my_seq = Seq("AGTACACTGGT")

# Calculating the GC content - important for understanding DNA stability
print(f"GC Content: {gc_fraction(my_seq) * 100:.2f}%")
```

## From Statistics to Survival

Coming from a research fellowship where I focused on statistics, I see Bioinformatics not just as biology, but as a high-dimensional data problem. Whether it is identifying a mutation that leads to cancer or understanding how a virus like COVID-19 interacts with human cells, the math remains the bridge to the answer.

## Turning Pain into Passion

This blog has always been about curiosity. Now, that curiosity is directed at healing. I am currently exploring:

- Genomic Alignment: Using dynamic programming to find similarities in sequences.
- Structural Biology: Visualizing proteins to understand drug interactions.
- Machine Learning in Health: Applying my Salzburg ML foundations to predict disease markers.

If you are a developer, a researcher, or someone navigating their own "new normal," I invite you to follow along as I decode the mysteries of life, one line of code at a time.
