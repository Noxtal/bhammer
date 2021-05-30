#!/usr/bin/env python

from art import *

def main():
	art = None

	artfn = input("ASCII art to include (text format, - to skip) ")
	if not artfn.startswith("-"):
		try:
			with open(artfn) as f:
				art = f.read()
		except FileNotFoundError:
			print("File not found... Skipping!")

	title = input("Title: ")
	font = input("Font (ls for font names *LARGE OUTPUT WARNING*) ")
	if font.startswith("ls"):
		for name in FONT_NAMES:
			if name:
				print(name)
				tprint(title,font=name,chr_ignore=True)
		font = input("Font: ")

	description = input("Description: ")

	fields = []
	while True:
		if input("Add another field? (y/n) ").lower().startswith("n"): 
			break

		n = input("Field name: ")
		v = input("Field value: ")
		fields.append(f"{n}: {v}")

	extra = input("Extra content (leave empty if needed, use *f followed by a space and your filename to use a file) ")
	if extra.startswith("*f "):
		try:
			with open(extra[3:]) as f:
				extra = f.read()
		except FileNotFoundError:
			print("File not found... Skipping!")

	print("YOUR ASCII BANNER \n\n\n(Copy from here!)")

	if art: print(art)

	tprint(title,font=font,chr_ignore=True)

	print(description)

	for line in fields:
		print(line)

	print(extra)

if __name__ == '__main__':
	exit(main() or 0)