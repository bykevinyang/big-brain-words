import pdfplumber
import re
from typing import List
import structs

theWordsYouShouldKnowPath = "data/The Words You Should Know To Sound Smarter.pdf"

words: List[structs.Word] = []
with pdfplumber.open(theWordsYouShouldKnowPath) as pdf: 
    for i in range(9, 24):
        try:
            text = pdf.pages[i]                     # extract text from page 
            raw_text = text.extract_text()          # extract raw text from page
            bold_text = text.filter(lambda obj: obj["object_type"] == "char" and "Bold" in obj["fontname"])                           # filter bold text
            word = bold_text.extract_text().strip() # extract text from bold text


            # Grabbing the definition and tense
            # for w in word.split():                  # split terms
            split_text = raw_text.splitlines()      # split raw text by term

            for i, line in enumerate(split_text):
                hesitant_tense_split = re.split(r"[ \t]", line)
                # print(hesitant_tense_split)
                if len(hesitant_tense_split) > 1:
                    # Checking if the word is the definition line (first word in sentence)
                    for pronouncation_position, pronouncation_check in enumerate(hesitant_tense_split):
                        if "(" in pronouncation_check:
                            word = str.join(" ", hesitant_tense_split[:pronouncation_position])
                            # if word.lower() == w.lower():
                            # Grabbing the tense
                            raw_tense = hesitant_tense_split[pronouncation_position+1::]
                            tense = structs.Tense(str.join(" ", raw_tense))
                            
                            # Grabbing the definition
                            raw_def_line = split_text[i+1]
                            hesitant_def_split = re.split(r"[ \t]", raw_def_line)
                            definition = structs.Definition(str.join(" ", hesitant_def_split))

                            word_entry = structs.Word(word, definition, tense)
                            words.append(word_entry)
                            # if hesitant_split[0].strip().lower() == w.lower(): print(hesitant_split[1].strip())
                
        except Exception as e:
            print(e)

for word in words:
    print(word)