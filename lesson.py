import csv
from termcolor import colored


def greeting():
    print(colored('===================================================', 'green'))
    print(colored('こんにちは！私はRobokoです。あなたの名前は何ですか？', 'green'))
    print(colored('Hello, I am Roboko. What is your name?', 'green'))
    print(colored('===================================================', 'green'))


def csv_has_data(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # ヘッダー行をスキップ

            for row in reader:
                if any(field.strip() for field in row):
                    return True  # 少なくとも1つの非空フィールドがある行を見つけた

        return False  # データが見つからなかった

    except FileNotFoundError:
        return False


def get_recommend_row(file_path):
    restaurants = {}
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                restaurants[row['NAME']] = int(row['COUNT'])
    except FileNotFoundError:
        pass

    sorted_keys = sorted(restaurants, key=restaurants.get, reverse=True)
    key_arr = []
    for key in sorted_keys:
        key_arr.append(key)

    return key_arr


def update_restaurant_count(file_path, favorite_restaurant):
    restaurants = {}
    # 既存のデータを読み込む
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                restaurants[row['NAME']] = int(row['COUNT'])
    except FileNotFoundError:
        pass  # ファイルが存在しない場合は新規作成

    # カウントを更新または新規追加
    if favorite_restaurant in restaurants:
        restaurants[favorite_restaurant] += 1
    else:
        restaurants[favorite_restaurant] = 1

    # 更新されたデータを書き込む
    with open(file_path, 'w', newline='') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for name, count in restaurants.items():
            writer.writerow({'NAME': name, 'COUNT': count})
