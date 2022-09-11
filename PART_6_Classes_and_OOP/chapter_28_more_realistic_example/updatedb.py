import shelve
with shelve.open('persondb') as db:
    for key in sorted(db):
        print(key, '\t=>', db[key])
    sue = db['Sue Jones']
    sue.give_raise(.10)
    db['Sue Jones'] = sue