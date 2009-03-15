#!/usr/bin/python

from reverend.thomas import Bayes

class ComaTokenizer:
  """A simple regex-based coma tokenizer.
    It expects a string and can return all tokens lower-cased
    or in their existing case.
    """
  def __init__(self, lower=False):
     self.lower = lower

  def tokenize(self, obj):
    for match in obj.split(','):
      match = match.strip()
      if self.lower:
        yield match.lower()
      else:
        yield match
      print match

class ComaTrainedBayes(Bayes):
  _coma_tokenizer = ComaTokenizer()

  def getTokens(self, obj):
    return self._coma_tokenizer.tokenize(obj)

POSITIVE = "pos"
NEGATIVE = "neg"
NEUTRAL  = "neu"

class BayesianClassifier:

  POSITIVE = POSITIVE
  NEGATIVE = NEGATIVE
  NEUTRAL  = NEUTRAL

  THRESHHOLD = 0.1
  guesser = None

  def __init__(self):
    self.guesser = Bayes()
    self.train()

  def train(self):
    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "Woo")
    self.guesser.train(POSITIVE, "quite amazing")
    self.guesser.train(POSITIVE, "thks")
    self.guesser.train(POSITIVE, "looking forward to")
    self.guesser.train(POSITIVE, "damn good")
    self.guesser.train(POSITIVE, "frickin ruled")
    self.guesser.train(POSITIVE, "frickin rules")
    self.guesser.train(POSITIVE, "Way to go")
    self.guesser.train(POSITIVE, "cute")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "not suck")
    self.guesser.train(POSITIVE, "prop")
    self.guesser.train(POSITIVE, "kinda impressed")
    self.guesser.train(POSITIVE, "props")
    self.guesser.train(POSITIVE, "come on")
    self.guesser.train(POSITIVE, "congratulation")
    self.guesser.train(POSITIVE, "gtd")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "can help")
    self.guesser.train(POSITIVE, "thanks!")
    self.guesser.train(POSITIVE, "pumped")
    self.guesser.train(POSITIVE, "integrate")
    self.guesser.train(POSITIVE, "really like")
    self.guesser.train(POSITIVE, "loves it")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "amazing")
    self.guesser.train(POSITIVE, "epic flail")
    self.guesser.train(POSITIVE, "flail")
    self.guesser.train(POSITIVE, "good luck")
    self.guesser.train(POSITIVE, "fail")
    self.guesser.train(POSITIVE, "life saver")
    self.guesser.train(POSITIVE, "piece of cake")
    self.guesser.train(POSITIVE, "good thing")
    self.guesser.train(POSITIVE, "hawt")
    self.guesser.train(POSITIVE, "hawtness")
    self.guesser.train(POSITIVE, "highly positive")
    self.guesser.train(POSITIVE, "my hero")
    self.guesser.train(POSITIVE, "yummy")
    self.guesser.train(POSITIVE, "awesome")
    self.guesser.train(POSITIVE, "congrats")
    self.guesser.train(POSITIVE, "would recommend")
    self.guesser.train(POSITIVE, "intellectual vigor")
    self.guesser.train(POSITIVE, "really neat")
    self.guesser.train(POSITIVE, "yay")
    self.guesser.train(POSITIVE, "ftw")
    self.guesser.train(POSITIVE, "I want")
    self.guesser.train(POSITIVE, "best looking")
    self.guesser.train(POSITIVE, "imrpessive")
    self.guesser.train(POSITIVE, "positive")
    self.guesser.train(POSITIVE, "thx")
    self.guesser.train(POSITIVE, "thanks")
    self.guesser.train(POSITIVE, "thank you")
    self.guesser.train(POSITIVE, "endorse")
    self.guesser.train(POSITIVE, "clearly superior")
    self.guesser.train(POSITIVE, "superior")
    self.guesser.train(POSITIVE, "really love")
    self.guesser.train(POSITIVE, "woot")
    self.guesser.train(POSITIVE, "w00t")
    self.guesser.train(POSITIVE, "super")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "leaning towards")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "incredible")
    self.guesser.train(POSITIVE, "the best")
    self.guesser.train(POSITIVE, "is the best")
    self.guesser.train(POSITIVE, "strong")
    self.guesser.train(POSITIVE, "would love")
    self.guesser.train(POSITIVE, "rally")
    self.guesser.train(POSITIVE, "very quickly")
    self.guesser.train(POSITIVE, "very cool")
    self.guesser.train(POSITIVE, "absolutely love")
    self.guesser.train(POSITIVE, "very exceptional")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "recommend")
    self.guesser.train(POSITIVE, "so proud")
    self.guesser.train(POSITIVE, "so great")
    self.guesser.train(POSITIVE, "so cool")
    self.guesser.train(POSITIVE, "cool")
    self.guesser.train(POSITIVE, "wowsers")
    self.guesser.train(POSITIVE, "plus")
    self.guesser.train(POSITIVE, "liked it")
    self.guesser.train(POSITIVE, "make a difference")
    self.guesser.train(POSITIVE, "moves me")
    self.guesser.train(POSITIVE, "inspired")
    self.guesser.train(POSITIVE, "OK")
    self.guesser.train(POSITIVE, "love it")
    self.guesser.train(POSITIVE, "LOL")
    self.guesser.train(POSITIVE, ":)")
    self.guesser.train(POSITIVE, ";)")
    self.guesser.train(POSITIVE, ":-)")
    self.guesser.train(POSITIVE, ";-)")
    self.guesser.train(POSITIVE, ":D")
    self.guesser.train(POSITIVE, ";]")
    self.guesser.train(POSITIVE, ":]")
    self.guesser.train(POSITIVE, ":p")
    self.guesser.train(POSITIVE, ";p")
    self.guesser.train(POSITIVE, "voting for")
    self.guesser.train(POSITIVE, "great")
    self.guesser.train(POSITIVE, "agreeable")
    self.guesser.train(POSITIVE, "amused")
    self.guesser.train(POSITIVE, "brave")
    self.guesser.train(POSITIVE, "calm")
    self.guesser.train(POSITIVE, "charming")
    self.guesser.train(POSITIVE, "cheerful")
    self.guesser.train(POSITIVE, "comfortable")
    self.guesser.train(POSITIVE, "cooperative")
    self.guesser.train(POSITIVE, "courageous")
    self.guesser.train(POSITIVE, "delightful")
    self.guesser.train(POSITIVE, "determined")
    self.guesser.train(POSITIVE, "eager")
    self.guesser.train(POSITIVE, "elated")
    self.guesser.train(POSITIVE, "enchanting")
    self.guesser.train(POSITIVE, "encouraging")
    self.guesser.train(POSITIVE, "energetic")
    self.guesser.train(POSITIVE, "enthusiastic")
    self.guesser.train(POSITIVE, "excited")
    self.guesser.train(POSITIVE, "exuberant")
    self.guesser.train(POSITIVE, "excellent")
    self.guesser.train(POSITIVE, "I like")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "fair")
    self.guesser.train(POSITIVE, "faithful")
    self.guesser.train(POSITIVE, "fantastic")
    self.guesser.train(POSITIVE, "fine")
    self.guesser.train(POSITIVE, "friendly")
    self.guesser.train(POSITIVE, "fun ")
    self.guesser.train(POSITIVE, "funny")
    self.guesser.train(POSITIVE, "gentle")
    self.guesser.train(POSITIVE, "glorious")
    self.guesser.train(POSITIVE, "good")
    self.guesser.train(POSITIVE, "pretty good")
    self.guesser.train(POSITIVE, "happy")
    self.guesser.train(POSITIVE, "healthy")
    self.guesser.train(POSITIVE, "helpful")
    self.guesser.train(POSITIVE, "high")
    self.guesser.train(POSITIVE, "agile")
    self.guesser.train(POSITIVE, "responsive")
    self.guesser.train(POSITIVE, "hilarious")
    self.guesser.train(POSITIVE, "jolly")
    self.guesser.train(POSITIVE, "joyous")
    self.guesser.train(POSITIVE, "kind")
    self.guesser.train(POSITIVE, "lively")
    self.guesser.train(POSITIVE, "lovely")
    self.guesser.train(POSITIVE, "lucky")
    self.guesser.train(POSITIVE, "nice")
    self.guesser.train(POSITIVE, "nicely")
    self.guesser.train(POSITIVE, "obedient")
    self.guesser.train(POSITIVE, "perfect")
    self.guesser.train(POSITIVE, "pleasant")
    self.guesser.train(POSITIVE, "proud")
    self.guesser.train(POSITIVE, "relieved")
    self.guesser.train(POSITIVE, "silly")
    self.guesser.train(POSITIVE, "smiling")
    self.guesser.train(POSITIVE, "splendid")
    self.guesser.train(POSITIVE, "successful")
    self.guesser.train(POSITIVE, "thankful")
    self.guesser.train(POSITIVE, "thoughtful")
    self.guesser.train(POSITIVE, "victorious")
    self.guesser.train(POSITIVE, "vivacious")
    self.guesser.train(POSITIVE, "witty")
    self.guesser.train(POSITIVE, "wonderful")
    self.guesser.train(POSITIVE, "zealous")
    self.guesser.train(POSITIVE, "zany")
    self.guesser.train(POSITIVE, "rocks")
    self.guesser.train(POSITIVE, "comeback")
    self.guesser.train(POSITIVE, "pleasantly surprised")
    self.guesser.train(POSITIVE, "pleasantly")
    self.guesser.train(POSITIVE, "surprised")
    self.guesser.train(POSITIVE, "love")
    self.guesser.train(POSITIVE, "glad")
    self.guesser.train(POSITIVE, "yum")
    self.guesser.train(POSITIVE, "interesting")



    self.guesser.train(NEGATIVE, "FTL")
    self.guesser.train(NEGATIVE, "irritating")
    self.guesser.train(NEGATIVE, "not that good")
    self.guesser.train(NEGATIVE, "suck")
    self.guesser.train(NEGATIVE, "lying")
    self.guesser.train(NEGATIVE, "duplicity")
    self.guesser.train(NEGATIVE, "angered")
    self.guesser.train(NEGATIVE, "dumbfounding")
    self.guesser.train(NEGATIVE, "dumbifying")
    self.guesser.train(NEGATIVE, "not as good")
    self.guesser.train(NEGATIVE, "not impressed")
    self.guesser.train(NEGATIVE, "stomach it")
    self.guesser.train(NEGATIVE, "pw")
    self.guesser.train(NEGATIVE, "pwns")
    self.guesser.train(NEGATIVE, "pwnd")
    self.guesser.train(NEGATIVE, "pwning")
    self.guesser.train(NEGATIVE, "in a bad way")
    self.guesser.train(NEGATIVE, "horrifying")
    self.guesser.train(NEGATIVE, "wrong")
    self.guesser.train(NEGATIVE, "flailing")
    self.guesser.train(NEGATIVE, "failing")
    self.guesser.train(NEGATIVE, "fallen way behind")
    self.guesser.train(NEGATIVE, "fallen behind")
    self.guesser.train(NEGATIVE, "lose")
    self.guesser.train(NEGATIVE, "fallen")
    self.guesser.train(NEGATIVE, "self-deprecating")
    self.guesser.train(NEGATIVE, "hunker down")
    self.guesser.train(NEGATIVE, "duh")
    self.guesser.train(NEGATIVE, "get killed by")
    self.guesser.train(NEGATIVE, "got killed by")
    self.guesser.train(NEGATIVE, "hated us")
    self.guesser.train(NEGATIVE, "only works in safari")
    self.guesser.train(NEGATIVE, "must have ie")
    self.guesser.train(NEGATIVE, "fuming and frothing")
    self.guesser.train(NEGATIVE, "heavy")
    self.guesser.train(NEGATIVE, "buggy")
    self.guesser.train(NEGATIVE, "unusable")
    self.guesser.train(NEGATIVE, "nothing is")
    self.guesser.train(NEGATIVE, "is great until")
    self.guesser.train(NEGATIVE, "don't support")
    self.guesser.train(NEGATIVE, "despise")
    self.guesser.train(NEGATIVE, "pos")
    self.guesser.train(NEGATIVE, "hindrance")
    self.guesser.train(NEGATIVE, "sucks")
    self.guesser.train(NEGATIVE, "problems")
    self.guesser.train(NEGATIVE, "not working")
    self.guesser.train(NEGATIVE, "fuming")
    self.guesser.train(NEGATIVE, "annoying")
    self.guesser.train(NEGATIVE, "frothing")
    self.guesser.train(NEGATIVE, "poorly")
    self.guesser.train(NEGATIVE, "headache")
    self.guesser.train(NEGATIVE, "completely wrong")
    self.guesser.train(NEGATIVE, "sad news")
    self.guesser.train(NEGATIVE, "didn't last")
    self.guesser.train(NEGATIVE, "lame")
    self.guesser.train(NEGATIVE, "pet peeves")
    self.guesser.train(NEGATIVE, "pet peeve")
    self.guesser.train(NEGATIVE, "can't send")
    self.guesser.train(NEGATIVE, "bullshit")
    self.guesser.train(NEGATIVE, "fail")
    self.guesser.train(NEGATIVE, "so terrible")
    self.guesser.train(NEGATIVE, "negative")
    self.guesser.train(NEGATIVE, "anooying")
    self.guesser.train(NEGATIVE, "an issue")
    self.guesser.train(NEGATIVE, "drop dead")
    self.guesser.train(NEGATIVE, "trouble")
    self.guesser.train(NEGATIVE, "brainwashed")
    self.guesser.train(NEGATIVE, "smear")
    self.guesser.train(NEGATIVE, "commie")
    self.guesser.train(NEGATIVE, "communist")
    self.guesser.train(NEGATIVE, "anti-women")
    self.guesser.train(NEGATIVE, "WTF")
    self.guesser.train(NEGATIVE, "anxiety")
    self.guesser.train(NEGATIVE, "STING")
    self.guesser.train(NEGATIVE, "nobody spoke")
    self.guesser.train(NEGATIVE, "yell")
    self.guesser.train(NEGATIVE, "Damn")
    self.guesser.train(NEGATIVE, "aren't")
    self.guesser.train(NEGATIVE, "anti")
    self.guesser.train(NEGATIVE, "i hate")
    self.guesser.train(NEGATIVE, "hate")
    self.guesser.train(NEGATIVE, "dissapointing")
    self.guesser.train(NEGATIVE, "doesn't recommend")
    self.guesser.train(NEGATIVE, "the worst")
    self.guesser.train(NEGATIVE, "worst")
    self.guesser.train(NEGATIVE, "expensive")
    self.guesser.train(NEGATIVE, "crap")
    self.guesser.train(NEGATIVE, "socialist")
    self.guesser.train(NEGATIVE, "won't")
    self.guesser.train(NEGATIVE, "wont")
    self.guesser.train(NEGATIVE, ":(")
    self.guesser.train(NEGATIVE, ":-(")
    self.guesser.train(NEGATIVE, "Thanks")
    self.guesser.train(NEGATIVE, "smartass")
    self.guesser.train(NEGATIVE, "don't like")
    self.guesser.train(NEGATIVE, "too bad")
    self.guesser.train(NEGATIVE, "frickin")
    self.guesser.train(NEGATIVE, "snooty")
    self.guesser.train(NEGATIVE, "knee jerk")
    self.guesser.train(NEGATIVE, "jerk")
    self.guesser.train(NEGATIVE, "reactionist")
    self.guesser.train(NEGATIVE, "MUST DIE")
    self.guesser.train(NEGATIVE, "no more")
    self.guesser.train(NEGATIVE, "hypocrisy")
    self.guesser.train(NEGATIVE, "ugly")
    self.guesser.train(NEGATIVE, "too slow")
    self.guesser.train(NEGATIVE, "not reliable")
    self.guesser.train(NEGATIVE, "noise")
    self.guesser.train(NEGATIVE, "crappy")
    self.guesser.train(NEGATIVE, "horrible")
    self.guesser.train(NEGATIVE, "bad quality")
    self.guesser.train(NEGATIVE, "angry")
    self.guesser.train(NEGATIVE, "annoyed")
    self.guesser.train(NEGATIVE, "anxious")
    self.guesser.train(NEGATIVE, "arrogant")
    self.guesser.train(NEGATIVE, "ashamed")
    self.guesser.train(NEGATIVE, "awful")
    self.guesser.train(NEGATIVE, "bad")
    self.guesser.train(NEGATIVE, "bewildered")
    self.guesser.train(NEGATIVE, "blues")
    self.guesser.train(NEGATIVE, "bored")
    self.guesser.train(NEGATIVE, "clumsy")
    self.guesser.train(NEGATIVE, "combative")
    self.guesser.train(NEGATIVE, "condemned")
    self.guesser.train(NEGATIVE, "confused")
    self.guesser.train(NEGATIVE, "crazy")
    self.guesser.train(NEGATIVE, "flipped-out")
    self.guesser.train(NEGATIVE, "creepy")
    self.guesser.train(NEGATIVE, "cruel")
    self.guesser.train(NEGATIVE, "dangerous")
    self.guesser.train(NEGATIVE, "defeated")
    self.guesser.train(NEGATIVE, "defiant")
    self.guesser.train(NEGATIVE, "depressed")
    self.guesser.train(NEGATIVE, "disgusted")
    self.guesser.train(NEGATIVE, "disturbed")
    self.guesser.train(NEGATIVE, "dizzy")
    self.guesser.train(NEGATIVE, "dull")
    self.guesser.train(NEGATIVE, "embarrassed")
    self.guesser.train(NEGATIVE, "envious")
    self.guesser.train(NEGATIVE, "evil")
    self.guesser.train(NEGATIVE, "fierce")
    self.guesser.train(NEGATIVE, "foolish")
    self.guesser.train(NEGATIVE, "frantic")
    self.guesser.train(NEGATIVE, "frightened")
    self.guesser.train(NEGATIVE, "grieving")
    self.guesser.train(NEGATIVE, "grumpy")
    self.guesser.train(NEGATIVE, "helpless")
    self.guesser.train(NEGATIVE, "homeless")
    self.guesser.train(NEGATIVE, "hungry")
    self.guesser.train(NEGATIVE, "hurt")
    self.guesser.train(NEGATIVE, "ill")
    self.guesser.train(NEGATIVE, "itchy")
    self.guesser.train(NEGATIVE, "jealous")
    self.guesser.train(NEGATIVE, "jittery")
    self.guesser.train(NEGATIVE, "lazy")
    self.guesser.train(NEGATIVE, "lonely")
    self.guesser.train(NEGATIVE, "mysterious")
    self.guesser.train(NEGATIVE, "nasty")
    self.guesser.train(NEGATIVE, "rape")
    self.guesser.train(NEGATIVE, "naughty")
    self.guesser.train(NEGATIVE, "nervous")
    self.guesser.train(NEGATIVE, "nutty")
    self.guesser.train(NEGATIVE, "obnoxious")
    self.guesser.train(NEGATIVE, "outrageous")
    self.guesser.train(NEGATIVE, "panicky")
    self.guesser.train(NEGATIVE, "fucking up")
    self.guesser.train(NEGATIVE, "repulsive")
    self.guesser.train(NEGATIVE, "scary")
    self.guesser.train(NEGATIVE, "selfish")
    self.guesser.train(NEGATIVE, "sore")
    self.guesser.train(NEGATIVE, "tense")
    self.guesser.train(NEGATIVE, "terrible")
    self.guesser.train(NEGATIVE, "testy")
    self.guesser.train(NEGATIVE, "thoughtless")
    self.guesser.train(NEGATIVE, "tired")
    self.guesser.train(NEGATIVE, "troubled")
    self.guesser.train(NEGATIVE, "upset")
    self.guesser.train(NEGATIVE, "uptight")
    self.guesser.train(NEGATIVE, "weary")
    self.guesser.train(NEGATIVE, "wicked")
    self.guesser.train(NEGATIVE, "worried")
    self.guesser.train(NEGATIVE, "is a fool")
    self.guesser.train(NEGATIVE, "painful")
    self.guesser.train(NEGATIVE, "pain")
    self.guesser.train(NEGATIVE, "gross")

  def classify(self, sentence):
    guess = self.guesser.guess(sentence)
    if len(guess) == 0:
      return NEUTRAL

    if len(guess) == 1:
      (sentiment, probabitily) = guess[0]
      return sentiment

    (max_sentiment, max_value) = guess[0]
    (min_sentiment, min_value) = guess[1]
    if max_value - min_value > self.THRESHHOLD:
      return max_sentiment

    return NEUTRAL







