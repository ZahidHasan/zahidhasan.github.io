---
published: true
key: '!!str'
title: How to Run DeepSeek R1 Locally on Windows
tag:
  - Windows
  - Linux
  - DeepSeek
  - AI
  - Machine Learning
---
The DeepSeek R1 model, developed by a team from China, has made waves in the AI world. It has surpassed ChatGPT and climbed to the top spot on the US App Store. Furthermore, DeepSeek has shaken the US tech stock market with its innovative R1 model, which claims to rival ChatGPT o1. Although you can access DeepSeek R1 for free on its official website, many users are concerned about privacy since the data is stored in China. If you'd like to run DeepSeek R1 on your PC or Mac, you can easily do so using LM Studio and Ollama. Here's a step-by-step guide to help you get started.

## What is Needed to Run DeepSeek Locally?
To operate DeepSeek R1 on a PC, Mac, or Linux system, your machine should have a minimum of 8GB of RAM. This amount of memory allows you to smoothly run the small DeepSeek R1 1.5B model, providing output at approximately 13 tokens per second. You can also handle the 7B model, but it will utilize around 4GB of memory, potentially causing your system to be a bit sluggish.

With additional memory, you could also manage the 14B, 32B, and 70B models, although a faster CPU and GPU would be necessary. Currently, most software doesn't leverage the NPU (Neural Processing Unit) for running local AI models. Instead, they primarily depend on the CPU and, in certain instances (such as high-end Nvidia GPUs), the GPU is used for inferencing.

For Android phones and iPhones, it's advisable to have at least 6GB of memory to efficiently run the DeepSeek R1 model locally. You can operate DeepSeek R1 on your Snapdragon 8 Elite, or other Snapdragon chipsets in the 8-series and 7-series. Moreover, you can explore how the Deepseek R1 and ChatGPT o1 models stack up right here. 

## Run DeepSeek R1 on PC Using LM Studio or Olama
LM Studio and Ollama are both tools designed to help developers and researchers work with large language models (LLMs) locally on their machines. LM Studio is a desktop application that allows users to discover, download, and run open-source LLMs locally on their computers. Ideal for users who want to explore different LLMs without needing to set up complex environments.
![LMStudio-Web.png]({{site.baseurl}}/images/LMStudio-Web.png)
