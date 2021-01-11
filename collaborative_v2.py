import pandas as pd
import collections
import copy

df = pd.read_csv('en_son.csv')

tmp_dict = {
    'icecekler': [],
    'kebaplar': [],
    'corbalar': [],
    'baslangiclar': [],
    'izgaralar': [],
    'durumler': [],
    'pideler': [],
    'tatlilar': []
}

rejected_cats = ['icecekler', 'tatlilar']

def getIds(df, foods):
    tmps = list()
    for food in foods:
        tmps.append(list(df[df.MenuItem == food]['Id']))
    
    tmps = [id_ for tmp in tmps for id_ in tmp]

    if len(foods) == 1:
        return tmps
    final = [item for item, count in collections.Counter(tmps).items() if count > len(foods) - 1]
    return final or -1

def getFoodsFromIds(df, ids, foods):
    result = copy.deepcopy(tmp_dict)
    for id_ in ids:
        order = df[df.Id == id_]
        for _, row in order.iterrows():
            if(row['MenuItem'] not in foods):
                category = row['Category']
                result[category].append(row['MenuItem'])
    
    return result

def getMostPreferredList(filename, foods):
    df = pd.read_csv(filename)
    ids = getIds(df, foods)
    if ids == -1:
        return -1
    int_dict = getFoodsFromIds(df, ids, foods)     
    for cat in list(int_dict):
        if(not int_dict[cat]):
            del int_dict[cat]
            continue

        freq = collections.Counter(int_dict[cat]).most_common()
        
        if(cat == 'baslangiclar'):
            int_dict[cat] = freq[:1]
            continue
        int_dict[cat] = freq[:2]
    
    return int_dict

if __name__ == "__main__":
    final = getMostPreferredList('son.csv', ['Adana Kebap', 'Sprite', 'Kuruluk Dolması'])
