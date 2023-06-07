import speech_recognition as sr 
import spacy
from wordcloud import WordCloud
from nltk import FreqDist
import matplotlib.pyplot as plt
from textblob import TextBlob

r= sr.Recognizer()

nlp = spacy.load('pt_core_news_sm')

def capturar_audio():
    with sr.AudioFile('C:\\Users\\Daniel\\Documents\\Django\\mineracao\\seminario\\seminario\\audio-lpn.wav') as source:
        print('Analisando audio...')
        audio = r.record(source)
        try:
            text = r.recognize_google(audio, language= 'pt-BR')
            print('transcricao: '+ text)
            
            print('\n')
            
            doc= nlp(text)
            for token in doc:
                print("token: " + token.text)
                print("lema: " + token.lemma_)
                print("Cateforia: " + token.pos_)
                print("Dependencia: " + token.dep_)
            tokens = [token.text for token in doc if not token.is_stop]
            
            fdist = FreqDist(tokens)
            
            weights = {term: freq for term, freq in fdist.items()}
            
            print('\n')
            
            print(weights)
            
            wordcloud = WordCloud(width=800, height= 400, background_color='white').generate_from_frequencies(weights)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.show()
                
        except sr.UnknownValueError:
            print("não foi possível reconhecer fala")
        except sr.RequestError:
            print("não foi possivel transcrever")
        
capturar_audio()          