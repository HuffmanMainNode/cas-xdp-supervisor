.PHONY: test verify

test:
	python3 -m unittest discover -v

verify:
	python3 supervisor.py verify-baseline
	python3 -m unittest discover -v
