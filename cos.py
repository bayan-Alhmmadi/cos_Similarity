import numpy as np
import string

documents = [
    "Artificial intelligence is transforming industries and improving decision making.",
    "Football is one of the most popular sports in the world and has millions of fans.",
    "Climate change is a global challenge that requires urgent and collective action.",
    "Cooking healthy meals at home can save money and improve your lifestyle.",
    "Space exploration continues to inspire innovation and scientific discoveries."
]
 
filename =[f"doc{i+1}.txt"for i in range(len(documents))]
def clean_text(text):
    return text.lower().translate(str.maketrans('','',string.punctuation))

documents = [clean_text(doc) for doc in documents]

query = clean_text(input("Enter your query: "))
query_words = query.split()

def text_to_vector(text, words):
    vec = np.zeros(len(words))
    
    text_words = text.split()
    for i, word in enumerate(words):
        vec[i] = text_words.count(word)
    return vec
    
query_vector = np.ones(len(query_words))  
doc_vectors = np.array([text_to_vector(doc, query_words) for doc in documents])    

def cosine_similarity(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-10)

similarities = np.array([cosine_similarity(query_vector, doc_vec) for doc_vec in doc_vectors])

sorted_indices = similarities.argsort()[::-1]

print("Documents most similar to your query:")
found = False
for idx in sorted_indices[:5]:
    if similarities[idx] > 0:
        print(f"{filename[idx]} - similarity: {similarities[idx]:.3f}")
        found = True

if not found:
    print("No documents match your query.")


