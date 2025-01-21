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
    my-articles-extensions = ['fenced_code', 'footnotes', 'tables', 'md_in_html']
    # Configure markdown converter with extensions
    md = markdown.Markdown(extensions=[
        'fenced_code',
        'tables',
        'toc'
    ])
    
    # Convert markdown to HTML
    html_content = md.convert(markdown_content)
    
    # Only include necessary styles for markdown-specific elements
    html_template = f"""
    <style>
        /* Code blocks */
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }}
        
        /* Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        
        /* Images */
        img {{
            max-width: 100%;
            height: auto;
        }}
        
        /* Table of Contents */
        .toc {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .toc ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
    </style>
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
