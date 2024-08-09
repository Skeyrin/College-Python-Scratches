from os import F_LOCK
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

files = []

for i in range(5):
  test_file = open(f"file{i+1}.txt", "r")
  test = test_file.read()
  files.append(test)

def Cleandoc(documents):
  documents_clean = []
  for d in documents:
      # Remove Unicode
      document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
      # Remove Mentions
      document_test = re.sub(r'@\w+', '', document_test)
      # Lowercase the document
      document_test = document_test.lower()
      # Remove punctuations
      document_test = re.sub(r'[^\w\s]', '',document_test)
      # Lowercase the numbers
      document_test = re.sub(r'[0-9]', '', document_test)
      # Remove the doubled space
      document_test = re.sub(r'\s{2,}', ' ', document_test)
      documents_clean.append(document_test)
  return documents_clean
fc = Cleandoc(files)
print(f"banyak file : {len(fc)}")
print(fc)

vectorizer = TfidfVectorizer()# It fits the data and transform it as a vector
def TfIdf(docs):
  # Instantiate a TfidfVectorizer object
  X = vectorizer.fit_transform(docs)
  # Convert the X as transposed matrix
  X = X.T.toarray()
  # Create a DataFrame and set the vocabulary as the index
  df = pd.DataFrame(X, index=vectorizer.get_feature_names())
  return df
TfIdf(fc)


def get_similar_articles(q, df):
    print("query:", q)
    print("Berikut artikel dengan nilai cosine similarity tertinggi: ")
    # Convert the query become a vector
    print()
    q = np.array([q])
    q_vec = vectorizer.transform(q).toarray().reshape(df.shape[0], )

    sim = []
    # Calculate the similarity
    for i in range(5):
        sim.append([i + 1, np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)])

    fileresult = open("hasilquery.txt", "a")
    fileresult.write("Hasil menggunakan TF-IDF\n")
    print("Hasil menggunakan TF-IDF\n")
    # Sort the values
    sim_sorted = sorted(sim, key=lambda x: x[1], reverse=True)
    # Print the articles and their similarity values
    for i in range(len(sim_sorted)):
        print(f"{i + 1}. text{sim_sorted[i][0]} = {sim_sorted[i][1]}\n")
        fileresult.write(f"{i + 1}. text{sim_sorted[i][0]} = {sim_sorted[i][1]}\n")

    fileresult.write("\n==========================================\n\n")
    fileresult.close()


# Add The Query
q1 = 'sistem pendukung keputusan'
# Call the function
get_similar_articles(q1, TfIdf(fc))