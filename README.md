# Mirror of Fred's ImageMagick Scripts

Source: http://www.fmwconcepts.com/imagemagick/index.php

## Licence

Check http://www.fmwconcepts.com/imagemagick/index.php for usage of these scripts.

## About

I wish the website had some .zip download that contained all the scripts so that this could all be avoided, but I digress.

Web-Scrapped with `get_imagemagick_scripts.py`.

Packages used:
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen
import cgi

Run with 

This is not unlike another mirror that exists: https://github.com/guzuomuse/fmwconcepts-imagemagicktools

I made this to get an updated version of the scripts, as well as use an alternative method (web scrapping). The other repo mentioned relies on `http://www.fmwconcepts.com/imagemagick/script_list.txt` being updated and accurate, which I believe currently is. I made this as an exercise.

## Edits made

`bin/3Drotate_animate`: change the hardcoded `infile` and `outfile` to parameters specified by user.