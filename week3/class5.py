class super:
    def fruit(self):
        print('사과')

class serve(super):
    def fruit(self):
        print('파인애플')

fruitName = serve()
fruitName.fruit()
