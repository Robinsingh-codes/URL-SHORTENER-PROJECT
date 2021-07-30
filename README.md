# URL-SHORTENER-PROJECT
Bitly URL Shortener
Bitly URL Shortener is very simple to use. You just need to make an account on Bitly.
 Then, go to Group Settings and click on Advanced settings. 
There you will find the API option. Since API is now depreciated, click on OAuth option. 
Then, generate the OAuth Token. Copy the token.
Now, install bitly_api. To do so, click on this link and download the repository.
 Then, unzip it and move inside the folder by doing:
cd bitly-api-python-master
Then, you would be inside the folder then you need to use the following command:
python setup.py install
Now, you are done with the installation work. The bitly_api is now installed on your machine.
 Now, let’s move to the real coding part which is very easy and is of few lines.

So, as you can see, it is very simple to do so. We need to import the bitly_api in our code first of all.
 Next, we need to put in the access token we generated earlier and call the connection with the access token in it.
Now, we need to ask for the link for the user.
 Next, we would simply shorten it by calling shorten function of the access created earlier by calling Connection.
Then, would print only the ‘url’ part of the short_url function.
 It also has various other info like hash, full link and other info which we really do not require.
And yes, we are done! It was so easy to use Bitly URL Shortener API to shorten links easily.

Get started
Open in app


Open in app


You have 2 free member-only stories left this month. Sign up for Medium and get an extra one

URL Shortener using Python
We will discuss and learn how to use various Python APIs to shorten URLs with only a few lines of code.
Kumar Shubham
Kumar Shubham

Nov 13, 2020·5 min read



Photo by Obi Onyeador on Unsplash
Hello Readers! So, you would have seen short URLs being used in various places (social media, websites, messaging platforms etc). Short URLs are easy to remember or type so they are very popular. No one loves long URLs and so the need to shorten lengthy URLs often come to us.
You would have personally used various URL shortening services online and they all do the job well! Even Google forms, LinkedIn etc. shortens the URLs for ease of use. So, it is a widely used thing on the internet.
So, have you ever thought or tried to make your own URL shortener? Hopefully, there are many libraries and APIs available to help us do the same programmatically without the need to visit any website and use anyone’s service.
We can write a program in Python language for our needs. Then we can give long URL as the input and we would get short URLs as output, that too in very few lines of code. Is not it exciting? The use of various APIs does it very easily without having to dig into complex topics.
So, there are various APIs available for doing this job, so let’s have a look at some of the APIs and let’s implement them and see how we can use them to shorten links.
Bitly URL Shortener
Bitly URL Shortener is very simple to use. You just need to make an account on Bitly. Then, go to Group Settings and click on Advanced settings. There you will find the API option. Since API is now depreciated, click on OAuth option. Then, generate the OAuth Token. Copy the token.
Now, install bitly_api. To do so, click on this link and download the repository. Then, unzip it and move inside the folder by doing:
cd bitly-api-python-master
Then, you would be inside the folder then you need to use the following command:
python setup.py install
Now, you are done with the installation work. The bitly_api is now installed on your machine. Now, let’s move to the real coding part which is very easy and is of few lines.

So, as you can see, it is very simple to do so. We need to import the bitly_api in our code first of all. Next, we need to put in the access token we generated earlier and call the connection with the access token in it.
Now, we need to ask for the link for the user. Next, we would simply shorten it by calling shorten function of the access created earlier by calling Connection.
Then, would print only the ‘url’ part of the short_url function. It also has various other info like hash, full link and other info which we really do not require.
And yes, we are done! It was so easy to use Bitly URL Shortener API to shorten links easily.


Cuttly URL Shortener
Cuttly URL Shortener is another fantastic URL shortener we can use. It is also pretty easy to use though requires 2–3 more lines of code but requires no installation so it is overall simpler.
First of all, move to Cuttly and sign up for a new account on it. Next, click on Edit Profile and click on Generate New API Keys. This would generate a new pair of API keys for us to use. Copy those API keys.
So, we can directly jump into code without caring to install anything. Though we need one simple installation I guess most of us already have that installed.
pip install requests
So, if you have not installed this simple library before, do it now. Next, let’s jump into the code for it.

So, as you can see we start by importing requests into our code. Next, we enter our API key. Then we ask the user for input URL. Also, we need to specify the api_url parameters. Then, we sent it to requests to get data.
If data is valid, then we take the shortLink part of the data which is the shortened URL and we print it. If invalid, we return an error.
pyshortener
pyshortener is a python module which can be used to use various URL shortener services using its access keys. We do not need to install separate libraries for different providers. For example, we can use Google URL shortener, Bitly shortener, Adf.ly shortener etc.
This also helps us to get the original URL back from the shortened URL. So, it serves a dual purpose.
To use any of the shortening services, we first need to sign up for that service and get its access token as we did in the last two ways.
Then, we need to install the python module for pyshorteners.

pip install pyshorteners

from pyshorteners import Shortener 
ACCESS_TOKEN = 'YOUR TOKEN'

# Shorten long URL
long_url = input()
url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN) 
print ("Short URL is {}".format(url_shortener.short(long_url)))

#Expand short URL
short_url = input()
url_expander = Shortener('Bitly', bitly_token = ACCESS_TOKEN)
print ("Long URL is {}".format(url_expander.expand(short_url))) 


We will use Bitly shortener for this example. We have already used Bitly but differently, so let’s try the same provider in this different way.
So, you can see below how easy it is to use pyshorteners module. It is incredibly easy and requires very few lines of code. Put the Access token you received in the Bitly OAuth. Then just input the link required to be shortened.

Also, as you can see, we can expand short links very easily too. Just input the short URL and use .expand to expand the short URl in the same way we used .short to shorten it.
So, in the same way, you can use various shortening service providers to do the same job.
So, I hope you learnt something new today and you would try some other URL providers like adf.ly, Google Shortener etc. You can also try various other complex things with this.
It is the basic part and the most important one. You can use this in your existing websites or apps too to enhance productivity or just play around with it to have some fun!
