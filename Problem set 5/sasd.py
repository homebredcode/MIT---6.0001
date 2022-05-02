import string


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        for char in text:
            if char in string.punctuation:
                text = text.replace(char, ' ')
        text = text.lower()
        text = text.split()
        self.phrase = self.phrase.split()
        for word in self.phrase:
            if word not in text:
                return False


        return True

abc = PhraseTrigger('HelLo')

print(abc.is_phrase_in('weiJKKJGA heLlo S!/"sss'))

a = ['hello', 'there', 'yo']

print(a[])