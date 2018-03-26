all:
	python3 script/make.py layouts/qwerty/*.yaml layouts/dvorak/*.yaml layouts/qwerty42/*.yaml

dvorak:
	python3 script/make.py layouts/dvorak/*.yaml

qwerty:
	python3 script/make.py layouts/qwerty/*.yaml

qwerty42:
	python3 script/make.py layouts/qwerty42/*.yaml

clean:
	rm -f dist/*

lint:
	flake8 script

