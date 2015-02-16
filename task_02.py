#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
print inquisition.SPANISH
FLEMISH = inquisition.SPANISH[:19] + 'FLEMISH' + inquisition.SPANISH[26:]
print FLEMISH
