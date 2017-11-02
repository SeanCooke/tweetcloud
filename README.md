# tweetcloud
Twitter word cloud generator which creates beautiful, colorful tweet visualizations for a given user.  Built for Python 2.7, [Python Twitter Tools 1.17.1](https://pypi.python.org/pypi/twitter) and [word\_cloud](https://github.com/amueller/word_cloud).

## Examples
`$ python tweetcloud.py text=@realDonaldTrump stopwords=stopwords-twitter.txt mask=trump.jpg color=1`
![tweetcloud made from @realDonaldTrump's recent tweets](https://github.com/SeanCooke/tweetcloud/blob/master/tweetcloud-trump.png?raw=true)
<br/>
`$ python tweetcloud.py text=alice.txt stopwords=stopwords-alice.txt mask=alice-color.png color=1`
![tweetcloud made from Lewis Carroll's Alice in Wonderland](https://github.com/SeanCooke/tweetcloud/blob/master/tweetcloud-alice.png?raw=true)
<br/>
`$ python tweetcloud.py text=@AdamSchefter stopwords=stopwords-twitter.txt color=0`
![tweetcloud made from @AdamSchefter's recent tweets](https://github.com/SeanCooke/tweetcloud/blob/master/tweetcloud-schefter.png?raw=true)

## Arguments
`$ python tweetcloud.py text={<@twitter_screen_name>, <.txt_file>} [stopwords=<.txt_file>] [mask=<mask_image>] [color={0, 1}] [max_font_size=[0-9]]`

### text
`text` is a mandatory command line agrument to tweetcloud.  When the `text` option begins with `@`, a twitter handle is assumed to be specified and the most recent tweets (up to 3,240) from that twitter user will be used to generate the tweetcloud.  Otherwise, the `text` option is assumed to be a file and the text from the file will be used to generate the tweetcloud.

### stopwords
`stopwords` is an optional command line argument.  The value to `stopwords` should be the location of a .txt file containing a list of words to be ignored by the tweetcloud, one word per line.  An example of can be found in [stopwords-twitter.txt](https://raw.githubusercontent.com/SeanCooke/tweetcloud/master/stopwords-twitter.txt)

### mask
`mask` is an optional command line argument.  The value to `mask` should be the location of an image file containing the desired shape of the tweetcloud.

### color
`color` is an optional command line argument only to be evaluated if `mask` is specified.  If `color=0`, `text` will be black.  If `color=1`, `text` will have colors from `mask`.

### max\_font\_size
`max_font_size` is an optional command line argument which must be a number and specifies the maximum font size used in the tweetcloud.

## Twitter Authentication
When the `text` option begins with `@` tweetcloud gets tweets from the specified user using API tokens associated with a twitter application.  [Click here](https://apps.twitter.com/app/new) to create a set of application keys associated with a Twitter account.  Variables `ACCESS_TOKEN`, `ACCESS_SECRET`, `CONSUMER_KEY`, and `CONSUMER_SECRET` in [tweetcloud.py](https://raw.githubusercontent.com/SeanCooke/tweetcloud/master/tweetcloud.py) must be customized with appropriate application keys.
