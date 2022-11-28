clean:
	rm -rf */__pycache__
	rm -rf */migrations
	rm -f db.sqlite3

setup: clean
	python3 manage.py makemigrations core && \
	python3 manage.py migrate && \
	python3 manage.py createsuperuser && \
	python3 manage.py createserviceaccount --username testsa --password password --description "hello world" && \
	python3 manage.py createapiroute --apiname goldapi --routes goldapi/view/  && \
	python3 manage.py createuserapiroute --username testsa --api goldapi --route goldapi/view/ 