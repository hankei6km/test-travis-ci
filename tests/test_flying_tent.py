# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.

from flying_tent.flying_tent import FlyingTent


class TestFlyingTent:

    def test_do_fly(self):
        f = FlyingTent()
        assert f.do_fly(True) is False
        assert f.do_fly(False) is True
        assert f.do_fly(False) is False
        assert f.do_fly(True) is False
        assert f.do_fly(True) is True

    def test_render(self):
        f = FlyingTent()
        assert f.render() == '⛺ '
        f.do_fly(True)
        assert f.render() == '⛺ 💨'
        f.do_fly(False)
        assert f.render() == '⛺ '
