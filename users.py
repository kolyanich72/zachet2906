import hashlib
import motor
import products
from products import IdCounter


class Cart:  # класс Cart (корзина в котором хранится информация о списке товаров)

    def __init__(self):
        self._data = []

    def __repr__(self):
        str_ = " class Cart __repr__: \n"
        for i in self._data:
           str_ += str(i) + "\n"
        return str_

    def add(self, product):
        self._data.append(product)

    def __len__(self):
        return len(self._data)

    def remove(self, index: int):

        for i in self._data:
            while True:
                try:
                    if i._id == index:
                        self._data.remove(i)
                        return
                except ValueError:
                    print("ошибка индекса")
                    continue

    def get_data(self):
        str_ = "Ваша корзина: \n"
        for i in self._data:
           str_ += f"{i}\n"  # {l2} {l1} \n
        return str_


class UserList:

    usr_list = []

    @classmethod
    def add_to_list(cls, _id, user_name, password):

        l1 = [_id, user_name, password]
        cls.usr_list.append(l1)

    @classmethod
    def get_user_from_list(cls, user_name: str):
        for i in cls.usr_list:
            if user_name in i:
                return i

    @classmethod
    def check_user_in_list(cls, user_name: str):
        for i in cls.usr_list:
            if user_name in i:
                return True
            else:
                return False


class User:

    _counter = IdCounter()

    def __init__(self, username, password):

        self._id = self._counter.get_new_id()
        self.username_new = username
        self.__password = Password.get(password)
        UserList.add_to_list(self._id, self._username, self.__password)

        self._cart = Cart()

    def __str__(self):
        return f"username: {self._username} "

    def __repr__(self):
        return f" user id:{self._id} username:{self._username} password: <password>"

    @property
    def get_username(self):
        return self._username

    @get_username.setter
    def username_new(self, username):
      self._username = username

    def get_user_name(self, username):
        if username in self.usr_list:
            return True


class Password:
    @classmethod
    def get(cls, password: str):

        cls.is_valid(password)
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def is_valid(password: str):
        if not password.isalnum() or len(password) < 8:
            print('пароль должен состоять из 8 и более символов - цифр и букв')
            raise ValueError
        return True

    @classmethod
    def check(cls, password, hash_password):
        if cls.get(password) != hash_password:
            raise ValueError("введите правильный пароль")


if __name__ == "__main__":
    user1 = User('user1111', "qwerty123")
    user2 = User('user22222', "qwerty1234")
    user3 = User('user33', "qwerty123")
    pr1 = products.Product('nuts', 54, 4)
    pr2 = products.Product('tyres', 154, 7)
    user3._cart.add(pr2)
    user3._cart.add(pr1)
    print(user3._cart.get_data())
