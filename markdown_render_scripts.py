import markdown2
import os
from typing import Tuple

class MarkdownRenderer:
    def __init__(self, articles_dir: str, html_output_dir: str):
        self.articles_dir = articles_dir
        self.html_output_dir = html_output_dir
        
        # 确保输出目录存在
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
    
    def render_markdown(self, content: str) -> str:
        """将Markdown内容转换为HTML"""
        return markdown2.markdown(content, extras=['fenced-code-blocks', 
                                                 'tables',
                                                 'code-friendly'])
    
    def process_article(self, md_filename: str) -> Tuple[str, str]:
        """处理单个文章，返回(html_content, html_filename)"""
        md_path = os.path.join(self.articles_dir, md_filename)
        html_filename = os.path.splitext(md_filename)[0] + '.html'
        html_path = os.path.join(self.html_output_dir, html_filename)
        
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分割元数据和正文
        split = content.split('<!-- split -->', 1)
        if len(split) != 2:
            return None, html_filename
        
        body_part = split[1]
        html_content = self.render_markdown(body_part)
        
        # 包装HTML内容
        full_html = self.wrap_html_content(html_content)
        
        # 保存HTML文件
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        return html_content, html_filename
    
    def wrap_html_content(self, content: str) -> str:
        """将HTML内容包装在完整的HTML文档中"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="/static/css/article.css">
        </head>
        <body>
            <article class="markdown-body">
                {content}
            </article>
        </body>
        </html>
        """
