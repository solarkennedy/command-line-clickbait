all: clickbait.csv

lbgen.xml:
	wget -O lbgen.xml http://www.portent.com/wp-content/themes/pi_portent/title-maker/_db/lbgen.xml

devops.xml:
	wget -O devops.xml http://www.devopsweekly.com/archive.xml

devops.csv: devops.xml
	./extract-devopsy-articles.py > devops.csv

clickbait.csv: lbgen.xml devops.csv
	./devops-to-clickbait.py > clickbait.csv