s = ["RT @richdemuro: Experiment - Add your own on-screen annotations to this Synched Up episode on YouTube http://bit.ly/185u14",
    "Experiment - Add your own on-screen annotations to this Synched Up episode on YouTube: http://bit.ly/ieEmr",
    "FYI: You have to have a YouTube account to add annotations: http://tinyurl.com/dkagcb",
    "According to YouTube, you can add annotations if we send you this: http://tinyurl.com/dkagcb. That's cool.",
    "Using adblock to block youtube annotations: http://bit.ly/bZZuC",
    "Playing with YouTube's annotations. http://tinyurl.com/b6el8m",
    "dear youtube: please give me a way to completely disable annotations from *all* videos. I really don't want to ever see them. ever.",
    "Does anyone else see YouTube annotations and think Pop-Up Video?",
    "Ive added annotations to the Big Switch ad on youtube so everyone can see where the switches are http://tinyurl.com/aqnrd9",
    "Thanks to everyone who entered the competition, will update the ad on youtube with annotations showing every switch.. :-)",
    "@darraghdoyle ill add annotations to the Youtube video later with all switch locations as confirmed by the post production people..",
    "YouTube: MAC Style warrior: cant wait!!! ill add annotations later MUSIC: Be next to ya .. http://tinyurl.com/dymx68",
    "New video tutorial tomorrow, this time on YouTube annotations! xoxo",
    "weird one...can you think of a youtube video with clickable links and annotations in?",
    "This is so great! YouTube choose your own adventure - http://bit.ly/fWvFo - great to see people starting to have fun with annotations",
    "Barack Paper Scissors... Great use of YouTube annotations. Check it out http://tinyurl.com/6abodj",
    "@bluemistanime Since when did the YouTube get Nico-esque user-submitted annotations?",
    "I think the worst invention of all time is youtube annotations. I wish you had the option of turning them off.",
    "on this dam Youtube... tryna fix annotations on the OFFICIAL ACK A AZZ Video... aint seen it yet then hurr ya go http://bit.ly/yobyy",
    "New YouTube video online. Adding annotations took a while. Yeah, yeah, I know what you're thinking. But trust me on this. http://bit.ly/4nn0",
    "Crysis vs YouTube Annotations: http://tinyurl.com/dhgbho",
    "@chrispirillo in regards to the annotations on the youtube video: Turn the annotations off and you look like you're going crazy",
    "@chrispirillo Your youtube video maxed out on annotations, well done :D",
    "@AlexaRPD i <3 oprah LOL tyra not so much. but yeah i think the video is on youtube & it has all these anti-porn annotations on it",
    "Has anyone used the new 'Annotations' and / or 'Audioswap' features in their YouTube videos yet? I'm thinking of having a play next week...",
    "Patrick Boivin creates a stop motion 'Bboy Joker' game using YouTube annotations: http://is.gd/k6cN Watch the making too: http://is.gd/me0k",
    "Hmm...seems the annotations editor on @youtube is unfunctioning...not cool.",
    "YouTube annotations are great for linking to and from your other videos and playlists, but it's such a hassle to set up on ALL your vids.",
    "I hate the in-player ads and annotations on YouTube. Useless and annoying.",
    "Annotations on YouTube: Is there anything more annoying? Worse is that you can only disable them by signing in.",
    "How did the anonymous annotations idea get past Youtube's drawing room?",
    "@brendanwenzel its kind of like youtube annotations it makes things more interesting!",
    "The FUTURE of YouTube - Collaborative Annotations: http://tinyurl.com/c7ohw6 :-)",
    "YOUTUBE BUSTING UPDATE: To remove BOTH titling/rating & pop-up annotations enter this after url in embed code: &showinfo=0&iv_load_policy=3",
    "dear YouTube, please remember my preference to NEVER view annotations on top of a video. Not a fan, never will be.",
    "Mario slots! Copyrighthater continues to innovate with YouTube annotations. http://tinyurl.com/cx3cv8",
    "Reading: Super Mario Slots Youtube Interactive: Wow this is really cool use of Youtube annotations. What a blast.. http://bit.ly/Wzr4e",
    "mwahahah, just discovered youtube annotations link tool",
    "YouTube video annotations are on my list of 'The 10 Most Annoying Things Ever'",
    "any good links about annotations on YouTube vids? why you should, benefits etc?",
    "Am I the only one who really hates the new colored annotations on YouTube???????",
    "My 2 vids NOW have awesome annotations! Rewatch em & check em out http://www.youtube.com/blakevjones",
    "seriously annotations on youtube was the worst thing they've ever done.",
    "http://bit.ly/OxrEd -- I use YouTube video annotations to break down that DS-10 track I posted earlier.",
    "wow youtube's annotations has real possibilities. if only i had the time to explore them today... still kewl annotation finally happening!!",
    "@dirkthecow Interesting post about YouTube annotations. Unrelated: Hello, Dirk. Hope this 'hello' finds you well.",
    "blogoscoped: How to Turn Off YouTube Annotations http://tinyurl.com/cheumd - http://twitter.com/blogoscoped/statuses/1232348103",
    "Thinks YouTube still annotations from fammilys whats what addition things",
    "New YouTube feature: 'Invite others to add annotations'. On MY videos?!? Uh, no. Hell no.",
    "Just added the missing annotations to all the videos at YouTube. Hope we attract more visitors. Keep checking out www.zstudios.net!",
    "YouTube collaborative annotations have given me an idea.",
    "http://twurl.nl/vqe51k Batman versus the Joker - Breakdance competitie met YouTube annotations",
    "Youtube annotations can be a little annoying at times. Specially when they are shown throughout a (music) video. Turning it off.",
    "New on YouTube: Collaborative Annotations http://tinyurl.com/b4nasw",
    "RT @lithium Blog Post: Malware in Social http://bit.ly/mwsm - youtube annotations take punters to malware. New patform - old tricks",
    "ugh - it appears Omnisio functionality is totally gone. annotations in YouTube aren't the same. anyone know of this functionality elsewhere?",
    "collaborative annotations on youtube! sounds messy but also interesting",
    "Barack, Paper, Scissors is the Most Ingenious Thing on YouTube: It turns out YouTube Annotations are useful for .. http://tinyurl.com/bjv67z",
    "You can now add annotations on other people's YouTube Videos! YouTubeYouWin! http://is.gd/kiKL",
    "Having fun with YouTube annotations: http://www.youtube.com/awiezbowski",
    "YouTube annotations look so much better now. Thoughts?",
    "Tip - How to Turn Off YouTube Annotations - http://tinyurl.com/cheumd",
    "I just added annotations to somebody else's video on youtube.",
    "RT @UrbanLifestyle YouTube introduces new features: Collaborative Annotations http://snurl.com/cmeqy",
    "YouTube introduces new features: Collaborative Annotations http://snurl.com/cmeqy",
    "annotations may be the downfall of youtube - please get rid of the misused annoyance ASAP #fail",
    "RT @ChrisWexler: -- Something I've been working on for MSFT -- check it out -- good use of annotations YouTube... http://tinyurl.com/cmzpvg",
    "-- Something I've been working on for MSFT -- check it out -- good use of annotations on YouTube... http://tinyurl.com/cmzpvg",
    "Blogoscoped: How to Turn Off YouTube Annotations: YouTube annotations are the text overlays on YouTu.. http://tinyurl.com/cheumd",
    "I break down YouTube Collaborative Annotations: http://bit.ly/puwCoGet Excited !",
    "@KevinCross + one can rip the video through uStream ... you could do it. Dub it or youtube it (with annotations etc) and stuff",
    "since when r there colored annotations on youtube? i like it"]


#classifier = BayesianClassifier()
#for i in s:
#  print '%s\t %s' % (classifier.classify(i), i)
