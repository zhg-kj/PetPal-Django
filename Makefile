.PHONY: clean
clean:
	rm -rf db.sqlite3 */*/__pycache__ */__pycache__ \
	   */*/*/__pycache__ apps/*/migrations/0*.py *.pyc