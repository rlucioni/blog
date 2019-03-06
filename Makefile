clean:
	rm -rf public

compile:
	npm run compile

build: clean compile
	hugo --minify --gc

serve: compile
	hugo server --buildDrafts --disableFastRender

post-%:
	hugo new posts/$*.md
