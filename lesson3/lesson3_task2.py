from smartphone import Smartphone

catalog = [
    Smartphone('marka1', 'model1', '+7963....'),
    Smartphone('Marka2', 'Model2', '+7909....'),
    Smartphone('marka3', 'model3', '+7982...'),
    Smartphone('Marka4', 'model4', '+7919....'),
    Smartphone('marka5', 'Model5', '+7912....')
]

for smartphone in catalog:
    print(f'{smartphone.marka} - {smartphone.model}. {smartphone.nomer}')