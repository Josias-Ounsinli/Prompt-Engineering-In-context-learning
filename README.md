# Prompt-Engineering-In-context-learning

# Prompt Engineering: In-context learning with GPT-3 and other Large Language Models 

## Business objective  

Large Language Models coupled with multiple AI capabilities to generate images and text as well as achieving human level performance on a number of tasks, the world is going through revolution in art (DALL-E, MidJourney, Imagine, etc.), science (AlphaFold), medicine, and other key areas. 
In-context learning, popularized by the team behind the GPT-3 LLM, brought a new revolution for using LLMs in so many tasks that the LLM is not trained for. This is in contrast to the usual fine-tuning that was required to equip AI models to perform better in tasks they are not trained for. 
With In-context learning, LLMs are able to readjust their performance on a task depending on the prompt - from structured input that can be considered partly a few-shot training and partly a test input. This has opened up many applications.  
This challenge is to systematically explore strategies that help generate prompts for LLMs to do classification of web pages according to a few examples of human scores. You will be also required to compare responses and accuracies of multiple LLM models for a given prompt.  

## Project Overview
There is a system that collects news artifacts from web pages, tweets, facebook posts, etc. One is interested in scoring a given news against a topic. The purpose is to score these news items in the range from 0 to 1 where a score of 0 means the news item is totally NOT relevant while a score of 1 means the news item is very relevant. The numbers in between 0 and 1 implies the  degree of relevance of the news item is to the topic. 
The objectif of this work is to explore how useful existing LLMs like GPT-3 are for this task.

## Data
There are two datasets you will use for this project

### Data 1:

This data comes from the system described above. The columns of this data are as follows:

Domain - the base URL or a reference to the source these item comes from 
Title - title of the item - the content of the item
Description - the content of the item
Body - the content of the item
Link - URL to the item source (it may not functional anymore sometime)
Timestamp - timestamp that this item was collected at
Analyst_Average_Score -  target variable - the score to be estimated 
Analyst_Rank - score as rank
Reference_Final_Score - Not relevant for now - it is a transformed quantity


### Data 2:
The data are job descriptions (together named entities)  and  relationships between entities in json format.
The data we shall use is:
 - Dataset 1: [For development and training](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt).
 - Dataset 2: [For testing and final reporting](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt)


