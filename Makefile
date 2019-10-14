all: clean
	tar czvf airflow-mpack-$(shell git describe --tags).tar.gz airflow-mpack
clean:
	rm -f *.tar.gz
