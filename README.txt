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

The apache bench command is this::

$ ab -n1001 -c4 http://localhost:8080/

To see the profiler output, go here::

http://localhost:8080/__profile__

At the time of writing Morepath gets about 100 lines of profiler
output. A significant fraction of this appears to be Werkzeug related,
or language built-in stuff. The Reg also adds to the output. This
means Morepath is around Flask in the "rankings", more than Pyramid or
Django, less than Zope 2, Grok.

I don't think this is too bad without trying, especially given
Morepath's factoring in small generic functions, with a model-driven
behavior baked in. Perhaps it is worthwhile to write some of Reg's
code in C code (optionally) so Reg can be hidden from the
debugger. Another thing to explore is Werkzeug.
