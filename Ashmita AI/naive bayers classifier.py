import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import defaultdict
class NaiveBayesClassifier:
    def __init__(self):
        self.spam_messages = []
        self.ham_messages = []
        self.vocabulary = set()
        self.word_freq_spam = defaultdict(int)
        self.word_freq_ham = defaultdict(int)
        self.total_spam_words = 0
        self.total_ham_words = 0
    def preprocess_message(self, message):
        stop_words = set(stopwords.words('english'))
        porter = PorterStemmer()
        words = word_tokenize(message.lower())
        words = [porter.stem(word) for word in words if word.isalnum()]
        words = [word for word in words if word not in stop_words]
        return words
    def train(self, messages, labels):
        for message, label in zip(messages, labels):
            words = self.preprocess_message(message)
            if label == 'spam':
                self.spam_messages.append(words)
            else:
                self.ham_messages.append(words)
        for message in self.spam_messages:
            for word in message:
                self.word_freq_spam[word] += 1
                self.vocabulary.add(word)
                self.total_spam_words += 1
        for message in self.ham_messages:
            for word in message:
                self.word_freq_ham[word] += 1
                self.vocabulary.add(word)
                self.total_ham_words += 1
    def calculate_spam_probability(self, message):
        words = self.preprocess_message(message)
        log_prob_spam = 0
        log_prob_ham = 0
        for word in words:
            if word in self.vocabulary:
                # Laplace smoothing to handle unseen words
                log_prob_spam += (self.word_freq_spam[word] + 1) / (self.total_spam_words + len(self.vocabulary))
                log_prob_ham += (self.word_freq_ham[word] + 1) / (self.total_ham_words + len(self.vocabulary))
        return log_prob_spam, log_prob_ham
    def classify(self, message):
        log_prob_spam, log_prob_ham = self.calculate_spam_probability(message)
        return 'spam' if log_prob_spam > log_prob_ham else 'ham'
# Example usage:
messages = [
    "Congratulations! You've won a free vacation.",
    "Meeting tomorrow at 10 am.",
    "Limited time offer. Buy now!",
    "Reminder: Your appointment is scheduled for next week."
]
labels = ['spam', 'ham', 'spam', 'ham']
classifier = NaiveBayesClassifier()
classifier.train(messages, labels)
test_message = "Free gift for you. Claim now!"
result = classifier.classify(test_message)
print("Test message classified as:", result)
