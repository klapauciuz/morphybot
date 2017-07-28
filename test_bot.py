# -*- coding: utf-8 -*-

from morphybot import morphy
import pytest

def test_morphy():
	assert morphy(u'Удивительно, почему паразиты используют столь сложные стратегии, в то время когда, казалось бы, природа вообще предпочитает простые решения. Однако же эти манипуляции, хотя и запутанные, наверняка не следуют из какого-то сознательного расчета.') == '3 verbs, 7 nouns, 6 adjectives'

def test_foreign():
	assert morphy(u'Fixtures requiring network access depend on connectivity and are usually time-expensive to create.') == 'Please enter Russian sentence'