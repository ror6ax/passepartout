#!/usr/bin/python
from PIL import Image, ImageOps, ImageDraw, ImageFont
from os import path
from sys import argv
import click


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('mode', type=click.Choice(['wide', 'high']))
@click.argument('tone', type=click.Choice(['light', 'dark']))
def main(filename, mode, tone):
	if path.isfile(filename):
		source_im = Image.open(filename)
		width, hight = source_im.size
		if mode == "wide":
			ratio = 5000/width
		if mode == "high":
			ratio = 5000/hight
		im = ImageOps.scale(source_im,ratio*0.8)
		wi, hi = im.size 
		wi2 = int((5000 - wi)/2)
		hi2 = int((5000 - hi)/2) 
		if tone == "light":
			im = ImageOps.expand(im, border = (wi2,hi2), fill="#E5E5E5")
		if tone == "dark":
			im = ImageOps.expand(im, border = (wi2,hi2), fill="#0e0e0e")
		im.save(f'exp_{filename}')
	else:
        	exit("No source file found!")

if __name__ == '__main__':
    main()
