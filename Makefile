all:
	rm *.tar.gz
	tar czvf airflow-mpack-$(shell git describe --tags).tar.gz airflow-mpack
