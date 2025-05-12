import pandas as pd

data = {
    'HSNCode': ['01', '0101', '010121', '01012100', 
                '02', '0201', '020110', '02011000'],
    'Description': ['Live Animals',
                   'Live horses, asses, mules and hinnies',
                   'Pure-bred breeding animals',
                   'Pure-bred breeding horses',
                   'Meat and edible meat offal',
                   'Meat of bovine animals, fresh or chilled',
                   'Carcasses and half-carcasses',
                   'Bovine carcasses, fresh or chilled']
}

df = pd.DataFrame(data)
df.to_csv('HSN_Master_Data.csv', index=False)
