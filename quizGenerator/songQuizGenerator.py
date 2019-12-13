# Top 50 songs of all time, quiz generator created by Mark Foos, based on Automate the Boring Stuff with Python
# match the song with the artist


import random

#question and answer objects
artists = { 'Smells Like Teen Spirit': 'Nirvana',
'Imagine': 'John Lennon',
'One': 'U2',
'Billie Jean': 'Michael Jackson',
'Bohemian Rhapsody': 'Queen',
'Hey Jude': 'The Beatles',
'Like A Rolling Stone': 'Bob Dylan',
"I Can't Get No Satisfaction": 'Rolling Stones',
'God Save The Queen': 'Sex Pistols',
"Sweet Child O'Mine": "Guns N' Roses",
"London Calling": 'The Clash',
'Waterloo Sunset': 'The Kinks',
'Hotel California': 'The Eagles',
'Your Song': 'Elton John',
'Stairway To Heaven': 'Led Zeppelin',
'The Twist': 'Chubby Checker',
'Live Forever': 'Oasis',
'I Will Always Love You': 'Whitney Houston',
'Life On Mars?': 'David Bowie',
'Heartbreak Hotel': 'Elvis Presley',
'Over The Rainbow': 'Judy Garland',
"What's Goin' On": 'Marvin Gaye',
'Born To Run': 'Bruce Springsteen',
'Be My Baby': 'The Ronettes',
'Creep': 'Radiohead',
'Bridge Over Troubled Water': 'Simon & Garfunkel',
'Respect': 'Aretha Franklin',
'Family Affair': 'Sly And The Family Stone',
'Dancing Queen': 'ABBA',
'Good Vibrations': 'The Beach Boys',
'Purple Haze': 'Jimi Hendrix',
'Yesterday': 'The Beatles',
'Jonny B Good': 'Chuck Berry',
'No Woman No Cry': 'Bob Marley',
'Hallelujah': 'Jeff Buckley',
'Every Breath You Take': 'The Police',
'A Day In The Life': 'The Beatles',
'Stand By Me': 'Ben E King',
"Papa's Got A Brand New Bag": 'James Brown',
'Gimme Shelter': 'The Rolling Stones',
"What'd I Say": 'Ray Charles',
'Sultans Of Swing': 'Dire Straits',
'God Only Knows': 'The Beach Boys',
"You've Lost That Lovin' Feeling":'The Righteous Brothers',
'My Generation': 'The Who',
'Dancing In The Street': 'Martha Reeves and the Vandellas',
'When Doves Cry': 'Prince',
'A Change Is Gonna Come': 'Sam Cooke',
'River Deep Mountain High': 'Ike and Tina Turner',
'Best Of My Love': 'The Emotions' }

#main function: create 5 individual quizzes and answer keys from object dictionary
for quizNum in range(5):
    quizFile = open('songsQuiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('songsQuiz_answers%s.txt' % (quizNum + 1), 'w')

    quizFile.write('Name:\n\nDate\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Song Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

#create the question list and answer list
    for questionNum in range(50):
        songs = list(artists.keys())
        random.shuffle(songs)
        correctAnswer = artists[songs[questionNum]]
        wrongAnswers = list(artists.values())
        #delete the correct Answer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        #delete duplicate correct answers
        if correctAnswer == wrongAnswers:
            del wrongAnswers

#pull the 4 choices and randomize
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)


#create the actual question format
        quizFile.write('%s. Who is the artist of %s\n' % (questionNum + 1, songs[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))

#close txt files
    quizFile.close()
    answerKeyFile.close()
