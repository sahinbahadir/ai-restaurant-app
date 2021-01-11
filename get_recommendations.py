import pandas as pd
import collections

CATEGORIES = ['kebaplar', 'corbalar', 'baslangiclar', 'izgaralar', 'durumler', 'pideler', 'icecekler', 'tatlilar']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_template = {
    '09:00-10:00': [],
    '10:00-11:00': [],
    '11:00-12:00': [],
    '12:00-13:00': [],
    '13:00-14:00': [],
    '14:00-15:00': [],
    '15:00-16:00': [],
    '16:00-17:00': [],
    '17:00-18:00': [],
    '18:00-19:00': [],
    '19:00-20:00': [],
    '20:00-21:00': [],
    '21:00-22:00': [],
    '22:00-23:00': []
}

# FILENAME -> str, DAY -> int, INTERVAL -> str

def popularityBased(FILENAME, DAY, INTERVAL):   
    df = pd.read_csv(FILENAME)

    for _, row in df.iterrows():
        day = days.index(row['Day'])
        time = row['DateTime'][11:13]
        
        if DAY == day and INTERVAL[:2] == time:
            df_template[INTERVAL].append(row['Category'] + ',' + row['MenuItem'])

    freq = collections.Counter(df_template[INTERVAL])
    return getMostFrequents(freq.most_common())

def getMostFrequents(freq_list):
    int_dict = {key: [] for key in CATEGORIES}
    final_dict = {key: [] for key in CATEGORIES}

    for cat in CATEGORIES:
        for result in freq_list:
            result_str = result[0].split(',')
            w_cat = result_str[0]
            if w_cat == cat:
                int_dict[cat].append([result[1], result_str[1]])

    for cat in CATEGORIES:
        sum_ = 0
        for i in range(3):
            try:
                sum_ += int_dict[cat][i][0]
            except IndexError:
                break
                

        for i in range(3):
            try:
                perc = round((int_dict[cat][i][0] / sum_) * 100.0, 1)
                food = int_dict[cat][i][1]
                final_dict[cat].append([perc, food])
            
            except IndexError:
                break

    return final_dict

if __name__ == "__main__":
    # print(popularityBased('son.csv', 4, '11:00-12:00'))
    print(popularityBased('son.csv', 3, '13:00-14:00'))