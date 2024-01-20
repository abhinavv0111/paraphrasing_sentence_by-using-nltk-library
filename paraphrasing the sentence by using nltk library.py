#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


# In[2]:


import nltk
from nltk.tokenize import sent_tokenize, RegexpTokenizer

# Download the NLTK data
nltk.download('punkt')


# # original text

# In[3]:


# Tokenize the sentences and words


# In[4]:


original_text = """
Artificial Intelligence (AI) plays a pivotal role in contemporary society, permeating various facets of daily life. 
In healthcare, AI facilitates early disease detection through advanced diagnostic tools, personalized treatment plans, 
and predictive analytics. Additionally, AI-driven robotic surgeries enhance precision and minimize human error. 
In finance, AI algorithms analyze vast datasets for market trends, optimize trading strategies, 
and detect fraudulent activities, ensuring economic stability.
"""


# In[5]:


sentences = sent_tokenize(original_text)
tokenizer = RegexpTokenizer(r'\w+')
tokenized_sentences = [tokenizer.tokenize(sentence.lower()) for sentence in sentences]



# In[6]:


# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_sentences = [
    [word for word in sentence if word not in stop_words]
    for sentence in tokenized_sentences]


# In[7]:


# Join the words to form paraphrased sentences
paraphrased_sentences = [' '.join(sentence) for sentence in filtered_sentences]


# In[8]:


# Join the paraphrased sentences to form the paraphrased text
paraphrased_text = ' '.join(paraphrased_sentences)


# In[9]:


print(paraphrased_text)


# In[ ]:




