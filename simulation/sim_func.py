def self_get_next_index_of_bias(self, step, len_of_number):
    """
    Функция получения смещения.
    Используется для получения условия на основе числа смещения
    [...33,43,24,...]
    [... 5, 6, 7,...]
    Пример self.ptr = 5
           step = 1
           index = 6
    Так как мы к self.ptr прибавили step и получили индекс смешение по гену
    len_of_number число ограничитель (К примеру если len_of_number является len(cfg.move_directions)
    то мы получим значение ограниченное количеством направлений от числа в гене
    43 % 8 - кол-во направлений = 3 - Вправо и низ)
    """
    index = (self.ptr + step) % len(self.genome)  # Индекс смещения
    index_of_bias = self.genome[index] % len_of_number
    return index_of_bias


def self_get_next_index(self, step):
    """
    Функция получения следующего индекса смешения
    используется для увеличения УТК на число полученное в смешении
    [...33,43,24,...]
    [... 5, 6, 7,...]
    Пример self.ptr = 5
           step = 1
           index = 6
    В данном примере УТК переместится на 43 (и остановится на 48) от позиции где он находился (Это self.ptr = 5)
    """
    index = (self.ptr + step) % len(self.genome)
    ptr = (self.ptr + self.genome[index]) % len(self.genome)
    return ptr


def self_get_bias(self, step):
    index = (self.ptr + step) % len(self.genome)
    bias = self.genome[index]
    return bias


def move_ptr_to(self):
    # Перемещение УТК к следующей команде на основе числа безусловного перехода
    self.ptr = (self.ptr + self.genome[self.ptr]) % len(self.genome)


# Функция перемещения указателя текущей команды
def move_ptr(self):
    # Перемещения УТК к следующей команде
    self.ptr = (self.ptr + 1) % len(self.genome)


def get_colors_bias(self):
    colors = [0, max(min(self.genome[0] % 255, 190), 140),
              max(min(self.genome[0] % 255, 80), 70), 255
              ]
    return colors
