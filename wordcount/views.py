from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
  return render(request,'neon.html')

def abhi(request):
  return render(request,'abhi.html') 
  
def aboutus(request):
  return render(request,'aboutus.html')  

def count(request):

  fulltext =request.GET['Fulltext']
  wordlist=fulltext.split(" ")
  worddictionary={}

  for word in wordlist:
    if word in worddictionary:
       worddictionary[word] +=1
    else:
      worddictionary[word]=1  

  sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
  
  return render(request,'count.html',{'Fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})




