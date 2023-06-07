import nltk

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def gerar_nuvem_palavras(texto):
    tokens = word_tokenize(texto)
    
    stop_words = set(stopwords.words('portuguese'))
    
    palavras_sem_stopwords = [word for word in tokens if word.lower() not in stop_words]
    
    texto_sem_stopwords = ''.join(palavras_sem_stopwords)
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_sem_stopwords)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
with open('C:\\Users\\Daniel\\Documents\\Django\\mineracao\\seminario\\seminario\\Todos os trabalhos', 'r', encoding= 'utf-8') as file:
    texto = file.read()
gerar_nuvem_palavras(texto)