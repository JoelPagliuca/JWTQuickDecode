#!/usr/bin/env python
import argparse, json, sys, pprint
from base64 import b64decode

__version__ = "1.0.0"
__all__ = ["decode_claims"]

def no_unicode(object, context, maxlevels, level):
	""" change unicode u'foo' to string 'foo' when pretty printing"""
	if pprint._type(object) is unicode:
		object = str(object)
	return pprint._safe_repr(object, context, maxlevels, level)

def decode_claims(claims):
	"""
	turn jwt claims string into a python claims dict
	
	:type claims: str
	:rtype: dict
	"""
	output = dict()
	i = 2
	while i: 
		try:
			decdoded = b64decode(claims, )
			output.update(json.loads(decdoded))
			i = 0
		except TypeError:
			claims = claims+"="
			i -= 1
	return output

def main(arguments=None):
	if arguments is None:
		arguments = sys.argv[1:]
	# set up a CLI
	parser = argparse.ArgumentParser(
		description="Quick JWT Claims Decoder - just pass in your jwt claims",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
	parser.add_argument('token', help='your jwt claims')
	args = parser.parse_args(arguments)
	# actualy do stuff
	claims = decode_claims(args.token)
	mypprint = pprint.PrettyPrinter()
	mypprint.format = no_unicode
	mypprint.pprint(claims)

if __name__ == '__main__':
	main()
