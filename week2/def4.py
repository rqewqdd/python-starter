def get_info(fruit_list, fruit_name, keyname):
    print(fruit_list[fruit_name][keyname])

name = input()

fruit = {'banana': {'price': 1000, 'stock': 10},
         'orange': {'price': 2000, 'stock': 20}}

get_info(fruit, name, 'price')
get_info(fruit, name, 'stock')


# def get_prcie(fruit_list, fruit_name):
#     print(fruit_list[fruit_name]['price'])
#
# def get_stock(fruit_list, fruit_name):
#     print(fruit_list[fruit_name]['stock'])
#
# name = input()
#
# fruit = {'banana': {'price': 1000, 'stock': 10},
#          'orange': {'price': 2000, 'stock': 20}}
#
# get_prcie(fruit, name)
# get_stock(fruit, name)


# def get_prcie(fruit_list):
#     fruit = {'banana':{'price':1000,'stock':10},
#          'orange':{'price':2000,'stock':20}}
#     print(fruit[fruit_list]['price'])

# def get_stock(fruit_list):
#     fruit = {'banana':{'price':1000,'stock':10},
#          'orange':{'price':2000,'stock':20}}
#     print(fruit[fruit_list]['stock'])

# fruit = input()
#
# get_prcie(fruit)
# get_stock(fruit)