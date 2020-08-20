VERSION=`< VERSION`
author=$(Ge Yang)
author_email=$(ge.ike.yange@gmail.com)
# notes on python packaging: http://python-packaging.readthedocs.io/en/latest/minimal.html
default: ;
wheel:
	rm -rf dist
	python setup.py bdist_wheel
dev:
	make wheel
	pip install --ignore-installed dist/functional_notations*.whl
release:
	git tag v$(VERSION) -m '$(msg)'
	git push origin --tags
publish:
	make test
	make wheel
	twine upload dist/*
test:
	pytest
