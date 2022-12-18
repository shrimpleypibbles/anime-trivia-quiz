import requests

question_data = requests.get(https: // opentdb.com / api.php?amount = 50 & type = boolean).json()

[
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "Amazon acquired Twitch in August 2014 for $970 million dollars.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "The retail disc of Tony Hawk&#039;s Pro Skater 5 only comes with the tutorial.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "medium",
     "question": "The Ceratosaurus, a dinosaur known for having a horn on the top of its nose, is also known to be a decendent of the Tyrannosaurus Rex.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The Great Wall of China is visible from the moon.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
                                      "question": "Greenland is almost as big as Africa.", "correct_answer": "False",
                                      "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
     "question": "&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "There are no roads in\/out of Juneau, Alaska.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
                                       "question": "Eurobeat is primarily an Italian genre of music.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "hard",
     "question": "Unturned originally started as a Roblox game.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "History", "type": "boolean", "difficulty": "medium",
                                       "question": "Sargon II, a king of the Neo-Assyrian Empire, was a direct descendant of Sargon of Akkad.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "medium",
     "question": "The colour of the pills in the Matrix were Blue and Yellow.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
                                      "question": "Big the Cat is a playable character in &quot;Sonic Generations&quot;.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                                       "question": "In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "Minecraft can be played with a virtual reality headset.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                                       "question": "The French word to travel is &quot;Travail&quot;",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "Danganronpa 2: Goodbye Despair featured all of the surviving students from the first game.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy", "question": "Rabbits are rodents.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In Splatoon, the Squid Sisters are named Tako and Yaki.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Japanese Anime & Manga", "type": "boolean", "difficulty": "easy",
     "question": "In Pok&eacute;mon, Ash&#039;s Pikachu refuses to go into a pokeball.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "medium",
     "question": "In the game &quot;Subnautica&quot;, a &quot;Cave Crawler&quot; will attack you.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "In the original Star Wars trilogy, Alec Guinness provided the voice for Darth Vader.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "hard",
     "question": "The song &quot;Mystery Train&quot; was released by artist &quot;Little Junior&#039;s Blue Flames&quot; in 1953.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "hard",
     "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Politics", "type": "boolean", "difficulty": "medium",
     "question": "George W. Bush lost the popular vote in the 2004 United States presidential election.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Vehicles", "type": "boolean", "difficulty": "medium",
     "question": "The General Motors EV1 was the first street-legal production electric vehicle.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "History", "type": "boolean", "difficulty": "medium",
     "question": "The Hundred Years&#039; War was fought for more than a hundred years.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Politics", "type": "boolean", "difficulty": "easy",
                                       "question": "One of Barack Obama&#039;s United States presidential campaign slogan&#039;s was &quot;Yes We Can&quot;.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "History", "type": "boolean", "difficulty": "easy",
     "question": "In World War ll, Great Britian used inflatable tanks on the ports of Great Britain to divert Hitler away from Normandy\/D-day landing.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "medium",
     "question": "Zero factorial is equal to zero. ", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
     "question": "Actor Tommy Chong served prison time.", "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "The sum of any two odd integers is odd.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Scotland voted to become an independent country during the referendum from September 2014.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "easy",
     "question": "New Haven is the capital city of the state of Connecticut in the United States.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "The National Animal of Scotland is the Unicorn.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the &quot;S.T.A.L.K.E.R.&quot; series, the Freedom faction wishes to destroy the supernatural area known as  &quot;the Zone&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "During Wimbledon, spectators in the grounds can buy the tennis balls that have been used in matches.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Mathematics", "type": "boolean", "difficulty": "easy",
     "question": "A scalene triangle has two sides of equal length.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "boolean", "difficulty": "medium",
     "question": "Snagglepuss was part of the Yogi Yahooies in the 1977 show Scooby&#039;s All-Star Laff-a-Lympics.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Geography", "type": "boolean", "difficulty": "medium",
     "question": "The title of the 1969 film &quot;Krakatoa, East_of Java&quot; is incorrect, as Krakatoa is in fact west of Java.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
     "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Entertainment: Cartoon & Animations", "type": "boolean", "difficulty": "medium",
     "question": "In &quot;Avatar: The Last Airbender&quot; and &quot;The Legend of Korra&quot;, Lavabending is a specialized bending technique of Firebending.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Animals", "type": "boolean", "difficulty": "easy",
     "question": "The internet browser Firefox is named after the Red Panda.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Entertainment: Film", "type": "boolean", "difficulty": "hard",
                                       "question": "YouTube personality Jenna Marbles served as an executive producer of the film Maximum Ride (2016).",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
     "question": "In the video game &quot;Splatoon&quot;, the playable characters were originally going to be rabbits instead of squids.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Entertainment: Music", "type": "boolean", "difficulty": "easy",
     "question": "Lead Singer Rivers Cuomo of American rock band Weezer attended Harvard.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
                                       "question": "The mitochondria is the powerhouse of the cell.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]}]
