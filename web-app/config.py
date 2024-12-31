import os

# get test data dir from env, default is '/app/articles-data-test'
Articles_Directory = os.environ.get("ARTICLES_DIRECTORY", "/articles-data")
# Rendered articles directory (relative to project root)
Rendered_Articles = "rendered_articles"
