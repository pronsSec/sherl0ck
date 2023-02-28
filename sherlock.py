from types import BuiltinMethodType
import os
import re
import email
from googletrans import LANGUAGES, Translator
from tqdm import tqdm

art2 = '''
   ▄▄▄▄▄    ▄  █ ▄███▄   █▄▄▄▄ █    ████▄ ▄█▄    █  █▀     
  █     ▀▄ █   █ █▀   ▀  █  ▄▀ █    █   █ █▀ ▀▄  █▄█       
▄  ▀▀▀▀▄   ██▀▀█ ██▄▄    █▀▀▌  █    █   █ █   ▀  █▀▄       
 ▀▄▄▄▄▀    █   █ █▄   ▄▀ █  █  ███▄ ▀████ █▄  ▄▀ █  █      
              █  ▀███▀     █       ▀      ▀███▀    █       
             ▀            ▀                       ▀        
                                                           
'''
print(art2)
print('           MULTI-LINGUAL EMAIL DUMP SEARCH SCRIPT\n')
print('-'*45)
print('By: Been')
print('-'*45)
print('-'*45)
print('-'*45)
print('-'*45)
print('-')




folder_path = input('Enter the path to the folder containing the .eml files: ')
print('-'*45)

if not os.path.isdir(folder_path):
    print('Invalid folder path. Please enter a valid path.')
    exit()


eml_files = [f for f in os.listdir(folder_path) if f.endswith('.eml')]


search_term = input('Enter the word or phrase to search for: ')
print('-'*45)

print('Please select a language to search in:')
for index, lang in enumerate(LANGUAGES.values()):
    print(f'{index + 1}. {lang}')
lang_index = int(input('Enter the number of the language: '))
lang_code = list(LANGUAGES.keys())[lang_index - 1]
print('-'*45)


# initialize a translator object
translator = Translator()

results = []
num_results = 0
print('-'*45)


for file in tqdm(eml_files, desc='Searching emails', unit='file'):
    # try to open the file and parse the email contents
    try:
        with open(os.path.join(folder_path, file), 'rb') as f:
            msg = email.message_from_binary_file(f)
    except:
        print(f'Error reading file {file}. Skipping...')
        continue
    
    # translate the search term to the selected language
    try:
        translated_term = translator.translate(search_term, dest=lang_code).text
        #translated_term = str(translated_term)
    except:
        print('Error translating search term. Skipping...')
        continue
    
    #handling serious shit yo
    
    body1 = msg.get_payload(decode=True)
    if body1 is None:
        global body
        body=msg.get_payload(decode=False)
        body = body[0].get_payload()

    else:
        #global body
        body = body1



    
    # search for the translated search term in the email subject, body, and file name using regular expressions
    if re.search(translated_term, msg['Subject'], re.IGNORECASE) or \
        re.search(translated_term, body, re.IGNORECASE) or \
        re.search(translated_term, file, re.IGNORECASE):
            
        # if the search term is found, print the file name and increment the counter
        print('\n Positive Result: ' + file)
        num_results += 1
        results += [file]

# print the total number of results

art = '''
________                        
\______ \   ____   ____   ____  
 |    |  \ /  _ \ /    \_/ __ \ 
 |    `   (  <_> )   |  \  ___/ 
/_______  /\____/|___|  /\___  >
        \/            \/     \/ 
'''
#print('-'*45)
print(art)
print('-'*45)
print('-'*45)
print('-'*45)
print(f'Total number of results: {num_results}')
print('-'*45)
print('Resulting filenames:')
for i in results:
  print(i)
print('-'*45)
print('-'*45)
