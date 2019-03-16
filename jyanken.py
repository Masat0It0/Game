#!/usr/bin/env python3
import const
import random

const.MSG_GOO = "グー"
const.MSG_CHOKI = "チョキ"
const.MSG_PA = "パー"

const.JANKEN_DIC = {"1": const.MSG_GOO, "2": const.MSG_CHOKI, "3": const.MSG_PA}
const.SENTAKU_LIST = ["1", "2", "3"]

const.MSG_KAKEGOE = "じゃーんけーん　ぽん！"
const.MSG_SENTAKU = "1.グー　2.チョキ　3.パー　1～3のいずれかを入力してください"

const.MSG_DRAW = '引き分け'
const.MSG_WIN = '勝ち'
const.MSG_LOSE = '負け'

try:
    print(const.MSG_SENTAKU)
    you = input('>>>  ')

    you_choice = const.JANKEN_DIC[you]
    pc_choice = const.JANKEN_DIC[random.choice(const.SENTAKU_LIST)]

    print(const.MSG_KAKEGOE)

    if you_choice == pc_choice:
        rslt = const.MSG_DRAW
    else:
        if you_choice == const.MSG_GOO:
            if pc_choice == const.MSG_CHOKI:
                rslt = const.MSG_WIN
            else:
                rslt = const.MSG_LOSE

        elif you_choice == const.MSG_CHOKI:
            if pc_choice == const.MSG_PA:
                rslt = const.MSG_WIN
            else:
                rslt = const.MSG_LOSE

        else:
            if pc_choice == const.MSG_GOO:
                rslt = const.MSG_WIN
            else:
                rslt = const.MSG_LOSE

    print("あなたの手：　{0}" .format(you_choice))
    print("あいての手：　{0}" .format(pc_choice))
    print("結　　　果：　{0}" .format(rslt))
except:
    print(const.MSG_SENTAKU)
