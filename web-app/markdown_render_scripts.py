import markdown
import os

def render_markdown_to_html(markdown_content: str, filename: str, destination_folder: str):
    """generate html file to destination folder
    
    Args:
        markdown_content: The markdown string need to convert
        filename: The name for the output html file
        destination_folder: The folder path to save the rendered HTML
    """
    # use entry point to specified the extension I need
    my_articles_extensions = ['fenced_code', 'footnotes', 'tables', 'md_in_html', 'sane_lists', 'codehilite']

    # Configure markdown converter with extensions
    md = markdown.Markdown(extensions=my_articles_extensions)
    
    # Convert markdown to HTML
    html_content = md.convert(markdown_content)
    
    # Only include necessary styles for markdown-specific elements
    html_template = f"""
    {html_content}
    """
    
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Write the HTML file
    output_path = os.path.join(destination_folder, f"{filename}.html")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
        print(f"Successfully rendered HTML to {output_path}")
    except Exception as e:
        print(f"Error writing HTML file: {e}")
