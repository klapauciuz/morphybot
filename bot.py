# -*- coding: utf-8 -*-

import pymorphy2
import string
import telepot
from telepot.loop import MessageLoop
import time
from collections import Counter

from alphabet_detector import AlphabetDetector
ad = AlphabetDetector()

morph = pymorphy2.MorphAnalyzer()


def handle(msg):
	chat_id = msg['chat']['id']
	sentence = msg['text']

	# определяем русский язык
	if not ad.is_cyrillic(sentence):
		bot.sendMessage(chat_id, 'Please enter Russian sentence')
	else:
		d = []

		# удаляем ненужные символы и создаем массив из слов
		sentence = [word.strip(string.punctuation) for word in sentence.split()]

		# создаем словарь
		for w in sentence:
			d.append((w, morph.parse(w)[0].tag.POS))
		counts = Counter(tag for word,tag in d)
		# print counts

		# считаем количество глаголов, существительных и прилагательных и формируем ответ
		resp = '%s verbs, %s nouns, %s adjectives' % (counts['VERB'], counts['NOUN'], counts['ADJF'] + counts['ADJS'])

		bot.sendMessage(chat_id, resp)


bot = telepot.Bot('443024916:AAHXoCRAQHDWslM10k0x-yrF4wx-Ca-amxc')
print bot.getMe()

MessageLoop(bot, handle).run_as_thread()
while 1:
	time.sleep(10)