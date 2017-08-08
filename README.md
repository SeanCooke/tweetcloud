# tweetcloud

A Twitter Wordcloud generator built for Python 2.7, Python Twitter Tools 1.17.1 and word\_cloud. Variables 'ACCESS\_TOKEN', 'ACCESS\_SECRET', 'CONSUMER\_KEY', and 'CONSUMER\_SECRET' must be customized.

## Examples
`$ python tweetcloud.py text=@realDonaldTrump stopwords=stopwords-trump.txt mask=trump.jpg color=1`
![tweetcloud made from @realDonaldTrump's recent tweets](https://raw.githubusercontent.com/SeanCooke/tweetcloud/tweetcloud-trump.png)
`$ python tweetcloud.py text=alice.txt stopwords=stopwords-alice.txt mask=alice-color.png color=1`
![tweetcloud made from Lewis Carroll's Alice in Wonderland](https://raw.githubusercontent.com/SeanCooke/tweetcloud/tweetcloud-alice.png)
