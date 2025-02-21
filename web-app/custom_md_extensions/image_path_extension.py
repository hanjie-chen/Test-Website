# this extension used to change relative image path correct image path
# further consider: for relative like ./ all use this extensino to deal with

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

class Image_Path_Processor(Postprocessor):
    def __init__(self, md, base_url):
        super().__init__(md)
        self.base_url = base_url

    def run(self, text):
        """
        use beautifulSoup to parse html
        only change <img> tag src attribute which start with "./"
        """
        soup = BeautifulSoup(text, "html.parser")
        for img in soup.find_all("img"):
            src = img.get("src", "")
            if src.startswith("./"):
                img["src"] = urljoin(self.base_url, src[2:])
                print("base_url = ", self.base_url)
                print("Update image src to ",img["src"])

        return str(soup)
    

class Image_Path_Extension(Extension):
    @staticmethod
    def normalize_base_url(url: str) -> str:
        return '/' + url.strip('/') + '/'

    def __init__(self, base_url: str, **kwargs):
        """
        :param base_url: Base URL for images, e.g. 'rendered-articles/tools-guide-git-guide/'
        """
        # make sure the base url end with / and start with /
        base_url = Image_Path_Extension.normalize_base_url(base_url)
        self.config = {
            'base_url': [base_url, 'Base URL for images']
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        base_url = self.getConfig('base_url')
        md.postprocessors.register(
            Image_Path_Processor(md, base_url),
            "image_path_postprocessor",
            25
        )

def makeExtension(**kwargs):
    return Image_Path_Extension(**kwargs)