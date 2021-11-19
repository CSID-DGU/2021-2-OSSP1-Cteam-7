# 2021-2-OSSP1-Cteam-7
공개SW프로젝트 2021-2 01분반 중국팀

## Problem Suggesting system based on NLP:Keyword Extraction
As we all known, whether it is a course quiz problem or some algorithm problem like leetcode, the explanation of the problem itself is usually not a sentence, it  tends to be in the form of a small paragraph. 
Using Natural Language Processing method to classify the problems in large quantities into categories based on keywords is now a hot direction in the industry. Compared to traditional methods, NLP based method can save both a lot of labor costs and time. 

Experiments Results Avaliable Now
In order to compare performances between transformer models, we set 100 questions as evaluation dataset and compare the models performance with manually labelled keywords and keywords calculated to see which model summarizes information better. The models will infer the questions one by one, and compare the relevance of the inferred keyword list (Top 5) with the manually labelled keyword list to get the score. The results(Top 5) is shown in the figure below:

![image](https://user-images.githubusercontent.com/90604378/142633965-08cbf384-8f31-4365-ba8b-23b286ab2dc2.png)


According to the benchmark,  “distill_bert_v1” shows best keyword extraction performance on our dataset. However, this does not mean that it is the best model in any scope. In fact, each model may achieve high score on different datasets. It is difficult to say that which is the best model. In previous studies, the weighted benchmark results of the most common datasets are usually used to determine whether a model has SOTA performance. In this article, our test results only represent the benchmark on our local dataset. 


This repo shows our implementations with four major parts:

### Search and create problem datasets
Done
### Setup transformer models for Questions and Candidate keywords/keyphrases embeddings.
Done
### Calculate Keywords for each Question and store in question-keyword dict format.
Done
### Create “Question Finder program” for user searching Questions using one-shot keywords or batch inference interface.
Done

That's all folks.
