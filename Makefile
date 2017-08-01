.DEFAULT_GOAL := build
.PHONY: requirements

SETTINGS=blog/settings.py
CONTENT=blog/content
OUTPUT=blog/output
SCSS=blog/theme/static/sass/main.scss
CSS=blog/theme/static/css/main.css

build: css ## Build the site
	pelican $(CONTENT) --settings $(SETTINGS)

clean: ## Remove generated files and directories
	rm -rf .sass-cache $(OUTPUT) $(CSS)

css: ## Convert SCSS files to CSS
	sass $(SCSS) $(CSS) --style compressed --sourcemap=none

# Generates a help message. Borrowed from https://github.com/pydanny/cookiecutter-djangopackage.
help: ## Display this help message
	@echo "Please run \`make <target>\` where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

requirements: ## Install requirements
	pip install -r requirements.txt
	gem install sass -v 3.5.1

serve: ## Serve the site
	cd $(OUTPUT) && python -m pelican.server
