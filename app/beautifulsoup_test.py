from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>My Web Page</title></head>
  <body>
    <h1>Welcome to My Web Page</h1>
    <p class="content">This is a paragraph.</p>
    <a href="http://example.com">Example Link</a>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())  # 구조화된 HTML 출력