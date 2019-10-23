
def getInfo(items):
    response = {}
    aliments = {'Pomme': {'Price': '1', 'Energie': '130kcal', 'Total Fat': '0g', 'Total Carbohydrate' : '34g','Protein':'1g'},
               'Banane': {'Price': '0.70', 'Energie': '105kcal', 'Total Fat': '0g', 'Total Carbohydrate' : '27g','Protein':'1g'},
               'Coke':{'Price': '1.2', 'Energie': '211kcal', 'Total Fat': '0g', 'Total Carbohydrate' : '53g','Protein':'0g'},
               'RizBlanc' : {'Price': '0.40', 'Energie':  '136kcal','Total Fat': '0.3g', 'Total Carbohydrate': '29.4g', 'Protein':'2.8g'},
               'SteakHaché' : {'Price': '1.37', 'Energie':  '168kcal','Total Fat': '10.9g', 'Total Carbohydrate': '0g', 'Protein':'16.3g'},
               'FiletPoulet' : {'Price': '1.47', 'Energie':  '164kcal','Total Fat': '3.5g', 'Total Carbohydrate': '0g', 'Protein':'34g'},
               'PoissonMerloin' : {'Price': '1.55', 'Energie':  '98<kcal','Total Fat': '1.3g', 'Total Carbohydrate': '0.3g', 'Protein':'21.4g'},
               'LentilesVerts' : {'Price': '0.60', 'Energie':  '116kcal','Total Fat': '0.4g', 'Total Carbohydrate': '20g', 'Protein':'9g'},
               'Carrot' : {'Price': '0.35', 'Energie':  '40kcal','Total Fat': '0.2g', 'Total Carbohydrate': '7g', 'Protein':'1.1g'},
               'Broccoli' : {'Price': '0.60', 'Energie':  '35kcal','Total Fat': '0.6g', 'Total Carbohydrate': '7g', 'Protein':'2g'},
               'FiletCanard' : {'Price': '2.03', 'Energie':  '159kcal','Total Fat': '9g', 'Total Carbohydrate': '0g', 'Protein':'19.6g'},
               'PoisVertes' : {'Price': '0.37', 'Energie':  '101kcal','Total Fat': '2.5g', 'Total Carbohydrate': '15.2g', 'Protein':'5.2g'},
               'Frites' : {'Price': '0.40', 'Energie':  '274kcal','Total Fat': '14.1g', 'Total Carbohydrate': '35.7g', 'Protein':'3.5g'}}
    
    for i in range(len(items)):
        response[items[i]] = aliments[items[i]]
        
    return response
