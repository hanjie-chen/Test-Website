import os

# get test data dir from env, default is '/articles-data'
Articles_Directory = os.environ.get("ARTICLES_DIRECTORY", "/articles-data")
# Rendered articles html directory, for develop env is /app/rendered-articles, for prod env is /rendered-articles
Rendered_Articles = os.environ.get("RENDERED_DIRECTORY", "/rendered-articles")
