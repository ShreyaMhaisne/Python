class ToyBox:
    def __init__(self):
        self._ball = "Bouncy Ball"    # can take, but not always safe
        self.__secret = "Magic Toy"   # private

    def show_secret(self):
        return self.__secret

box = ToyBox()
print(box._ball)           # 🟡 Allowed (but not best)
# print(box.__secret)      ❌ Not allowed
print(box.show_secret())   # ✅ Okay via function
