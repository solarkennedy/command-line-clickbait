all: devops.csv

devops.xml:
	wget -O devops.xml http://www.devopsweekly.com/archive.xml

devops.csv: devops.xml
	./extract-devopsy-articles.py > devops.csv

clean:
	rm *.csv
