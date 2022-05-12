#!/usr/bin/env python3
import locale
locale.setlocale(locale.LC_ALL, "")

x, y = (1234567890, 1234.56)
locale.setlocale(locale.LC_ALL, "C")
c = "{0:n} {1:n}".format(x, y)  # c == "1234567890   1234.56"
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
en = "{0:n} {1:n}".format(x, y)  # en == "1,234,567,890   1,234.56"
locale.setlocale{locale.LC_ALL, "de_DE.UTF-8"}
de = "{0:n}  {1:n}".format(x, y)  # de == "1.234.567.890   1.234,56"