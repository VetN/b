
class Animal:
    '''питомник кошек и собак
    человек забирает всегда самого старшего первого в очереди '''

    # создаем список
    def __init__(self):
        self.dog = []
        self.cat = []
        self.order = 0

    # создаем словарь с характ животного и присваиваим сквозной номер очереди
    def add_animal(self, name, view):
        view = view.lower() # переводим все в нижний регистр чтобы избежать ошибок ввода
        self.order += 1 # присваиваем номер очереди
        animal = {
            "name": name,
            "view": view,
            "order": self.order
        }

        # сортируем входящих животных
        if view == "dog":
            self.dog.append(animal)
        elif view == "cat":
            self.cat.append(animal)
        else:
            print("Такого животного нет в питомнике")

        # создаем методы отдачи животных выбор либо из кошек или собак или любого

    # создаем общий метод(инкапсуляцией те внутренний двойная нижняя черта) в нем создаем общий список животных             }
    def __take_animal(self, animal_list):
        print("jj", animal_list)
        if len(animal_list) == 0:
            return None
        return animal_list.pop(0)

    # создаем отдельные методы и в них возвращ список животного
    def take_cat(self):
        return self.__take_animal(self.cat)

    def take_dog(self):
        return self.__take_animal(self.dog)


    # если берем любого, то создаем несколько условий
    def take_any(self):

        if len(self.cat) == 0: #если котов нет, то включ метод собак
            return self.take_dog()

        elif len(self.dog) > 0 and self.cat[0]["order"] > self.dog[0]["order"]:
        # если есть собаки и номер кошки выше(те она пришла позже) берем собаку
            return self.take_dog()

        else:
            return self.take_cat() # если кошка старше



        
#необх учит временную сложность. т.е. работа в методах должна занимать один время здесь она 0(1)
#проверка
s = Animal()
s.add_animal("Tory", "dog")
s.add_animal("Grom", "dog")
s.add_animal("Tim", "dog")
s.add_animal("Musya", "cat")
s.add_animal("Kiss", "cat")
print(s.dog)# выводим список
print(s.cat)

# включ метод take

s.take_dog()
s.take_any()
print(s.dog)
print(s.cat)



