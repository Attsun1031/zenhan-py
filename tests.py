# -*- coding: utf-8 *-

import sys
import unittest

import zenhan

class TestZenhan(unittest.TestCase):
    def setUp(self):
        if sys.version_info < (3, 0):
            self.original = u"ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"
        else:
            self.original = "ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ"

    def test_h2z_ascii_only(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟａｂｃＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟａｂｃＤＥﾞＦ123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_h2z_digit_only(self):
        converted = zenhan.h2z(self.original, zenhan.DIGIT)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_h2z_kana_only(self):
        converted = zenhan.h2z(self.original, zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"゜abcＤＥ゛Ｆ123４５６アガサダナバビプペ゜")
        else:
            self.assertEqual(converted, "゜abcＤＥ゛Ｆ123４５６アガサダナバビプペ゜")

    def test_h2z_ascii_and_digit(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII|zenhan.DIGIT)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟａｂｃＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟａｂｃＤＥﾞＦ１２３４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_h2z_ascii_and_kana(self):
        converted = zenhan.h2z(self.original, zenhan.ASCII|zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"゜ａｂｃＤＥ゛Ｆ123４５６アガサダナバビプペ゜")
        else:
            self.assertEqual(converted, "゜ａｂｃＤＥ゛Ｆ123４５６アガサダナバビプペ゜")

    def test_h2z_digit_and_kana(self):
        converted = zenhan.h2z(self.original, zenhan.DIGIT|zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"゜abcＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜")
        else:
            self.assertEqual(converted, "゜abcＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜")

    def test_h2z_all(self):
        converted = zenhan.h2z(self.original, zenhan.ALL)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"゜ａｂｃＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜")
        else:
            self.assertEqual(converted, "゜ａｂｃＤＥ゛Ｆ１２３４５６アガサダナバビプペ゜")

        self.assertEqual(zenhan.h2z(self.original, zenhan.ALL),
                         zenhan.h2z(self.original,
                                    zenhan.ASCII|zenhan.DIGIT|zenhan.KANA))


    def test_z2h_ascii_only(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcDEﾞF123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcDEﾞF123４５６ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_z2h_digit_only(self):
        converted = zenhan.z2h(self.original, zenhan.DIGIT)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcＤＥﾞＦ123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcＤＥﾞＦ123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_z2h_kana_only(self):
        converted = zenhan.z2h(self.original, zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcＤＥﾞＦ123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")

    def test_z2h_ascii_and_digit(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII|zenhan.DIGIT)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcDEﾞF123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcDEﾞF123456ｱｶﾞｻダナバビﾌﾟﾍﾟﾟ")

    def test_z2h_ascii_and_kana(self):
        converted = zenhan.z2h(self.original, zenhan.ASCII|zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcDEﾞF123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcDEﾞF123４５６ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")

    def test_z2h_digit_and_kana(self):
        converted = zenhan.z2h(self.original, zenhan.DIGIT|zenhan.KANA)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcＤＥﾞＦ123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcＤＥﾞＦ123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")

    def test_z2h_all(self):
        converted = zenhan.z2h(self.original, zenhan.ALL)

        if sys.version_info < (3, 0):
            self.assertEqual(converted, u"ﾟabcDEﾞF123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")
        else:
            self.assertEqual(converted, "ﾟabcDEﾞF123456ｱｶﾞｻﾀﾞﾅﾊﾞﾋﾞﾌﾟﾍﾟﾟ")

        self.assertEqual(converted,
                         zenhan.z2h(self.original,
                                    zenhan.ASCII|zenhan.DIGIT|zenhan.KANA))

if __name__ == '__main__':
    unittest.main()
