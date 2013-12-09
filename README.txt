What is it doing
================

This directory contains a very simple "hello" Morepath app, wrapped
into a ``repoze.profile`` middleware. This is to compare Morepath
along these lines:

http://plope.com/whats_your_web_framework_doing

http://plope.com/whatsitdoing2

http://plope.com/pyroptimization

After running the buildout, starting the app goes like this::

$ bin/devpython app.py

Starting it without profiler for raw performance measurement is like
this::

$ NO_PROFILE=1 bin/devpython app.py

The server uses Waitress by default.

The apache bench command is this::

$ ab -n1001 -c4 http://localhost:8080/

To see the profiler output, go here::

http://localhost:8080/__profile__

At the time of writing Morepath gets about 100 lines of profiler
output. A significant fraction of this appears to be Werkzeug related,
or language built-in stuff. Reg also adds to the output. This means
Morepath is around Flask in the "rankings", more than Pyramid or
Django, less than Zope 2, Grok.

I don't think this is too bad without trying, especially given
Morepath's factoring in small generic functions, with a model-driven
behavior baked in. Perhaps it is worthwhile to write some of Reg's
code in C code (optionally) so Reg can be hidden from the
debugger. Another thing to explore might be Werkzeug, though that's
all pretty hidden from normal use.

It is also interesting to run the benchmark (without profiling) with gunicorn.
gunicorn is installed, and the command to start with gunicorn is this one::

$ bin/gunicorn -w 4 app:the_app

The ab command has to be adjusted to use port 8000::

$ ab -n1001 -c4 http://localhost:8000/

On my machine doing so I get 6500 requests per second, much more than
when using waitress, where I only get about 1000.
