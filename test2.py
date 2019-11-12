class Rett: 
    def __init__(self, name, price, ingredients):
        self._name = name
        self._price = price
        self._ingredients = ingredients
        print('Name: {} Price: {} Ingredients: {}'.format(self._name,self._price,self._ingredients))
    def sjekkInnholdOK(self, substances):
        for substance in substances:
            if substance in self._ingredients:
                return False
        return True
        
    def __str__(self):
        return 'Name: {} Price: {} Ingredients: {}'.format(self._name,self._price,self._ingredients)

ingredients = ["tomato","chicken","cheese"]
substances = ["apple","potato","chicken"]
obj = Rett("salad",10, ingredients)
print(obj.sjekkInnholdOK(substances))
# print(obj)
