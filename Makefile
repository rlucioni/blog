build: css
	pelican blog/content --settings blog/settings.py

clean:
	rm -rf .sass-cache blog/output blog/theme/static/css/main.css

css:
	sass blog/theme/static/sass/main.scss blog/theme/static/css/main.css --style compressed --sourcemap=none

requirements:
	pip install -r requirements.txt
	gem install sass -v 3.5.1

serve: build
	cd blog/output && python -m pelican.server
