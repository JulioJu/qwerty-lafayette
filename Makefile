all:
	kalamine layouts/*.yaml
	@echo
	./xkb_patch.py lafayette

install:
	./dist/xkb/lafayette_install.sh
	@echo
	@echo "Successfully installed. Testable with one of the following:"
	@echo "    setxkbmap fr -variant lafayette"
	@echo "    setxkbmap fr -variant lafayette42"

clean:
	rm -rf dist/*
