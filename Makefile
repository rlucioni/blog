clean:
	rm -rf public
	rm -rf resources

build: clean
	hugo

serve:
	hugo server -D
