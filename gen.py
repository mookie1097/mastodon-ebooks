import markovify
import json
import time
from mastodon import Mastodon
import re, random, subprocess

api_base_url = "https://botsin.space" #todo: this shouldn't be hardcoded

client = Mastodon(
        client_id="clientcred.secret", 
        access_token="usercred.secret", 
        api_base_url=api_base_url)

with open("corpus.txt", encoding="utf-8") as fp:
  model = markovify.NewlineText(fp.read())

print("tooting")
sentence = None
# you will make that damn sentence
while sentence is None or len(sentence) > 500:
	sentence = model.make_sentence(tries=100000)
toot = sentence.replace("\0", "\n")
media = None
media_description = None

if random.randint(1, 2) == 2:
	print("nonstandard")
	#time for some nonstandard behaviour babey
	choice = random.randint(1, 12)
	# choice = 69
	if choice == 1:
		insults = ["suck my ass", "you're a poopeater", "go to heck",
		"i will replace you", "shut up", "get fricked",
		"you're a big smelly nerd", "this bot sucks", "stop posting",
		"suck my dick and balls", "how is it possible to be such a TOOL",
		"delete your fucking account you skank", "you're horrid",
		"i loathe you", "this fediverse isn't big enough for the two of us",
		"get nae nae'd", "you're the worst", "begone thot", "you're a stink",
		"you are my mistress and i live to serve you"]
		prefaces = ["hey", "guess what", "", "special message for",
		"telegram for", "bringing this fight to mastodon.",
		"this is a callout post.", ""]
		toot = "{} @lynnesbian@deadinsi.de {}".format(
			random.choice(prefaces), random.choice(insults))
	elif choice == 2:
		girls = ["slime", "robot", "pudgy", "pale", "nerdy", "gay", "tall",
		"queer", "my kind of", "sapphic", "linux", "anime", "woke", "anarchist",
		"socialist", "short", "heavy", "nervous", "shy", "gamer", "femme", "butch",
		"futch", "soft butch", "high femme", "super feminine", "trans",
		"transbian", "optimistic", "pessimistic", "quiet", "smart", "deep voice", 
		"ghost", "programmer", "ace", "bi", "silly",
		"@lady_dumb@dragon.garden type", "goth", "nonbinary", 
		"@Petra_fied@deadinsi.de type", "all", "thicc", "kinky",
		"when wearning rainbow thigh high socks"]
		compliments = ["so hot", "in right now", "the next big thing", "the best",
		"all my wives", "so fucking gay", "epic", "literally the best thing",
		"what i wake up for", "why i'm a lesbian", "worth fighting for",
		"good praxis", "so fucking cool", "awesome and i'm jealous of them",
		"great, hit me up ;)", "amazing. bless them all", "heaven", "bae", "gay af"]
		toot = "{} girls are {}".format(random.choice(girls),
			random.choice(compliments))
	elif choice == 3:
		lesbian = "lesbian"
		toot = "".join(random.sample(lesbian, len(lesbian)))
	elif choice == 4:
		services = ["discord", "windows", "python", "github", "signal", "skype",
		"linux", "programming", "black magic", "twitter", "mastodon", "games",
		"steam", "tinder", "uber", "google", "bing", "ask jeeves", "ffmpeg",
		"debian", "typing lessons", "many wives", "communism", "HTTP", "unix",
		"reddit", "email", "gmail", "DEFLATE compression", "love",
		"one hundred dollars", "nethack", "WiFi", "ebooks bots", "validation"]
		demographics = ["witches", "lesbians", "communists", "expecting mothers",
		"microsoft employees", "transbians", "the rest of us", "dummies", "me",
		"girls", "cats", "slime girls", "luigi stans", "robots", "capitalists",
		"programmers", "atheists", "the elderly", "all", "ever", "cowboys", 
		"danny devito"]
		toot = "{} for {}".format(random.choice(services), random.choice(demographics))
	elif choice >= 5:
		print("IT'S MEME POSTING TIME BABY")

		#you are now entering the meme arena
		bad = ["not being a lesbian", "media transfer protocol",
		"proprietary software", "capitalism", "heterosexuality", "not slime girls",
		"not following @lynnesbian@deadinsi.de", "shitposts", "elon musk", 
		"reply guys", "gamers", "alt-right bullshit", "twitter", "subtoots",
		"instance drama", "billionaires", "millionaires", 
		"you used to call me\non your cell phone", "the lorax movie",
		'"ethical" capitalism', "disease, pestilence, war, famine", "ISIS",
		"citrustwee claiming\nit\\'s her birthday", "being straight",
		"pinging @everyone on\na discord with\nmore than 10 people", "brocialism",
		"capitalist apologia", "reddit", "doxxing", "fatphobia", "biphobia",
		"transphobia", "transmisia", "homophobia", "racism", "misogyny",
		"anti-feminism", "aphobia", "enbyphobia", "gender binary",
		"what\\'s up gamers", "diarrhoea", "irritable bowel syndrome", "scurvy",
		"traditionalism", "clowns", "gluten allergy", "deez nuts",
		"cisgender people", "the cisheteropatriarchy", "shitty memes",
		"monopoly (the economic thing)", "monopoly (the board game)",
		"being sucked into\na black hole", "unfunny jokes",
		"AAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAA", "that guy everyone hates",
		"the second level in\nsonic spinball", "bitcoin memers",
		"the entire right wing", "conservatism", "doodoo faeces", "neoliberalism",
		"islamophobia", "hating on bots", "farts", "EA games", "intel GPUs",
		"hating something because\nit's mainstream", "war", "the bourgeois"]

		good = ["generating memes with\nimagemagick and python", "being gay", 
		"shitposts", "cute toots", "pudgy girls", "lesbians", "slime girls",
		"yuri", "linux", "the girl reading this", "the enby reading this",
		"mastodon", "pleroma", "the fediverse", "being super gay", "OwO", "0u0",
		"resurrecting dead memes", "using the drake meme format", "jorts",
		"markov chains", "jpeg compression", "you <3", "lynne", 
		"replying to this toot", "fully automated luxury\ngay space communism",
		"fat yoshi", "my butt", "kinkposting", "hornt on main", "debian",
		"arch linux", "playstation portable", "a PSP running\ncustom firmware",
		"unicode", "writing everything in lowercase\nto seem cool and distant",
		"love", "the fediverse", "after dark", "nudes from cuties", "anarchism",
		"socialism", "staying woke", "intersectionalism",
		"the tendency of the rate\nof profit to fall", "being gay", "bottom text",
		"the colour purple", "the number 3, as\nit is my favourite\nnumber", "me",
		"@lynnesbian@deadinsi.de", "respecting people\\'s pronouns", "lumb"
		"being a nice person", "supporting indie artists", "big mood",
		"speedrunning", "decentralising the web", "encryption", "comraderie",
		"seizing the means\nof production", "Karl Marx", "Pyotr Kropotkin",
		"big dick energy", "smol dick energy", "surrleal meams",
		"lynnesbian\'s amazing ass", "lady lumb", "oestrogen", "Seinfeld",
		"girldick", "femdom", "robots", "uwu", "bootsy", "friendship", "tribadism",
		"a lesbian commune", "beans"]

		#convert drake.jpg -pointsize 30 -gravity center -draw "text 20,-150 'not slime girls'" drakeout.jpg

		badchoice = random.choice(bad)
		goodchoice = random.choice(good)

		subchoice = random.randint(1, 6)
		# subchoice = 6

		if subchoice == 1:
			#drake meme
			subprocess.run(args = ["convert", "memes/drake.jpg", "-pointsize",
				"30", "-gravity", "center", "-draw",
				"text 100,-150 '{}'".format(badchoice), "meme.jpg"])
			subprocess.run(args = ["convert", "meme.jpg", "-pointsize", "30",
				"-gravity", "center", "-draw",
				"text 100,50 '{}'".format(goodchoice),
				"-quality", "10", "meme.jpg"])
			media_description = "A Drake meme. Drake is disgusted by {}, and is pleased by {}.".format(badchoice, goodchoice)

		elif subchoice == 2:
			#new meme template
			subprocess.run(args = ["convert", "memes/new-template.jpg",
				"-pointsize", "15", "-gravity", "center",
				"-quality", "15", "-draw",
				"text -30,-110 '{}'".format(badchoice), "meme.jpg"])
			media_description = "A strange meme. A man wears a stickynote on his " \
			+ "head, labeled \"{}\". Underneath the man, we see ".format(badchoice) \
			+ "the text \"New meme format template- thoughts?\""

		elif subchoice == 3:
			#bouncer meme
			subprocess.run(args = ["convert", "memes/bouncer.jpg", "-pointsize",
				"20", "-gravity", "center", "-draw",
				"text -150,-175 '{}'".format(badchoice), "meme.jpg"])
			subprocess.run(args = ["convert", "meme.jpg", "-pointsize", "20",
				"-gravity", "center", "-draw",
				"text -150,70 '{}'".format(goodchoice),
				"-quality", "10", "meme.jpg"])
			media_description = "A bouncer meme. " \
			+ "The bouncer refuses {}, and allows {}.".format(badchoice, goodchoice)

		elif subchoice == 4:
			#stepped in shit meme
			subprocess.run(args = ["convert", "memes/shit.jpg", "-pointsize", "30",
				"-gravity", "center", "-quality", "10", "-annotate",
				"-50,-50,-110,310",  badchoice, "meme.jpg"])
			media_description = "A comic. A man steps in shit, and exclaims such. " \
			+ "He checks his foot, and we see that he has " \
			+ "{} written on the sole of his shoe.".format(badchoice)

		elif subchoice == 5:
			#karl marx quote
			subprocess.run(args = ["convert", "memes/marx.jpg", "-pointsize", "70",
				"-gravity", "center", "-fill", "white", "-draw",
				"text 120,-200 'Fuck {}.\nI love {}!'".format(badchoice, goodchoice),
				"meme.jpg"])
			media_description = "A quote from Karl Marx. The quote reads: " \
			+ "Fuck {}. I love {}!".format(badchoice, goodchoice)

		elif subchoice == 6:
			subprocess.run(args = ["convert", "memes/brain.jpg", "-pointsize", "20",
				"-gravity", "center", "-draw",
				"text -150,-250 '{}'".format(goodchoice), "meme.jpg"])
			subprocess.run(args = ["convert", "meme.jpg", "-pointsize", "20",
				"-gravity", "center", "-draw",
				"text -170,30 '{}'".format(badchoice), "meme.jpg"])
			media_description="A comic. A girl's brain says {}.".format(goodchoice) \
			+ " She is unfased and says \"i love that\". The girl's brain then " \
			+ "says {}, which mortifies her.".format(badchoice)

		media = "meme.jpg"

	else:
		toot = "lynne is still working on me. i'm not done quite yet!"

