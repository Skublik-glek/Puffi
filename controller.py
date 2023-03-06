from gui_elements import *
import pygame as pg
from sound_manager import *


import random

background = Background('data/pictures/background.jpg')
new_text = Update_text("""Добропожаловать в дивижок визуальных новелл""")
choises = Choises({})
choises.active = False
game_gui = Game_gui(sc, background, new_text, choises)
sound_manager = Music("data/music/embient.mp3")


class Character():
    def __init__(self, name):
        self.name = name
        self.ultimate_status = True

    def ability(self):
        pass

    def ultimate(self):
        pass


class Pufi(Character):
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        super().ability()
        return "Flight"

    def ultimate(self):
        super().ultimate()
        if self.ultimate_status:
            self.ultimate_status = False
            return "Hurricane."
        else:
            return "None"


class GrandpaVacuumCleaner(Character):
    def __init__(self, name):
        super().__init__(name)

    def ability(self):
        super().ability()
        return "Throw stone"

    def ultimate(self):
        super().ultimate()
        if self.ultimate_status:
            self.ultimate_status = False
            return "Offense"
        else:
            return "None"


class GrandmaVacuumCleaner(Character):
    def __init__(self, name):
        super().__init__(name)
        self.ultimate_status = False

    def ability(self):
        super().ability()
        return "A ladle."

    def ultimate(self):
        super().ultimate()
        return "Borsch."


class StartLocacion():
    def __init__(self, character: Character):
        self.character = character
        game_gui.background.send("data/pictures/background.jpg")
        game_gui.choises.choises = {}
        game_gui.choises.active = False
        game_gui.choises.done = False
        sound_manager.play()
        game_gui.update_text.send_text(text="""Вы в долине пылесосов смотрите новости, и вдруг а в телеэфир взрывается незнакомец Говорит, что
старые проводные пылесосы вышли из моды""")
        self.next_action = self.next
                                       
    def next(self):
        if game_gui.update_text.done and not game_gui.choises.done:
            game_gui.choises.send({"Пример ответа, возвращает 1": [1, pg.Color('white'), pg.Color('lightgreen'), pg.Color('black')]})
        if game_gui.choises.result == 1:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Вы вышли из своего дом на поиски золотой щепки спустя три Долгих дня вы под подошли 
к болоту фабрика где сидел главный робот пылесос было совсем близко но вы понимаете что через болото просто так не перебраться 
у вас есть три варианта как его пройти""")
            game_gui.background.send("data/pictures/picture1.jpg")
            game_gui.choises.done = False
            self.next_action = self.next2
                                           
    def next2(self):
        if game_gui.update_text.done and not game_gui.choises.done:
            game_gui.choises.send({"Ответ 1": [1, pg.Color('white'), pg.Color('lightgreen'), pg.Color('black')], 
                                   "Ответ 2": [2, pg.Color('white'), pg.Color('yellow'), pg.Color('black')],
                                   "Ответ 3": [3, pg.Color('white'), pg.Color('red'), pg.Color('black')]})
        if game_gui.choises.result == 2:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Конец теста!!! Вы выбрали 2""")
        if game_gui.choises.result == 1:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Конец теста!!! Вы выбрали 1""")
        if game_gui.choises.result == 3:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Конец теста!!! Вы выбрали 3""")
        



class TinaKandelaki():
    def __init__(self, character: Character):
        self.character = character
        print(""""Вы вышли из своего дом на поиски золотой щепки спустя три Долгих дня вы под подошли 
        к болоту фабрика где сидел главный робот пылесос было совсем близко но вы понимаете что через болото просто так не перебраться 
        у вас есть три варианта как его пройти
""")
        print("Выберите 1 из 3 дверей")

class BossFight():
    def __init__(self, character: Character):
        self.character = character
        self.health = 100
        self.action = 0

        self.boss_health = 350
        self.boss_activity = "Ничего не делает"


        # принт сюжета



    def step(self):
        print(f"""Ваш ход!

Состояние персонажа:
Здоровье: {self.health}

Состояние босса:
Здоровье: {self.boss_health}
Активность босса: {self.boss_activity}


Выберите действие:
1 - Атаковать
2 - Увернуться 
3 - Восстановить здоровье""")

        while True:
            try:
                self.action = int(input())
                if self.action not in range(1, 4):
                    print("Введите правильное значение!")
                    continue
                break
            except Exception:
                print("Введите правильное значение!")

        if self.action == 1:
            dmg = random.randint(8, 20)
            crit = 1.0
            if self.boss_activity == "Замахивается":
                crit = 2.2
            self.boss_health -= dmg * crit
            if crit != 1.0:
                print(f"Вы кританули!\nВаш урон: {dmg * crit}\nЗдоровье боса: {self.boss_health}")

        if self.action == 3:
            if self.health != 100:
                self.health += 10
                if self.health > 100:
                    self.health = 100
                print(f"Вы восстановили 10 здоровья, ваше здоровье {self.health}")
            else:
                print("Здоровье максимальное!")

        if self.action == 2:
            print("Вы уворачиваетесь")

        if self.boss_health <= 0:
            return 1
        else:
            return 0

    def bossStep(self):
        pass


start_location = StartLocacion(Pufi(name="Пуфи"))