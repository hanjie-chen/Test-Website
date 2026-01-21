import os

# get test data dir from env, default is '/articles-data'
Articles_Directory = os.environ.get("SOURCE_ARTICLES_DIRECTORY", "/articles/src")
# Rendered articles html directory, for develop env is /app/rendered-articles, for prod env is /rendered-articles
Rendered_Articles = os.environ.get("RENDERED_ARTICLES_DIRECTORY", "/articles/rendered")
