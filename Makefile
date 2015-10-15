PY?=python
PELICAN?=pelican
PELICANOPTS=
SASS?=sass

DATE:=$(shell date +'%Y-%m-%d %H:%M')
# Pass the provided name to sed, use the g (global replacement) switch and an
# exclusion set to replace all non-alphanumeric characters with hyphens, squeeze
# repeated hyphens into a single hyphen, and lowercase all remaining characters
SLUG:=$(shell echo '${TITLE}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXTENSION?=md

IPREGEX=[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
INTERNALIP:=$(shell ifconfig en0 inet | grep -oE 'inet $(IPREGEX)' | grep -oE '$(IPREGEX)')

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
POSTDIR=$(BASEDIR)/content/posts
THEMEDIR=$(BASEDIR)/themes/custom

DEVCONFIG=$(BASEDIR)/configuration/dev.py
GITHUBCONFIG=$(BASEDIR)/configuration/github.py

SCSS=$(THEMEDIR)/static/sass/main.scss
CSS=$(THEMEDIR)/static/css/main.css

S3_BUCKET=my_s3_bucket

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo '                                                                                                   '
	@echo 'Makefile for a Pelican website                                                                     '
	@echo '                                                                                                   '
	@echo 'Usage:                                                                                             '
	@echo '    make post                        create new draft post                                         '
	@echo '    make html                        generate HTML                                                 '
	@echo '    make css                         generate CSS                                                  '
	@echo '    make clean                       remove generated output                                       '
	@echo '    make regenerate                  regenerate files upon modification                            '
	@echo '    make serve [PORT=8000]           serve site at http://localhost:8000                           '
	@echo '    make preview                     serve the site at 0.0.0.0:8000                                '
	@echo '    make fresh                       generate CSS and HTML, and serve site at http://localhost:8000'
	@echo '    make devserver [PORT=8000]       start/restart develop_server.sh                               '
	@echo '    make stopserver                  stop local server                                             '
	@echo '    make publish                     generate using production settings                            '
	@echo '    make s3_upload                   upload site via S3                                            '
	@echo '    make github                      upload site via gh-pages                                      '
	@echo '                                                                                                   '
	@echo 'Set the DEBUG variable to 1 to enable Pelican debugging (e.g., make DEBUG=1 html)                  '
	@echo '                                                                                                   '

post:
ifdef TITLE
	echo "Title: $(TITLE)"         >  $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Description: FILL ME IN" >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Slug: $(SLUG)"           >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Date: $(DATE)"           >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Modified: $(DATE)"       >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Author: Renzo Lucioni"   >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Tags: FILL ME IN"        >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo "Status: draft"           >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo ""                        >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	echo ""                        >> $(POSTDIR)/$(SLUG).$(EXTENSION)
	git add $(POSTDIR)/$(SLUG).$(EXTENSION)
else
	@echo '                                         '
	@echo 'Usage:                                   '
	@echo '    make post TITLE='"'"'Post Title'"'"
	@echo '                                         '
endif

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(DEVCONFIG) $(PELICANOPTS)

css:
	$(SASS) $(SCSS) $(CSS) --style compressed --sourcemap=none

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(DEVCONFIG) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

preview: css html
	@echo 'Access the site externally at $(INTERNALIP):8000.'
	pushd $(OUTPUTDIR); $(PY) -m SimpleHTTPServer; popd

fresh: css html serve

devserver:
ifdef PORT
	$(BASEDIR)/utilities/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/utilities/develop_server.sh restart
endif

stopserver:
	kill -9 `cat pelican.pid`
	kill -9 `cat srv.pid`
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish: css
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(GITHUBCONFIG) $(PELICANOPTS)

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type

github: publish
	ghp-import -m "Generate site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: help post html css clean regenerate serve preview fresh devserver stopserver publish s3_upload github
