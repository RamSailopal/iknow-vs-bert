# iknow-vs-bert

A repo comparing the Natural Language Processing (NLP) sentiment accuracy of iKnow vs Bert. 

Bert uses training data (https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) to train it's model.

iKnow uses **"semantic attributes**" as a means of discovering the sentiment of a given text.

The review https://www.yelp.com/biz/social-brew-cafe-pyrmont is taken and then used as source data for both Bert and iKnow to process. Both will output sentiment scores that can then be compared to the actual scores on the Yelp site.

