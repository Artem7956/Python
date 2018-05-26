cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }

def make_ingridient(ist):
    ing={}
    tmp_ist=[]
    tmp_ist=ist.split('|')
    #print(tmp_ist)
    ing['ingridient_name']=tmp_ist[0].rstrip()
    ing['quantity'] = tmp_ist[1].strip()
    ing['measure'] = tmp_ist[2].lstrip()
    return(ing)

cb1={}
f = open('cook','r',encoding='utf-8')

for line in f:

    dish = line
    ing_count = f.readline()

    #print ('dish',dish)
    #print('count',ing_count)
    ingridient=[]
    i=1
    while i <= int(ing_count):
        tmp_ing=f.readline()
        #print('dfgdgd',tmp_ing)
        ingridient.append(make_ingridient(tmp_ing.replace('\n','')))

        i += 1
    cb1[dish.replace('\n','')] = ingridient
    f.readline()
    #print(ingridient)
print(cb1)
    #print(dish)
def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=new_shop_list_item['quantity']
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

#create_shop_list()