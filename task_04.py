#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
EMAIL = 'Hi {person}! I have {0} news! I won the raffle with number {1}{2}!'.format(NTYPE, 00, RNUM, person='Pat')
print EMAIL
