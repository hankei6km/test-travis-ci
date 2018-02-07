# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 hankei6km
# Licensed under the MIT License. See LICENSE.txt in the project root.


class FlyingTent:

    _emoji_tent = '⛺'
    _emoji_flying = '💨'

    def __init__(self):
        self._flying = False
        self._fmt = '{tent} {flying}'

    def do_fly(self, fly):
        ret = self._flying
        self._flying = fly
        return ret

    def render(self):
        return \
            self._fmt.format(
                tent=self._emoji_tent,
                flying=self._emoji_flying if self._flying else '')


if __name__ == '__main__':  # pragma: no cover.
    f = FlyingTent()
    print(f.render())
    f.do_fly(True)
    print(f.render())
