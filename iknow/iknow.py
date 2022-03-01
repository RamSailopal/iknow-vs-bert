import iknowpy
import requests
from bs4 import BeautifulSoup
import re
from colorama import init, Fore, Style
import sys
if len(sys.argv) < 2:
   print("Please enter a Yelp review link to run the iKnow against")
   exit(1)
engine = iknowpy.iKnowEngine()
r = requests.get(sys.argv[1])
soup = BeautifulSoup(r.text, 'html.parser')
regex = re.compile('.*comment.*')
results = soup.find_all('p', {'class':regex})
reviews = [result.text for result in results]
t=0
print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tReview\tSentiment score\n")
for i in reviews:
   text=i
   conccnt=0
   negcnt=0
   sentcnt=0
   poscnt=0
   engine.index(text, 'en')
   for s in engine.m_index['sentences']:
      sentcnt=sentcnt+1
      for e in s['entities']:
         if (e['type']=="Concept"):
            conccnt=conccnt+1
      for a in s['path_attributes']:
         if a['type']=="NegativeSentiment":
            negcnt=negcnt+1
         elif a['type']=="PositiveSentiment":
            poscnt=poscnt+1
         for ent in range(s['path'][a['pos']], 
            s['path'][a['pos']+a['span']-1]+1):
               if a['type']=="Negation":
                  s['entities'][ent]['colour'] = Fore.RED

   totcnt=poscnt+negcnt
   perpos=((poscnt/totcnt)/2)*10
   print(str(t) + "\t" + text[0:50] + "...\t" + str("{:.2f}".format(perpos)))
   t=t+1

