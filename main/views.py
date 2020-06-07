from django.shortcuts import render

from random import randint

# Create your views here.
posts ={
'1':' System Design Interviews_ A step by step guide',
'2':' Designing a URL Shortening service like TinyURL',
'3':' Designing Pastebin',
'4':' Designing Instagram',
'5':' Designing Dropbox',
'6':' Designing Facebook Messenger',
'7':' Designing Twitter',
'8':' Designing Youtube or Netflix',
'9':' Designing Typeahead Suggestion',
'10':' Designing an API Rate Limiter',
'11':' Designing Twitter Search',
'12':' Designing a Web Crawler',
'13':' Designing Facebook’s Newsfeed',
'14':' Designing Yelp or Nearby Friends',
'15':' Designing Uber backend',
'16':' Design Ticketmaster',
'17':' Additional Resources',
        }

theory ={
'18':'. System Design Basics',
'19':'. Key Characteristics of Distributed Systems',
'20':'. Load Balancing',
'21':'. Caching',
'22':'. Data Partitioning',
'23':'. Indexes',
'24':'. Proxies',
'25':'. Redundancy and Replication',
'26':'. SQL vs. NoSQL',
'27':'. CAP Theorem',
'28':'. Consistent Hashing',
'29':'. Long-Polling vs WebSockets vs Server-Sent Events',
}

randomised={}
def home(request):
    for i in range(0,29):
        randomised[i]=random_number(3)
    context={'posts':posts,'theory':theory,'randomised':randomised}
    return render(request, 'home.html', context)

def resource_requested(request,pk):
    if(pk>16):
        return render(request,"b"+str(pk-16)+".html",{})
    return render(request, str(pk)+".html",{})




def random_number(length=3):
    """
    Create a random integer with given length.
    For a length of 3 it will be between 100 and 999.
    For a length of 4 it will be between 1000 and 9999.
    """
    return randint(10**(length-1), (10**(length)-1))