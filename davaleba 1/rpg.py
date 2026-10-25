class Character:

    count = 0


    def __init__(self, name, hp=100, level=1):
        self.name = name
        self.hp = hp
        self.level = level

        Character.count += 1 # es mushaobs yvela obieqtze da ara individualurze

    def __str__(self):
        return f"{self.name} (Lv {self.level}, HP {self.hp})"

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    @property
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def attack(self, target):
        target.take_damage(5)



class Warrior(Character):
    def __init__(self, name, hp=100, level=1, strength=10):
        super().__init__(name, hp, level)
        self.strength = strength

    def attack(self, target):
        target.take_damage(self.strength)


class Mage(Character):
    def __init__(self, name, hp=100, level=1, mana=50):
        super().__init__(name, hp, level)
        self.mana = mana


    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(20)
        else:
            super().attack(target)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} MP {self.mana}"


class HealerMixin:
    def heal(self, target, amount):
        target.hp += amount


#amis mere gavwede
# :(((




a = Character("Tariel")
b = Character("Avtandil", hp=50)
b.take_damage(70)

print(a)                 # Tariel (Lv 1, HP 100)
print(b)                 # Avtandil (Lv 1, HP 0)
print(b.is_alive)        # False
print(Character.count)   # 2

t = Warrior("Tariel", hp=120, strength=15)
n = Mage("Nestan", hp=80, mana=15)

t.attack(n)
print(n)    # Nestan (Lv 1, HP 65) MP 15

n.attack(t)   # 20 ზიანი, mana-ს 5 რჩება
n.attack(t)   # mana არ ჰყოფნის: 5 ზიანი
print(t)    # Tariel (Lv 1, HP 95)