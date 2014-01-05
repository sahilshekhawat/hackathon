Hackathon
=========

Hackathon project of Sahil Shekhawat and Karan Grover.

Installing
==========

Download and unpack most recent Google App Engine SDK for python from
http://code.google.com/appengine/downloads.html, e.g.::

    $ wget http://googleappengine.googlecode.com/files/google_appengine_1.6.1.zip
    $ unzip google_appengine_1.6.1.zip

Then clone hackathon repository::

    $ git clone git://github.com/sahilshekhawat/hackathon.git


Development Server
==================

Now you are ready to run development web server::

    $ python google_appengine/dev_appserver.py hackathon/

This is the local server that runs on port 8080 (use ``--port`` option to 
change this). Open a web browser and go to http://localhost:8080.


Further Development
===================

Instead of using Google maps API, it will be better to use leaflet.js library.
Integrating it in Django environment would be a nice add-on.
User specific views and templates is what we lack which really needs to be
done.


