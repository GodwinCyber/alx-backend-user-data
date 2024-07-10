<h1>0x02. Session authentication</h1>

Back-end Authentification<br>

<h2>Background Context</h2>

<p>In this project, you will implement a <strong>Session Authentication</strong>. You are not allowed to install any other module.</p>

<p>In the industry, you should <strong>not</strong> implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: <a href="/rltoken/_ZTQTaMKjx1S_xATshexkA" title="Flask-HTTPAuth" target="_blank">Flask-HTTPAuth</a>). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/oofk0VhuS0ZFZTNTVrQeaQ" title="REST API Authentication Mechanisms - Only the session auth part" target="_blank">REST API Authentication Mechanisms - Only the session auth part</a> </li>
<li><a href="/rltoken/peLV8xuJ4PDJMOVFqk-d2g" title="HTTP Cookie" target="_blank">HTTP Cookie</a> </li>
<li><a href="/rltoken/AI1tFR5XriGfR8Tz7YTYQA" title="Flask" target="_blank">Flask</a> </li>
<li><a href="/rltoken/QYfI5oW6OHUmHDzwKV1Qsw" title="Flask Cookie" target="_blank">Flask Cookie</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/uWXp4VcY3Dd9UzTtc9N5_A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What session authentication means</li>
<li>What Cookies are</li>
<li>How to send Cookies</li>
<li>How to parse Cookies </li>
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
