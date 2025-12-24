---
layout: tabs
title: Learning Lab
icon: fas fa-flask
order: 2
permalink: /learning-lab/ # The permanent URL for the page
---


## 🧪 The Learning Lab

This is my public notebook where I document my transition from **Silicon** (Computer Science) to **Carbon** (Bioinformatics).

### 🧬 Module 1: Biological Foundations

- [x] The Central Dogma (DNA $\rightarrow$ RNA $\rightarrow$ Protein)
- [ ] Understanding GenBank & FASTA file formats
- [ ] Chromosome Mapping basics

### 💻 Module 2: Computational Tools

- [x] Biopython Environment Setup
- [ ] Implementing the Smith-Waterman Algorithm
- [ ] Exploratory Data Analysis (EDA) on Genomic Datasets

#### 📊 Module 3: Statistical Genomics

- [ ] Applying Salzburg ML Research to Gene Expression
- [ ] P-value significance in BLAST searches

### 📝 Recent Lab Entries

Here are my latest experiments, organized by logic and sequence:

{% for post in site.categories["Learning Lab"] %}

- [{{ post.title }}]({{ post.url }}) — *{{ post.date | date: "%Y-%m-%d" }}*

{% endfor %}
