class GroceryList:
    def __init__(self):
        self.items = {}

    def add_recipe(self, recipe):
        for ingredient in recipe.ingredients:
            name = ingredient["name"]
            quantity = ingredient["quantity"]

            if name in self.items:
                # Можно реализовать более умную логику для объединения количества, например, для единиц измерения
                self.items[name] += quantity
            else:
                self.items[name] = quantity

    def remove_recipe(self, recipe):
        for ingredient in recipe.ingredients:
            name = ingredient["name"]
            quantity = ingredient["quantity"]

            if name in self.items:
                # Можно реализовать более умную логику для удаления количества, например, для единиц измерения
                self.items[name] -= quantity

                if self.items[name] <= 0:
                    del self.items[name]

    def filter_by_preferences(self, preferences):
        for pref in preferences:
            for item in list(self.items.keys()):
                if pref.lower() in item.lower():
                    del self.items[item]

    def __str__(self):
        return "Grocery List:\n" + "\n".join([f"{name}: {quantity}" for name, quantity in self.items.items()])

    def __repr__(self):
        return f"GroceryList({str(self.items)})"