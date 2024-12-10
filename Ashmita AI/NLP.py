import nltk
sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
   ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]

grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking = nltk.RegexpParser(grammar)

parser_chunking.parse(sentence)

Output = parser_chunking.parse(sentence)

Output.draw()
