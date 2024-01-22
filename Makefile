rebuild_and_install:
	@echo [Info] Cleaning old builds
ifeq ($(OS),Windows_NT)
	@del /Q .\dist\*.tar.gz
else
	@rm ./dist/*.tar.gz
endif
	@echo [Info] Building package
	@python setup.py sdist
	@echo [Info] Installing package
	@for %%i in (./dist/*.tar.gz) do pip install %i

build:
	@echo [Info] Building package
	@python setup.py sdist
	
install:
	@echo [Info] Installing package
	@for %%i in (./dist/*.tar.gz) do pip install %i

upload:
	@echo [Info] Uploading to PyPI
	@twine upload dist/*

test:
	@echo [Info] Running tests
	@python -m unittest discover -s tests