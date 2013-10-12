===============
Getting Started
===============

Create a new list
-----------------
Lists represent a customers database. Customers should only have one database but support is there to have multiple databases per customer. A list is necessary to perform any other operation on this service.

.. raw:: html

   <ul class="nav nav-tabs http-control-tab">
     <li class="active"><a href="#http" data-toggle="tab">HTTP POST Example</a></li>
	 <li><a href="#cURL" data-toggle="tab">cURL POST Example</a></li>
   </ul>

   <div class="tab-content">
	  <div class="tab-pane active" id="http">
	  <p><strong>Example request:</strong></p>

	  <div class="highlight-http">
	  <div class="highlight">
	  <pre>
	  <span class="nf">POST</span> <span class="nn">/lists</span> <span class="kr">HTTP</span><span class="o">/</span><span class="m">1.1</span>
	  <span class="na">Host</span><span class="o">:</span> <span class="l">example.com</span>
	  <span class="na">Accept</span><span class="o">:</span> <span class="l">application/json</span>
	  <span class="na">{"name"</span><span class="o">:</span> <span class="l">"new-list"}</span>
	  </pre>
	  </div>
	  </div>

	  <p><strong>Example response:</strong></p>

	  <div class="highlight-http"><div class="highlight">
	  <pre>
	  <span class="kr">HTTP</span><span class="o">/</span><span class="m">1.1</span> <span class="m">201</span> <span class="ne">CREATED</span>
	  <span class="na">Content-Type</span><span class="o">:</span> <span class="l">application/json</span>

	  <span class="p">{</span>
	  <span class="nt">"list_id"</span><span class="p">:</span> <span class="s2">"RTVhBsVG8prtKRzVgTS4fD"</span>
	  <span class="p">}</span>
	  </pre></div>
	  </div>
	  </div>

	  <div class="tab-pane" id="cURL">
	  <p><strong>Example request:</strong></p>

	  <p><code>curl "/lists" -u 1:1 -d '{"name": "new-name"}' -H "Content-Type: application/json"</code></p>

	  <p><strong>Example response:</strong></p>

	  <div class="highlight-http">
	  <pre>
	  {
	    "list_id": "2OeZXxTP82KJNJyGAyyddC"
	  }
	  </pre>
	  </div>
	  </div>
   </div>