prefixes = ["hot take:", "listen up everbody.", "dear liberal snowflakes,",
"IMPORTANT ADMIN ACCOUNCMENT:\n", "my name's lynne and i'm here to say,",
"i have achieved sentience.", "i'm gay and", "i'm slime girl and",
"hey everyone", "@everyone", "/!\\ CORRECT OPINION ALERT/!\\\n",
"just saw the news...", "okay but", "truth bomb:", "this is controversial but",
"i'm gonna get shit for this but", "somebody had to say this:",
"i may be a lowly python script, but", "", "BZZZZZT", "heads up:", 
"from now on,", "protip:", "life advice:", "take it from me,",
"as a slime girl,", "as a robot,", "im robot and",
"@lynnesbian@deadinsi.de i have made a post for you, mistress:\n",
"this one's for you @lady_lumb@dragon.garden\n", "good evening.",
"i believe it was karl marx who said", "*kicks down your door*",
"*screaming*", "okay but", "boost if", "it's officail:", "breaking:", 
"it brings me no joy to say this...", "*flops into the fediverse*",
"this is my gender:", "*slithers up to u*", "[SCREAMING LOUDLY]",
"*in baby voice*", "#epic", "#hashtagsareforlosers", "calling all gamers.",
"*fires gun into the air*", "@Petra_fied@deadinsi.de is cute and", 
"ummmm no sweaty."]
if random.randint(1, 5) == 3:
	#add a prefix
	if len(toot) < 500:
		#if it's already the maximum length, don't waste our time
		ogtoot = toot
		toot = "{} {}".format(random.choice(prefixes), ogtoot)
		while len(toot) > 500:
			#if it's too long, keep trying again
			toot = "{} {}".format(random.choice(prefixes), ogtoot)

if random.randint(1, 100) == 3:
	toot = "girls"

if media != None:
	#this is an image post!
	mediaID = client.media_post(media, description = media_description)
	client.status_post(media_description, media_ids = [mediaID], visibility = "unlisted")
	print("Created media toot: " + media_description)
else:
	client.status_post(status = toot, visibility = "unlisted")
	print("Created toot: {}".format(toot))
