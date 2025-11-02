PY = python

all:
	@$(PY) rp.py $(word 2,$(MAKECMDGOALS))

clean:
	rm  -f ./*.c

%:
	@: