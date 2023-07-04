import users
import products


class Store:
    _counter = products.IdCounter()

    def __init__(self):  # product_generator):
        user = self.authentification()
        self.username = user
        self.product_generator = products.ProductGenerator()
        #  self._order_id = self._counter.get_new_id()

    def __str__(self):
        print("class Store Motor __str__")
        str_ = "Корзина пользователя: \n"
        for i in self.username._cart.get_data():
            str_ += str(i) + "\n"
        return str_

    def view_cart_(self):
        print(self.username._cart.get_data())

    def add_to_cart(self):
        while True:
            product = self.product_generator.get_product()
            print(product)
            bool_ = input("добавить товар в корзину? - y/n \n")
            if bool_ == 'y' or bool_ == 'Y':
                self.username._cart.add(product)
                continue
            else:
                return

    def remove_from_cart(self):
        while True:
            ind_ = int(input('введите индекс товара\n'))
            try:
                ind_ = int(ind_)
                if not isinstance(ind_, int):
                    raise TypeError()
                self.username._cart.remove(ind_)
                return
            except ValueError:
                print("ошибка индекса")
                continue

    @staticmethod
    def authentification():
        while True:
            login = input("Логин \n")
            try:
                if users.UserList.check_user_in_list(login):
                    print('Такой пользователь зарегистрирован')
                    user = users.UserList.get_user_from_list(login)
                    password = input("пароль \n")
                    password_h = user[2]
                    users.Password.check(password, password_h)

                else:
                    print('регистрация нового пользователя')

                    password = input("пароль \n")
                    user = users.User(login, password)
                return user
            except ValueError:
                print("ошибка аутентификации")
                continue

    def init(self):
        while True:
            st.add_to_cart()
            bool_ = input("показать товары в корзине? - y/n \n")
            if bool_ == 'y' or bool_ == 'Y':
                self.view_cart_()
                bool_ = input("хотите удалить товар? - y/n \n")
                if bool_ == 'y' or bool_ == 'Y':
                    self.remove_from_cart()
                else:
                    bool_ = input("продолжить? - y/n \n")
                    if bool_ == 'y' or bool_ == 'Y':
                        continue
                    else:
                        return
            else:
                return


if __name__ == "__main__":
    st = Store()
    new_cart = users.Cart()
    st.init()
