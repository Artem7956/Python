# cook_book1 = {
# 'яйчница': [
#   {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#   {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#   ],
# 'стейк': [
#   {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#   {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#   {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#   ],
# 'салат': [
#   {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#   {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#    ]
#  }


def make_ingridient(ist):
    ing = {}

    tmp_ist = ist.split('|')

    ing['ingridient_name'] = tmp_ist[0].rstrip()
    ing['quantity'] = int(tmp_ist[1].strip())
    ing['measure'] = tmp_ist[2].lstrip()
    return ing


cook_book = {}
f = open('cook', 'r', encoding='utf-8')

for line in f:

    dish = line
    ing_count = f.readline()
    ingridient = []
    i = 1
    while i <= int(ing_count):
        tmp_ing = f.readline()
        ingridient.append(make_ingridient(tmp_ing.replace('\n', '')))

        i += 1
    cook_book[dish.replace('\n', '').lower()] = ingridient
    f.readline()

print(cook_book)
f.close()


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()