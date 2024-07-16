<h1>0x03. User authentication service</h1>

Back-end Authentification<br>

<p>In the industry, you should <strong>not</strong> implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="/rltoken/9nVfotMI_1zpEzihMzBeTA" title="Flask-User" target="_blank">Flask-User</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch:</strong></p>

<ul>
<li><a href="/rltoken/lKExyvivrrW4eh0eI8UV6A" title="Flask documentation" target="_blank">Flask documentation</a></li>
<li><a href="/rltoken/py7LuuD1u2MUwcaf8wnDzQ" title="Requests module" target="_blank">Requests module</a></li>
<li><a href="/rltoken/cj-mc5ZHp_KyXn1yikHC0A" title="HTTP status codes" target="_blank">HTTP status codes</a></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/oAqmZmipBdjCcfI5QqyFXA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<ul>
<li>How to declare API routes in a Flask app</li>
<li>How to get and set cookies</li>
<li>How to retrieve request form data</li>
<li>How to return various HTTP status codes</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>You should use <code>SQLAlchemy</code> 1.3.x</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>All your functions should be type annotated</li>
<li>The flask app should only interact with <code>Auth</code> and never with <code>DB</code> directly.</li>
<li>Only public methods of <code>Auth</code> and <code>DB</code> should be used outside these classes</li>
</ul>

<h2>Setup</h2>

<p>You will need to install <code>bcrypt</code></p>

<pre><code>pip3 install bcrypt
</code></pre>

<!-- Task Body -->
    <p>In this task you will create a SQLAlchemy model named <code>User</code> for a database table named <code>users</code> (by using the <a href="/rltoken/-a69l-rGqoFdXnnu6qfKdA" title="mapping declaration" target="_blank">mapping declaration</a> of SQLAlchemy). </p>

<p>The model will have the following attributes:</p>

<ul>
<li><code>id</code>, the integer primary key</li>
<li><code>email</code>, a non-nullable string</li>
<li><code>hashed_password</code>, a non-nullable string</li>
<li><code>session_id</code>, a nullable string</li>
<li><code>reset_token</code>, a nullable string</li>
</ul>

<pre><code>bob@dylan:~$ cat main.py
#!/usr/bin/env python3
&quot;&quot;&quot;
Main file
&quot;&quot;&quot;
from user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print(&quot;{}: {}&quot;.format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
</code></pre>