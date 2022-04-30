from flask import Flask

# print a nice greeting.
def say_hello(username = "teacher"):
    return '<p>Welcome %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <table>
        <tr>
            <th>Máxima provincia contagiada</th>
            <th>Cantidad contagiados</th>
            <th>Mínima provincia contagiada</th>
            <th>Cantidad mínima</th>
            <th>Media aritmética</th>
            <th>Desviación típica</th>
            <th>Varianza</th>
            <th>Moda provincia</th>
            <th>Moda cantidad</th>
          </tr>
          <tr>
            <td>MD</td>
            <td>493480</td>
            <td>CE</td>
            <td>3758</td>
            <td>350.02799838470855</td>
            <td>756.9521803489858</td>
            <td>572976.6033350836</td>
            <td>AN</td>
            <td>391</td>
          </tr>
    </table>
    \n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
