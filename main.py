import csv

from termcolor import colored

import lesson

lesson.greeting()

CSV_PATH = 'ranking.csv'
fieldnames = ['NAME', 'COUNT']


while True:
    name = input('')
    if name:
        if lesson.csv_has_data(CSV_PATH):

            key_arr = lesson.get_recommend_row(CSV_PATH)
            for key in key_arr:
                print(colored('===================================================', 'green'))
                print(colored(f'私のオススメのレストランは、{key}です。', 'green'))
                print(colored(f'I recommend {key} restaurant.', 'green'), end='\n\n')

                while True:
                    print(colored('このレストランは好きですか？ [yes/no]', 'green'))
                    print(colored('Do you like it? [y/n]', 'green'))
                    print(colored('===================================================', 'green'))
                    yes_or_no = input('').lower()

                    if yes_or_no in ['yes', 'no', 'y', 'n']:
                        break
                    
                    print(colored('yesかnoで回答してください。', 'red'))
                    print(colored('Please answer with yes or no.', 'red'))

                if yes_or_no in ['yes', 'y']:
                    break

            print(colored('===================================================', 'green'))
            print(colored(f'{name}さん。どこのレストランが好きですか？', 'green'))
            print(colored(f'{name}, which restaurants do you like?', 'green'))
            print(colored('===================================================', 'green'))
            favorite_restaurant = input('').title()

            if favorite_restaurant:
                lesson.update_restaurant_count(CSV_PATH, favorite_restaurant)

                print(colored('===================================================', 'green'))
                print(colored(f'{name}さん。ありがとうございました。', 'green'))
                print(colored(f'Thank you so much, {name}!', 'green'), end='\n\n')
                print(colored('良い一日を！さようなら。', 'green'))
                print(colored('Have a good day!', 'green'))
                print(colored('===================================================', 'green'))

        else:
            print(colored('===================================================', 'green'))
            print(colored(f'{name}さん。どこのレストランが好きですか？', 'green'))
            print(colored(f'{name}, which restaurants do you like?', 'green'))
            print(colored('===================================================', 'green'))
            favorite_restaurant = input().title()

            if favorite_restaurant:
                with open(CSV_PATH, 'w', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'NAME': favorite_restaurant, 'COUNT': 1})

            print(colored('===================================================', 'green'))
            print(colored(f'{name}さん。ありがとうございました。', 'green'))
            print(colored(f'Thank you so much, {name}!', 'green'), end='\n\n')
            print(colored('良い一日を！さようなら。', 'green'))
            print(colored('Have a good day!', 'green'))
            print(colored('===================================================', 'green'))

    break
