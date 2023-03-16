from gui_elements import *
import pygame as pg
from sound_manager import *


import random


class Loc_manager():
    def __init__(self, loc):
        self.loc = loc


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
        game_gui.background.send("data/pictures/start_loc2.jpg")
        sound_manager.play_new("data/music/pufiost2.mp3")
        game_gui.choises.choises = {}
        game_gui.choises.result = None
        game_gui.choises.active = False
        game_gui.choises.done = False
        game_gui.update_text.send_text("""Вы  спите у себя дома как вдруг  вас будет  громкий звук вы просыпаетесь""")
        self.next_action = self.next
                                       
    def next(self):
        if game_gui.update_text.done and not game_gui.choises.done:
            game_gui.choises.send({
                                   "Встать и покормить домашнее животное": [2, pg.Color('black'),
                                                                            pg.Color('lightgreen'),
                                                                            pg.Color('white')],
                                   "Встать и спрятаться Вниз": [3, pg.Color('black'),
                                                                     pg.Color('lightgreen'),
                                                                     pg.Color('white')]})
        if game_gui.choises.result == 1 or game_gui.choises.result == 3:
            game_gui.choises.result = None
            game_gui.update_text.send_text("""Вы обязательно должны покормить домашний тостер""")
            game_gui.choises.done = False
            self.next_action = self.next
        if game_gui.choises.result == 2:
            game_gui.choises.result = None
            game_gui.update_text.send_text("""Вы покормили своего питомца""")
            game_gui.choises.done = False
            self.next_action = self.next2

    def next2(self):
        if game_gui.update_text.done and not game_gui.choises.done:
            game_gui.choises.send({
                                   "Встать и спрятаться  На нижний этаж": [2, pg.Color('black'),
                                                                     pg.Color('lightgreen'),
                                                                     pg.Color('white')]})
        if game_gui.choises.result == 2:
            game_gui.choises.result = None
            game_gui.choises.done = False
            loc_manager.loc = podval_loc(self.character)
        if game_gui.choises.result == 1:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Конец теста!!! Вы выбрали 1""")
        if game_gui.choises.result == 3:
            game_gui.choises.result = None
            game_gui.update_text.send_text(text="""Конец теста!!! Вы выбрали 3""")


class podval_loc():
    def __init__(self, character: Character):
        self.character = character
        game_gui.background.send("data/pictures/podval_loc3.jpg")
        game_gui.choises.choises = {}
        game_gui.choises.active = False
        game_gui.choises.done = False
        game_gui.update_text.send_text("""Вы Спустились  Вниз""")
        self.next_action = self.next

    def next2(self):
        if game_gui.update_text.done and not game_gui.choises.done:
            game_gui.choises.result = None
            game_gui.choises.done = False
            game_gui.update_text.send_text("""Достижения половая тряпка получена""")
            self.next_action = self.next

    def next(self):
        if game_gui.update_text.done and not game_gui.choises.done:
                game_gui.choises.send({"Выйти из Дома": [1, pg.Color('black'), pg.Color('lightgreen'),
                                                                  pg.Color('white')],
                                       "Остаться Дома": [2, pg.Color('black'),
                                                                                pg.Color('lightgreen'),
                                                                                pg.Color('white')]})
        if game_gui.choises.result == 2:
            game_gui.choises.result = None
            game_gui.choises.done = False
            self.next_action = self.next2

        if game_gui.choises.result == 1:
            game_gui.choises.result = None
            game_gui.choises.done = False
            loc_manager.loc = street_loc(self.character)



class street_loc():
    def __init__(self, character: Character):
        self.character = character
        game_gui.background.send("data/pictures/street_loc.jpg")
        game_gui.choises.choises = {}
        game_gui.choises.active = False
        game_gui.choises.done = False
        game_gui.update_text.send_text("""Вы вышли из дома и видите как гигантский летающий робот пылесос засасывает всю вашу деревню со всеми жителями и видите 
как он улетает на старый завод  чтоб спасти весь свой народ 
пылесосов вы решили добраться до главного босса и отомстить ему """)
        self.next_action = self.next
        
    def next(self):
        if game_gui.next_text and game_gui.update_text.done and not game_gui.choises.done:
            game_gui.next_text = False
            loc_manager.loc = TinaKandelaki(self.character)
class TinaKandelaki():
    def __init__(self, character: Character):
        self.character = character
        game_gui.background.send("data/pictures/boloto_loc.jpg")
        sound_manager = Music("data/music/долико.mp3")
        game_gui.choises.choises = {}
        game_gui.choises.active = False
        game_gui.choises.done = False
        game_gui.update_text.send_text("""спустя три Долгих дня вы под подошли к болоту. фабрика, где сидел главный 
робот пылесос, была совсем близко, но вы понимаете ,что 
через болото просто так не перебраться. У вас есть три варианта, как его пройти
    """)
        self.next_action = self.next

    def next(self):
        pass

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


background = Background('data/pictures/background.jpg')
new_text = Update_text("""Добропожаловать в дивижок визуальных новелл""")
choises = Choises({})
choises.active = False
game_gui = Game_gui(sc, background, new_text, choises)
sound_manager = Music("data/music/pufiost2.mp3")
loc_manager = Loc_manager(StartLocacion(Pufi(name="Пуфи")))