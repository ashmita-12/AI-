import nltk
from nltk import Tree

def draw_parse_tree(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    grammar = r"""
        NP: {<PRP\$>?<JJ>*<NN>}
        VP: {<VBZ>}
        """
    cp = nltk.RegexpParser(grammar)
    parsed = cp.parse(tagged)
    parsed.pretty_print()

def main():
    sentence = input("Enter a sentence: ")
    draw_parse_tree(sentence)

if __name__ == "__main__":
    main()
