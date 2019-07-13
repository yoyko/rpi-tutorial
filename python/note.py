#!/usr/bin/env python
import re

noteValue = {
	'c': 0,
	'd': 2,
	'e': 4,
	'f': 5,
	'g': 7,
	'a': 9,
	'b': 11,
	'h': 11,
}

def calculateFreqs():
	freqs = {}
	# a4 -> 440Hz, one octave -> *2, one seminote -> * (12th root of 2)
	a4 = 4*12 + noteValue['a']
	freqs[a4] = 440.0
	step = pow(2.0, 1.0/12)
	for i in xrange(a4 - 1, 0, -1):
		freqs[i] = freqs[i+1] / step
	for i in xrange(a4 + 1, 10*12):
		freqs[i] = freqs[i-1] * step
	return freqs

noteFreq = calculateFreqs()
noteAdj = { '#': 1, 's': 1, 'b': -1, 'f': -1 } # # or s for sharp,  b or f for flat
noteRegex = re.compile(r'^([A-Ha-hzZ])([#bsf]?)([-+]?\d*)/(\d+)(\.?)$')

def parse(s, tempo = 120, denominator = 4):
	"""Parse the textual note description of a note.
	Returns a pair (frequency, duration) where frequency == 0 means a pause.
	"""
	matches = noteRegex.match(s)
	if matches == None:
		raise Exception("Bad note: '%s'" % s)

	duration = 60.0 * denominator / tempo / int(matches.group(4))

	if matches.group(1).lower() == 'z':
		return (0, duration)

	value = noteValue[matches.group(1)]
	if matches.group(2) in noteAdj.keys():
		value += noteAdj[matches.group(2)]

	octave = 4
	if matches.group(3):
		if matches.group(3)[0] in '+-':
			octave += int(matches.group(3))
		else:
			octave = int(matches.group(3))

	value += octave * 12

	return (noteFreq[value], duration)
