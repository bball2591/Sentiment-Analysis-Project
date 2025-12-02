# Industry Sentiment Analysis with NewsAPI and VADER

This project builds a complete sentiment analysis pipeline using financial news headlines collected from NewsAPI. Each headline is processed with a custom VADER based SentimentAnalyzer, and the results are grouped by industry to compare sentiment across sectors. The project demonstrates how data collection, natural language processing, and data visualisation can be combined into a single analytical workflow.

## Overview

- Collect news data across multiple industries using NewsAPI  
- Apply a custom VADER based sentiment analyzer implemented in Python  
- Build a dataset containing sentiment scores, article metadata, and industry labels  
- Visualise sentiment differences across industries  
- Analyse sentiment distributions, time trends, and category proportions  

## Project Structure

The repository contains:

- sentiment_analyzer.py  
- industry_sentiment.ipynb  
- sentiment_data_results.csv  
- README.md  

## Getting Started

Install required libraries using pip or conda.  
Obtain a free API key from NewsAPI and store it in your notebook or script.  
Open the Jupyter Notebook to run the full workflow, from data collection to visualisation.

## Sentiment Analysis

The sentiment analyzer uses the VADER lexicon to compute negative, neutral, positive, and compound scores for each headline. A final sentiment label is assigned to each article. This method works well for short texts such as headlines and small news snippets.

## Visualisations

The notebook includes several visualisations:

- Bar chart of average sentiment by industry  
- Sentiment label distribution for each industry  
- Pie chart of overall sentiment distribution  
- Boxplot of sentiment score variability  
- Time based scatter plot of sentiment values  
- Heatmap showing sentiment proportions by industry  

These visuals highlight clear differences in sentiment across sectors.

## Findings

- Neutral sentiment appears most frequently across all industries  
- Telecom, Retail and Apparel, and Healthcare show the highest average positive sentiment  
- Food and Beverage has the lowest average sentiment and higher negative proportions  
- All industries contain a wide range of sentiment values  
- Sentiment varies over time as news events unfold  

## Future Work

Potential extensions include using transformer based models, comparing multiple news sources, building an interactive dashboard, or exploring predictive links between sentiment and market behaviour.

## License

This project is intended for educational and portfolio use.
