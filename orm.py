from entity import Entity


class Category(Entity):
    fields = ['id', 'title']

    def __init__(self, _id=None):
        self._title = None

        super().__init__()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._changed = True


class Item(Entity):
    fields = ['id', 'title', 'price', 'category_id']

    def __init__(self, _id=None):
        self._title = None
        self._price = None
        self._category_id = None

        super().__init__(_id)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self._changed = True

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        self._changed = True

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
        self._changed = True
