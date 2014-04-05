# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
from .compat import text_type


class Converter(object):
    z_ascii = (
        "ａ", "ｂ", "ｃ", "ｄ", "ｅ", "ｆ", "ｇ", "ｈ", "ｉ",
        "ｊ", "ｋ", "ｌ", "ｍ", "ｎ", "ｏ", "ｐ", "ｑ", "ｒ",
        "ｓ", "ｔ", "ｕ", "ｖ", "ｗ", "ｘ", "ｙ", "ｚ",
        "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ",
        "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｑ", "Ｒ",
        "Ｓ", "Ｔ", "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ",
        "！", "”", "＃", "＄", "％", "＆", "’", "（", "）",
        "＊", "＋", "，", "−", "．", "／", "：", "；", "＜",
        "＝", "＞", "？", "＠", "［", "￥", "］", "＾", "＿",
        "‘", "｛", "｜", "｝", "〜", "　")

    z_digit = (
        "０", "１", "２", "３", "４",
        "５", "６", "７", "８", "９")

    z_kana = ("ア", "イ", "ウ", "エ", "オ",
              "カ", "キ", "ク", "ケ", "コ",
              "サ", "シ", "ス", "セ", "ソ",
              "タ", "チ", "ツ", "テ", "ト",
              "ナ", "ニ", "ヌ", "ネ", "ノ",
              "ハ", "ヒ", "フ", "ヘ", "ホ",
              "マ", "ミ", "ム", "メ", "モ",
              "ヤ", "ユ", "ヨ",
              "ラ", "リ", "ル", "レ", "ロ",
              "ワ", "ヲ", "ン",
              "ァ", "ィ", "ゥ", "ェ", "ォ",
              "ッ", "ャ", "ュ", "ョ", "ヴ",
              "ガ", "ギ", "グ", "ゲ", "ゴ",
              "ザ", "ジ", "ズ", "ゼ", "ゾ",
              "ダ", "ヂ", "ヅ", "デ", "ド",
              "バ", "ビ", "ブ", "ベ", "ボ",
              "パ", "ピ", "プ", "ペ", "ポ",
              "。", "、", "・", "゛", "゜", "「", "」", "ー")

    h_ascii = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z",
        "!", '"', "#", "$", "%", "&", "'", "(", ")",
        "*", "+", ",", "-", ".", "/", ":", ";", "<",
        "=", ">", "?", "@", "[", "\\", "]", "^", "_",
        "`", "{", "|", "}", "~", " ")

    h_digit = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    h_kana = ("ｱ", "ｲ", "ｳ", "ｴ", "ｵ",
              "ｶ", "ｷ", "ｸ", "ｹ", "ｺ",
              "ｻ", "ｼ", "ｽ", "ｾ", "ｿ",
              "ﾀ", "ﾁ", "ﾂ", "ﾃ", "ﾄ",
              "ﾅ", "ﾆ", "ﾇ", "ﾈ", "ﾉ",
              "ﾊ", "ﾋ", "ﾌ", "ﾍ", "ﾎ",
              "ﾏ", "ﾐ", "ﾑ", "ﾒ", "ﾓ",
              "ﾔ", "ﾕ", "ﾖ",
              "ﾗ", "ﾘ", "ﾙ", "ﾚ", "ﾛ",
              "ﾜ", "ｦ", "ﾝ",
              "ｧ", "ｨ", "ｩ", "ｪ", "ｫ",
              "ｯ", "ｬ", "ｭ", "ｮ", "ｳﾞ",
              "ｶﾞ", "ｷﾞ", "ｸﾞ", "ｹﾞ", "ｺﾞ",
              "ｻﾞ", "ｼﾞ", "ｽﾞ", "ｾﾞ", "ｿﾞ",
              "ﾀﾞ", "ﾁﾞ", "ﾂﾞ", "ﾃﾞ", "ﾄﾞ",
              "ﾊﾞ", "ﾋﾞ", "ﾌﾞ", "ﾍﾞ", "ﾎﾞ",
              "ﾊﾟ", "ﾋﾟ", "ﾌﾟ", "ﾍﾟ", "ﾎﾟ",
              "｡", "､", "･", "ﾞ", "ﾟ", "｢", "｣", "ｰ")

    def __init__(self):
        self.zh_ascii = dict(zip(self.z_ascii, self.h_ascii))
        self.hz_ascii = dict(zip(self.h_ascii, self.z_ascii))

        self.zh_digit = dict(zip(self.z_digit, self.h_digit))
        self.hz_digit = dict(zip(self.h_digit, self.z_digit))

        self.zh_kana = dict(zip(self.z_kana, self.h_kana))
        self.hz_kana = dict(zip(self.h_kana, self.z_kana))

    def zen2han(self, text, mode, ignore):
        if isinstance(text, text_type) or text == '':
            pass
        else:
            raise TypeError('You must set unicode string')

        if self._is_valid_mode(mode):
            zh_dict = self._make_zen2han_dict(mode)
        else:
            raise ValueError('Invalid mode value')

        converted = []
        for c in text:
            if c in ignore:
                converted.append(c)
            else:
                converted.append(zh_dict.get(c, c))

        return ''.join(converted)

    def han2zen(self, text, mode, ignore):
        if isinstance(text, text_type) or text == '':
            pass
        else:
            raise TypeError('You must set unicode string')

        if self._is_valid_mode(mode):
            hz_dict = self._make_han2zen_dict(mode)
        else:
            raise ValueError('Invalid mode value')

        converted = ['']
        prev = ''
        for c in text:
            if c in ignore:
                converted.append(c)
            elif c in ("ﾞ", "ﾟ"):
                p = converted.pop()
                converted.extend(hz_dict.get(prev+c, [p, hz_dict.get(c, c)]))
            else:
                converted.append(hz_dict.get(c, c))
            prev = c

        return ''.join(converted)

    def _is_valid_mode(self, mode):
        if isinstance(mode, int) and 0 <= mode <= 7:
            return True
        else:
            return False

    def _make_zen2han_dict(self, mode):
        d = {}

        if mode >= 4:
            d.update(self.zh_kana)
            mode = mode - 4

        if mode >= 2:
            d.update(self.zh_digit)
            mode = mode - 2

        if mode:
            d.update(self.zh_ascii)

        return d

    def _make_han2zen_dict(self, mode):
        d = {}

        if mode >= 4:
            d.update(self.hz_kana)
            mode = mode - 4

        if mode >= 2:
            d.update(self.hz_digit)
            mode = mode - 2

        if mode:
            d.update(self.hz_ascii)

        return d
