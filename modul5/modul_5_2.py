articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    dict_new = []
    for item in articles_dict:
        print(item['title'].find(key))
        print(item['author'].find(key))

  #      for value in item.values():
        if item['title'].find(key)!= -1 or item['title'].find(key.upper()) !=-1:
                dict_new += dict_new[item]

        if item['author'].find(key)!= -1 or item['author'].find(key.upper()) !=-1:
                dict_new += dict_new[item]


    return dict_new

print(find_articles("Golden"))
    
