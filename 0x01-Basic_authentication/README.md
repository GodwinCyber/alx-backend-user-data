<h1>0x01. Basic authentication</h1>

<h2>Background Context</h2>

<p>In this project, you will learn what the authentication process means and implement a <strong>Basic Authentication</strong> on a simple API.</p>

<p>In the industry, you should <strong>not</strong> implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="/rltoken/rpsPy0M3_FJuCLGNPUbmvg" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/ssg5umgsMk5jKM8WRHk2Ug" title="REST API Authentication Mechanisms" target="_blank">REST API Authentication Mechanisms</a> </li>
<li><a href="/rltoken/RpaPRyKx1rdHgRSUyuPfeg" title="Base64 in Python" target="_blank">Base64 in Python</a> </li>
<li><a href="/rltoken/WlARq8tQPUGQq5VphLKM4w" title="HTTP header Authorization" target="_blank">HTTP header Authorization</a> </li>
<li><a href="/rltoken/HG5WXgSja5kMa29fbMd9Aw" title="Flask" target="_blank">Flask</a> </li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/" title="abort - Custom Error Pages" target="_blank">abort - Custom Error Pages</a> </li>
<li><a href="/rltoken/br6Rp4iMaOce6EAC-JQnOw" title="Base64 - concept" target="_blank">Base64 - concept</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/swiIZazfz7mspY1vjuy_Zg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What Base64 is</li>
<li>How to encode a string in Base64</li>
<li>What Basic authentication means</li>
<li>How to send the Authorization header</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
