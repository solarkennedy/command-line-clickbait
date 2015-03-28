print: lbgen.xml
	@./command-line-clickbait.py

lbgen.xml:
	wget -O lbgen.xml http://www.portent.com/wp-content/themes/pi_portent/title-maker/_db/lbgen.xml

devops-weekly-generator/devops.csv:
	make -C devops-weekly-generator
