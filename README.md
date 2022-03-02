# iknow-vs-bert

![Alt text](iknow-bert.webp?raw=true "iKnow vs Bert")

A repo comparing the Natural Language Processing (NLP) sentiment accuracy of iKnow vs Bert. 

Bert uses training data (https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) to train it's model.

iKnow uses **Named Entity Recognition** (NER) and **"semantic attributes**" as a means of discovering the sentiment of a given text.

The review https://www.yelp.com/biz/social-brew-cafe-pyrmont is taken and then used as source data for both Bert and iKnow to process. Both will output sentiment scores that can then be compared to the actual scores on the Yelp site.

 # Gitpod
   
1) Create a free/paid Gitpod account - https://www.gitpod.io/
2) Log into the account
3) Open a new browser tab and add **gitpod.io/#https://github.com/RamSailopal/iknow-vs-bert** to the address - This will create a new Gitpod cloud instance.
4) Let the containers fully load.
5) A browser panel will appear showing the link referenced above with the actual ratings/reviews.
6) Three terminal windows will appear. The second will show the results of iKnow against the referenced link and the third, the results of Bert.

# References

**Intersystems iKnow** - https://github.com/intersystems/iknow

**Google Bert** - https://github.com/google-research/bert
