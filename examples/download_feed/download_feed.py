import csv
import tqdm
from lemon8 import Lemon8

if __name__ == "__main__":
    keys = ['groupId', 'articleClass', 'canonicalUri', 'articleLikes', 'title', 'shortContent']
    lemon8 = Lemon8()
    with open('people.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore')
        for n in tqdm.tqdm(range(10)):
            try:
                to_csv = lemon8.feed('foryou').get_items() 
                if n == 0:
                    dict_writer.writeheader()
                dict_writer.writerows(to_csv)
            except Exception as e:
                print(e)