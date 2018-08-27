clean:
	rm -rf public

build: clean
	hugo --minify --gc

serve:
	hugo server -D
