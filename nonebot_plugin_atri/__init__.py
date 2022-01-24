#!/usr/bin/python3
# coding: utf-8
import re
import random
from difflib import SequenceMatcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, GROUP, MessageSegment
from nonebot.plugin import on_command
from .data import atri_text
from .data import V_PATH

__plugin_name__ = "ATRI 语音包"
__usage__ = "atri"

atri = on_command("atri", permission=GROUP, priority=50)


@atri.handle()
async def _h(bot: Bot, event: GroupMessageEvent):
    words = str(event.message).strip()
    if words:
        diff: dict[str, float] = {}
        for text in atri_text:
            r1 = SequenceMatcher(None, words, text["s"]).ratio()
            r2 = SequenceMatcher(None, words, text["s_f"]).ratio()
            r3 = SequenceMatcher(None, words, text["s_k"]).ratio()
            diff.update({text["o"]: r1 * r2 + r3})  # 完全瞎想的计算方式，没啥特殊的意义
        diff_sorted = dict(
            sorted(diff.items(), key=lambda item: item[1], reverse=True))
        voice = random.choice(
            [
                list(diff_sorted.keys())[0],
                list(diff_sorted.keys())[1],
                list(diff_sorted.keys())[2],
            ]
        )
    else:
        voice = random.choice(atri_text)["o"]
    text = re.findall("(.*).mp3", voice)[0]
    await atri.send(MessageSegment.record(f"file:///{V_PATH}{voice}"))
    await atri.finish(text)