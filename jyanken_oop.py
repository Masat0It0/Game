### sources;
### better write rock paper scissors (python)
### https://stackoverflow.com/questions/49630723/better-write-rock-paper-scissors-python

import random

### *1 @classmethod 
### @classmethodをデコレーターで定義
### *2 random.choice()


class Hand:

    _ordering = {
        'rock': 'scissor',
        'scissor': 'paper',
        'paper': 'rock'
    }

    def __init__(self, kind):
        if kind in self._ordering:
            self.kind = kind
        else:
            raise ValueError(
                "It's rock, paper, scissor... Not rock, {}, scissor.".format(kind)
            )

    ### *1 @classmethod 
    ### @classmethodをデコレーターで定義 
    ### selfを使わない場合、@classmethodをデコレーターで定義
    ### このとき第一引数には、cls
    ### selfを使わないときはどのようなケースか
    ### クラス変数にアクセスすべきときや、継承クラスで動作が変わるべき
    ### sources;
    ### Pythonで classmethod、staticmethod を使う
    ### https://qiita.com/msrks/items/fdc9afd12effc2cba1bc
    @classmethod
    def random_hand(cls):
        ### *2 random.choice()
        ### random.choice(list)のlistから無作為に抽出
        ### ここでは、 ['rock', 'scissor', 'paper']からひとつ抽出される
        tmp = list(cls._ordering)
        print('list(cls._ordering): {}'.format(tmp))
        ### list(cls._ordering): ['rock', 'scissor', 'paper']
        print('random.choice(tmp): {}'.format(random.choice(tmp)))
        ### random.choice(tmp): scissor
        return cls(random.choice(tmp))
        #return cls(random.choice(list(cls._ordering)))

    def beats(self, other):
        return self._ordering[self.kind] == other.kind

#グー、チョキ、パーのいずれかを入力してください
player_hand = Hand(input("Play rock, paper or scissor please: "))

cpu_hand = Hand.random_hand()

if player_hand.beats(cpu_hand):
    print(
        "Player won!\nPlayer's hand is {}\nCPU's hand is {}.".format(player_hand.kind, cpu_hand.kind)
    )
elif cpu_hand.beats(player_hand):
    print(
        "Player lost!\nPlayer's hand is {}\nCPU's hand is {}.".format(player_hand.kind, cpu_hand.kind)
    )
else:
    print(
        "It's a draw.\nPlayer's hand is {}\nCPU's hand is {}.".format(player_hand.kind, cpu_hand.kind)
    )
