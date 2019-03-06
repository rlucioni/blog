clean:
	rm -rf public
	rm assets/js/main.min.js

compile:
	npm run compile

build: clean compile
	hugo --minify --gc

serve:
	hugo server --buildDrafts --disableFastRender

post-%:
	hugo new posts/$*.md
