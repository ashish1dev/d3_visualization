
#code to remove stop words
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re

from nltk.stem import PorterStemmer

import emoji
def give_emoji_free_text(text):
    allchars = [str for str in text.decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

def remove_emoji(string):
    # Emojis pattern
    emoji_pattern = re.compile("["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                    u"\U00002702-\U000027B0"
                    u"\U000024C2-\U0001F251"
                    u"\U0001f926-\U0001f937"
                    u'\U00010000-\U0010ffff'
                    u"\u200d"
                    u"\u2640-\u2642"
                    u"\u2600-\u2B55"
                    u"\u23cf"
                    u"\u23e9"
                    u"\u231a"
                    u"\u3030"
                    u"\ufe0f"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def clean_data(rawText):
    # example_sent = "This is a sample sentence, showing off the stop words filtration."
    # rawText = '@username : This is a 123 rawText3 0with a url: http://t.co/0DlGChTBIx sample text 33 http://t.co/0DlGChTBIx '

    rawText = rawText.encode('ascii', 'ignore').decode('ascii')
    #remove Emojis
    rawText = give_emoji_free_text(rawText)


    #remove @username
    rawText = re.sub('@[^\s]+','',rawText)

    # rawText = rawText.replace('\n',' ')

    # remove patterns matching url format
    url_pattern = r'((http|ftp|https):\/\/)?[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'
    rawText = re.sub(url_pattern, ' ', rawText)
    # print('without URL : ',rawText)


    #remove numbers / digits
    rawText = re.sub(r'\d+', '', rawText)
    # print rawText

    #convert to lowercase
    rawText = rawText.lower()

    #remove comma
    rawText = rawText.replace(',',' ')

    #remove semicolon
    rawText = rawText.replace(';',' ')

    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(rawText)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    # print(word_tokens)
    # print(filtered_sentence)

    rawText = " ".join(filtered_sentence)

    # #stemming
    # stemmed = []
    # ps = PorterStemmer()
    # for w in filtered_sentence:
    #     # print(w, '= ',ps.stem(w))
    #     stemmed.append(ps.stem(w))
    #
    # rawText = " ".join(stemmed)

    #remove colon
    rawText = rawText.replace(':',' ')

    #remove dot
    rawText = rawText.replace('.',' ')

    #remove '
    rawText = rawText.replace("-",' ')
    rawText = rawText.replace("/",' ')
    rawText = rawText.replace(".",' ')
    rawText = rawText.replace("..",' ')
    rawText = rawText.replace("...",' ')
    rawText = rawText.replace("#",' ')
    rawText = rawText.replace("?",' ')
    rawText = rawText.replace("!",' ')
    rawText = rawText.replace("%",' ')

    rawText = rawText.replace("'",' ')

    #remove (
    rawText = rawText.replace('(',' ')
    rawText = rawText.replace(')',' ')
    rawText = rawText.replace('[',' ')
    rawText = rawText.replace(']',' ')
    rawText = rawText.replace('`',' ')
    rawText = rawText.replace('|',' ')





    #remove \n newline with space
    rawText = rawText.replace('\r', '').replace('\n', '')


    #replace multi white spaces to single whitespace
    rawText = ' '.join(rawText.split())

    return rawText

# text = "@username : This is a 123 rawText3 0with a url: http://t.co/0DlGChTBIx sample text 33 http://t.co/0DlGChTBIx"
# cleanText = clean_data(text)
# print(cleanText)

word = 'All_Disease'
filename = "get_tweets/data/cc/data_commonCrawl_"+word
# filename = "output_NYT_All_Disease"
cleaned_data = []
# Open the file with read only permit
f = open(filename+".txt", "r")
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    print("----------")

    line = line.decode('utf-8')
    line = line.strip()
    # print(len(line))
    if(len(line)>1 and (line != '\n')):
        cleanText = clean_data(line)
        cleaned_data.append(cleanText)
        print(cleanText)
    # use realine() to read next line
    line = f.readline()
f.close()

#write to file
file = open(filename+"_processed"+".txt", "w")

# file.write("This is a test")
# file.write("To add more lines.")
for str in cleaned_data:
    # print(str)
    if(str != '\n' and str != ''):
        file.write(str+'\n')

file.close()
