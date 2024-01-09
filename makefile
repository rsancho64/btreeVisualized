# https://stackoverflow.com/questions/24736146/how-to-use-virtualenv-in-makefile

venv:
#	source alias.sh   ## source: not found (todo el makefile tiene su shell propio)
	python3 -m venv .venv

# activate: via alias activate='source .venv/bin/activate'
# install: via alias install='pip install -r requirements.txt'

# deactivate: direct


clean:
	rm -f bt_* 
	rm -f *.svg
	rm -Rf .venv/
