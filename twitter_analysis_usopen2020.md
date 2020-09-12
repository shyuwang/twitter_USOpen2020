In this project, I obtained realtime tweets using [python-twitter](https://github.com/bear/python-twitter) wrapper, and then processed the tweets using Apache Spark Streaming to identify mentioned users with search keyword *USOpen*, and finally returned top 20 popular mentioned users and visualized them with bar plots.


## 1. Obtain realtime tweets from Twitter
### Step 1.1 Apply for Twitter developer account

Upgrade Twitter account to developer account on [apps.twitter](https://apps.twitter.com/) and create an app to get the consumer keys and authentication tokens.

### Step 1.2 Install the python-twitter wrapper

With the keys and tokens of newly created Twitter App and the help of [python-twitter](https://github.com/bear/python-twitter) wrapper, I easily extracted the tweet text from Twitter and sent the information to Spark via TCP connection using Python Socket package. (For [official document](https://docs.python.org/3/library/socket.html) of Socket, for [brief introduction](https://zhuanlan.zhihu.com/p/39982451).)


## 2. Establish Apache Spark Streaming application

As a powerful big data tool, Spark is able to process the realtime stream data and transform it to get the information we need. More specifically, I used Spark to receive the tweets and extract the user (the word begin with **@**, excluding the keyword itself), and calculate the number of times a user was mentioned. 



## 3. Analyze data
USOpen is one of the major tennis championships in the year. Due to the COVID-19 pandemic, USOpen 2020 is held in Flushing, New York with no audience at present. People watch the matches through online platform. One of the ways to capture the trending of the game is via Twitter. Therefore, I set up the realtime data gathering and transformation pipeline to see the up-trending players as the game proceeds.


### 2020-09-10 17:00, after Men’s Doubles Final

Mate Pavia & Bruno Soares defeat Koolhof & Mektic in the game. It is their first Grand Slam title together. As is shown in the barplot, **@brunosoares82**, the Twitter account for Bruno Soares is quite popular at the time when the code was run. Mate Pavia doesn’t have Twitter account, so he is not shown in the top mentioned Twitter user. 

As Women’s Singles Semifinals are to be on at the same day at 19:00, the candidates Naomi Osaka (No.4 seed, **@naomiosaka**) and Serena Williams (No.3 seed, **@serenawilliams**) are also popular.

![](/images/0910-17.gif)



### 2020-09-10 21:30, after Women’s Single Semifinal -1
Naomi Osaka beats Jennifer Brady. This is an exciting and fantastic match, with a tied at the first set. This is Osaka’s 3rd career Grand Slam final. People are thrilled at the result and looking forward to seeing her in the final. The strong support for Osaka could be seen from the number of times her Twitter account is mentioned after the semifinal.

![](/images/0910-21.gif)



### 2020-09-11 00:00, after Women’s Single Semifinal -2

This is Victoria Azarenka’s (**@vika7**) first major final in seven years! She beats Serena Williams with 1-6, 6-3, 6-3. I watch this match in live stream, and Azarenka is so impressive! Although people hate to see Serena lose the match, they are glad to see Azarenka doing well again and going to the final of the USOpen from unseeded. Azarenka will battle Osaka in the Women’s Single Final, and the match would be so much fun because the two player are former finalist and former champion, respectively. Therefore, **@vika7**, **@serenawilliams**, **@naomiosaka** are top-trending after this semifinal. By the way, **@espn** is also mentioned so many times because it is the media that provides live stream service and people re-tweet its tweet after it announces the victory of Azarenka. 

![](/images/0911-00.gif)


### 2020-09-11 15:00, after Women’s Doubles Final and before Men’s Single Semifinals
Laura Siegemund (**@laurasiegemund**) and Vera Zvonareva (**@verazvonareva**) win Women’s Doubles Final and have their first Grand Slam together. Their Twitter accounts are mentioned multiple times and are shown in the bar plots. However, the accounts that are more popular are Mariah Carey (**@mariahcarey**) who will perform SAVE THE DAY tomorrow at the Women’s Single Finals, Dominic Thiem (No.2 seed, **@theimdomi**),  Pablo Carreno Busta (No.20 seed, **@pablocarreno91**), Daniil Medvedev (No.3 seed, **@daniilmedwed**) who will compete in the Men’s Single Semifinals an hour later. It suggests that people are likely to pay more attention to Men’s Single Semifinals, and Mariah Carey than the Women’s Doubles Final. 

![](/images/0911-15.gif)

### 2020-09-11 19:50, after Men’s Single Semifinal -1
Alexander Zverev defeats Pablo Carreno Busta and enters into his first Grand Slam final. He is the youngest Grand Slam finalist since Novak Djokovic at the 2010 UsOpen, and he is also the first German Grand Slam finalist since 2003. This is so impressive! The match is unbelievable because he rallies from two sets down to reach the win. The impressiveness could also be seen from the number of times **@alexzverev** is mentioned. 

![](/images/0911-20.gif)


### 2020-09-11 23:00, after Men’s Single Semifinal -2
Dominic Thiem is into the USOpen final for the first time in his career, making history for Austrian tennis. What a rally! It is an absolute battle in the match, which can be captured by the mentioned times of **@theimdomi**. Let’s get excited about the final between Dominic Thiem and Alexander Zverev.

![](/images/0911-23.gif)

### 2020-09-12 18:15, after Women’s Single Final
Congratulations on Osaka! It is a hard-fought final and Osaka completes an impressive USOPen with a 1-6, 6-3, 6-3. People are thrilled at the final and it is demonstrated by the large amount of times @naomiosaka is mentioned.

![](/images/0912-18.gif)