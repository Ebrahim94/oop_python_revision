class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total


    @classmethod
    def franchise(cls, store):
        new_store = cls(f"{store.name} - franchise")
        return new_store

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        return f"{store.name}, total stock price: {store.stock_price()}"
        # It should be in the format 'NAME, total stock price: TOTAL'

store = Store("Amazon")
store.add_item("item_1", 160)
print(Store.store_details(store))
