from dataclasses import dataclass


class Term(str):
    def __new__(cls, string):
        instance = super().__new__(cls, string)
        return instance

class Definition(str):
    def __new__(cls, string):
        instance = super().__new__(cls, string)
        return instance

class Tense(str):
    def __new__(cls, string):
        instance = super().__new__(cls, string)
        return instance

@dataclass
class Word():
    term: Term
    definition: Definition
    tense: Tense

    def __str__(self):
        return f"{self.term} ({self.tense}): {self.definition}"
    
    def __repr__(self):
        return self.__str__()