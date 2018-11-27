# local-ci.py

This is a wrapper script for running local Gitlab CI pipelines before pushing to the repository server.

After reading *AkitaOnRails*'s post about [running Gitlab CI Runner locally](http://www.akitaonrails.com/2018/04/28/smalltips-running-gitlab-ci-runner-locally), 
I got inspired to run my CI jobs locally.
The problem is that Gitlab CI Runner can only execute one job per run, necessitating the need for a loop of some kind.

`local-ci.py` takes CI stage names as arguments and runs all CI steps that belong to that stage.

Example:

    $ local-ci.py test
    $ local-ci.py build test deploy

It requires that Gitlab CI Runner, Docker and Python 3.5 are installed locally, but should be trivial to modify if these requirements are a problem to you.

First draft of this tool, so no edge case or other workloads are supported.
