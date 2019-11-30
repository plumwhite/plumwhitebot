# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
import pickle
import html.parser
import pandas as pd
import re
import string
from collections import defaultdict
import random


# Optional code that requires an allpoetry account to execute
# #for scraping
# def scrape_poems(url):
#     urls = []

#     page = requests.get(url).text
#     soup = BeautifulSoup(page)
#     author_link_list = soup.find_all("a")
#     for a in author_link_list:
#         urls.append(a.get('href'))

#     return urls

# # relative hrefs of poems
# # replace string with valid link
# poem_links = [scrape_poems("link to list of Li Po poems from allpoetry")]
# print(poem_links)

# urls = []
# #indexed at 0 due to list within list
# for link in poem_links[0]:
#     urls.append("https://allpoetry.com/" + link)

# print(urls)

def scrape_gutenberg(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    text = [span.text for span in soup.find_all(class_='poem')]
    return ''.join(text)

# deprecated, could be useful for future scrapes
urls = ['https://allpoetry.com//poem/8448219--by-Li-Po',
        'https://allpoetry.com//A-Farewell-To-Secretary-Shuyun-At-The-Xietiao-Villa-In-Xuanzhou',
        'https://allpoetry.com//A-Mountain-Revelry', 'https://allpoetry.com//A-Song-Of-An-Autumn-Midnight',
        'https://allpoetry.com//A-Song-Of-Changgan', 'https://allpoetry.com//A-Vindication',
        'https://allpoetry.com//About-Tu-Fu', 'https://allpoetry.com//Alone-and-Drinking-Under-the-Moon',
        'https://allpoetry.com//Alone-Looking-at-the-Mountain',
        'https://allpoetry.com//Amidst-the-Flowers-a-Jug-of-Wine', 'https://allpoetry.com//Amusing-Myself',
        'https://allpoetry.com//Ancient-Air',
        'https://allpoetry.com//poem/14046184-Atop-Green-Mountains-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Autumn-Air', 'https://allpoetry.com//poem/13494460-Autumn-Air-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Autumn-River-Song', 'https://allpoetry.com//Ballads-Of-Four-Seasons:-Spring',
        'https://allpoetry.com//Ballads-Of-Four-Seasons:-Summer',
        'https://allpoetry.com//Ballads-Of-Four-Seasons:-Winter', 'https://allpoetry.com//Bathed-and-Washed',
        'https://allpoetry.com//Before-The-Cask-of-Wine',
        'https://allpoetry.com//poem/13517669-Bitter-Love-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Bringing-in-the-Wine', 'https://allpoetry.com//poem/13521343-Ching-Ping-Tiao-by-Li-Po',
        'https://allpoetry.com//Changgan-Memories', 'https://allpoetry.com//poem/14327926-Chiang-Chin-Chiu-by-Li-Po',
        'https://allpoetry.com//Chuang-Tzu-And-The-Butterfly', 'https://allpoetry.com//Clearing-at-Dawn',
        'https://allpoetry.com//Climbing-West-Of-Lotus-Flower-Peak', 'https://allpoetry.com//Confessional',
        'https://allpoetry.com//Crows-Calling-At-Night', 'https://allpoetry.com//Down-from-the-Mountain',
        'https://allpoetry.com//Down-Zhongnan-Mountain-',
        'https://allpoetry.com//poem/14327929-Drinking-Alone-by-Li-Po',
        'https://allpoetry.com//Drinking-Alone-in-the-Moonlight', 'https://allpoetry.com//Drinking-in-the-Mountains',
        'https://allpoetry.com//Drinking-With-Someone-In-The-Mountains',
        'https://allpoetry.com//poem/13711135-Endless-Yearning-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//poem/13689342-Exiles-Letter-by-Li-Po',
        'https://allpoetry.com//poem/13556808-Facing-Wine-by-Li-Po', 'https://allpoetry.com//Farewell-to-Meng-Hao-jan',
        'https://allpoetry.com//poem/13497812-Farewell-to-Meng-Hao-jan-at-Yellow-Crane-Tower-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Farewell-to-Secretary-Shu-yun-at-the-Hsieh-Tiao-Villa-in-Hsuan-Chou',
        'https://allpoetry.com//For-Meng-Hao-Jan', 'https://allpoetry.com//For-Wang-Lun',
        'https://allpoetry.com//poem/13494456-For-Wang-Lun-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//poem/14327923-Gazing-At-The-Cascade-On-Lu-Mountain-by-Li-Po',
        'https://allpoetry.com//Going-Up-Yoyang-Tower',
        'https://allpoetry.com//Gold-painted-jars---wines-worth-a-thousand.', 'https://allpoetry.com//Good-Old-Moon',
        'https://allpoetry.com//poem/14327928-Green-Mountain-by-Li-Po', 'https://allpoetry.com//Hard-Is-The-Journey',
        'https://allpoetry.com//poem/13494468-Hearing-a-Flute-in-Lo-yang-City-On-a-Spring-Night-by-Li-Po--by-Li-Po',
        'https://allpoetry.com//Hearing-A-Flute-On-A-Spring-Night-In-Luoyang',
        'https://allpoetry.com//His-Dream-Of-Skyland', 'https://allpoetry.com//Ho-Chih-chang',
        'https://allpoetry.com//In-Spring', 'https://allpoetry.com//poem/13494474-Jade-Stairs-Grievance-by-Li-Po',
        'https://allpoetry.com//Lament-for-Mr-Tai', 'https://allpoetry.com//Lament-of-the-Frontier-Guard',
        'https://allpoetry.com//poem/14048754-Lament-On-an-Autumn-Night-by-Li-Po',
        'https://allpoetry.com//Laolao-Ting-Pavilion',
        'https://allpoetry.com//poem/13689334-Leave-Taking-Near-Shoku-by-Li-Po',
        'https://allpoetry.com//Leaving-White-King-City', 'https://allpoetry.com//Lines-For-A-Taoist-Adept',
        'https://allpoetry.com//Listening-to-a-Flute-in-Yellow-Crane-Pavillion', 'https://allpoetry.com//Long-Yearning',
        'https://allpoetry.com//Long-Yearning-(Sent-Far)',
        'https://allpoetry.com//Looking-For-A-Monk-And-Not-Finding-Him', 'https://allpoetry.com//Lu-Mountain,-Kiangsi',
        'https://allpoetry.com//poem/14327920-Marble-Stairs-Grievance-by-Li-Po', 'https://allpoetry.com//Mng-Hao-jan',
        'https://allpoetry.com//Midnight-Song-of-Wu',
        'https://allpoetry.com//poem/13517660-Moon-at-the-Fortified-Pass-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//poem/14327924-Moon-Over-Mountain-Pass-by-Li-Po',
        'https://allpoetry.com//Mountain-Drinking-Song', 'https://allpoetry.com//Nefarious-War',
        'https://allpoetry.com//Old-Poem', 'https://allpoetry.com//poem/14327919-On-A-Picture-Screen-by-Li-Po',
        'https://allpoetry.com//poem/14327916-On-Climbing-In-Nan-King-To-The-Terrace-Of-Phoenixes-by-Li-Po',
        'https://allpoetry.com//On-Dragon-Hill',
        'https://allpoetry.com//poem/14327911-On-Gazing-Into-A-Mirror-by-Li-Po',
        'https://allpoetry.com//On-Kusu-Terrace',
        'https://allpoetry.com//poem/14327918-Parting-At-A-Wine-Shop-In-Nan-King-by-Li-Po',
        'https://allpoetry.com//poem/13689349-Poem-by-The-Bridge-at-Ten-Shin-by-Li-Po',
        'https://allpoetry.com//Question-And-Answer-On-The-Mountain',
        'https://allpoetry.com//poem/14327927-Quiet-Night-Thoughts-by-Li-Po',
        'https://allpoetry.com//Reaching-the-Hermitage', 'https://allpoetry.com//Remembering-the-Springs-at-Chih-chou',
        'https://allpoetry.com//Resentment-Near-the-Jade-Stairs', 'https://allpoetry.com//Seeing-Off-A-Friend',
        'https://allpoetry.com//Seeing-Off-Meng-Haoran-For-Guangling-At-Yellow-Crane-Tower',
        'https://allpoetry.com//Self-Abandonment', 'https://allpoetry.com//Sent-To-Du-Fu-Below-Shaqiu-City',
        'https://allpoetry.com//She-Spins-Silk',
        'https://allpoetry.com//poem/13523108-Sitting-Alone-On-Jingting-Mountain-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Sitting-Alone-On-Jingting-Shan-Hill',
        'https://allpoetry.com//poem/13517663-Song-of-an-Autumn-Midnight-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Song-of-the-Forge', 'https://allpoetry.com//Song-Of-The-Jade-Cup',
        'https://allpoetry.com//poem/13689350-South-Folk-in-Cold-Country-by-Li-Po',
        'https://allpoetry.com//poem/14327917-Spring-Night-In-Lo-Yang-Hearing-A-Flute-by-Li-Po',
        'https://allpoetry.com//Staying-The-Night-At-A-Mountain-Temple',
        'https://allpoetry.com//poem/13497798-Summer-Day-in-the-Mountains-by-Li-Po',
        'https://allpoetry.com//poem/13544955-Summer-Day-in-the-Mountains-by-Li-Po',
        'https://allpoetry.com//Summer-in-the-Mountains', 'https://allpoetry.com//Taking-leave-of-a-friend',
        'https://allpoetry.com//poem/13497827-Taking-Leave-of-a-Friend-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//poem/13689355-Taking-Leave-of-a-Friend-by-Li-Po-Tr.-by-Ezra-Pound-by-Li-Po',
        'https://allpoetry.com//Talk-in-the-Mountains',
        'https://allpoetry.com//poem/14327913-The-Ching-Ting-Mountain-by-Li-Po',
        'https://allpoetry.com//poem/13689358-The-City-of-Choan-by-Li-Po',
        'https://allpoetry.com//The-Cold-Clear-Spring-At-Nanyang',
        'https://allpoetry.com//The-Moon-At-The-Fortified-Pass', 'https://allpoetry.com//The-Old-Dust',
        'https://allpoetry.com//poem/13689361-The-River-Song-by-Li-Po',
        'https://allpoetry.com//The-River-Captains-Wife--A-Letter', "https://allpoetry.com//The-River-Merchant's-Wife",
        'https://allpoetry.com//The-Roosting-Crows',
        'https://allpoetry.com//poem/14327912-The-Solitude-Of-Night-by-Li-Po',
        'https://allpoetry.com//poem/14327925-Thoughts-In-A-Tranquil-Night-by-Li-Po',
        'https://allpoetry.com//poem/13497833-Thoughts-On-a-Quiet-Night-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Thoughts-On-A-Still-Night', 'https://allpoetry.com//Three-Poems-on-Wine',
        'https://allpoetry.com//poem/14327921-Through-The-Yangzi-Gorges-by-Li-Po',
        'https://allpoetry.com//To-His-Two-Children', 'https://allpoetry.com//To-My-Wife-on-Lu-shan-Mountain',
        "https://allpoetry.com//To-Tan-Ch'iu", 'https://allpoetry.com//To-Tu-Fu-from-Shantung',
        'https://allpoetry.com//poem/14327914-To-Wang-Lun-by-Li-Po',
        'https://allpoetry.com//poem/14327922-Under-The-Moon-by-Li-Po',
        "https://allpoetry.com//Viewing-Heaven's-Gate-Mountains",
        'https://allpoetry.com//poem/13497844-Visiting-a-Taoist-Master-on-Tai-Tien-Mountain-by-Li-Po-by-Li-Po',
        'https://allpoetry.com//Visiting-A-Taoist-On-Tiatien-Mountain',
        'https://allpoetry.com//Visiting-The-Taoist-Priest-Dai-Tianshan-But-Not-Finding-Him',
        'https://allpoetry.com//Waking-from-Drunken-Sleep-on-a-Spring-Day.',
        'https://allpoetry.com//Waterfall-at-Lu-shan', 'https://allpoetry.com//We-Fought-for---South-of-the-Walls',
        'https://allpoetry.com//Yearning', 'https://allpoetry.com//poem/14327915-Ziyi-Song-by-Li-Po',
        'https://allpoetry.com//poem/8448155-Facing-Wine-by-Li-Po']


# Scrapes transcript data from Gutenberg Project
def url_to_poem_body(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    text = [p for p in soup.find(class_="poem_body")]
    return text

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)

    return text

def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub("[^a-zA-Z' ]+", '', text)
    return text


def markov_chain(text):
    '''The input is a string of text and the output will be a dictionary with each word as
       a key and each value as the list of words that come after the key in the text.'''

    # Tokenize the text by word, though including punctuation
    words = text.split(' ')

    # Initialize a default dictionary to hold all of the words and next words
    m_dict = defaultdict(list)

    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    m_dict = dict(m_dict)
    return m_dict

def generate_sentence(chain, count):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''

    # Capitalize the first word
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count-1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    return(sentence)

def clean_main():
    poets = ['libai']

    poems = scrape_gutenberg("https://www.gutenberg.org/files/43274/43274-h/43274-h.htm")

    # Pickle files for later use

    with open("transcript.txt", "wb") as file:
        pickle.dump(poems, file)
    # Load pickled files
    data = {}
    with open("transcript.txt", "rb") as file:
        data['libai'] = pickle.load(file)

    data['libai'] = [data['libai']]

    pd.set_option('max_colwidth', 150)

    data_df = pd.DataFrame.from_dict(data).transpose()
    data_df.columns = ['transcript']
    data_df = data_df.sort_index()

    round1 = lambda x: clean_text_round1(x)

    data_clean = pd.DataFrame(data_df.transcript.apply(round1))
    data_clean.transcript.loc['libai']

    round2 = lambda x: clean_text_round2(x)

    data_clean = pd.DataFrame(data_clean.transcript.apply(round2))

    data_clean.to_pickle("corpus.pkl")

def generate_main():
    data = pd.read_pickle('corpus.pkl')
    li_bai_text = data.transcript.loc['libai']
    li_bai_dict = markov_chain(li_bai_text)
    return generate_sentence(li_bai_dict, random.randint(15,30))