import csv

with open('4_files/scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    result = {}
    for row in reader:
        if row['name'] not in result:
            result[row['name']] = int(row['score'])
        else:
            result[row['name']] += int(row['score'])

    first = None
    score = -1
    for key, value in result.items():
        if value > score:
            score = value
            first = key
    
    print('The person with highest score is: '+first+' with score '+str(score))
    