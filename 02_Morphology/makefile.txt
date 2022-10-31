all:
	hfst-lexc chv.lexc.txt -o chv.lexc.hfst
	hfst-twolc chv.twol.txt -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst