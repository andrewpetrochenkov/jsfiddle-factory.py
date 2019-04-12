#!/usr/bin/env python
"""detox, init, update resources, create `build.html` and `README.md`"""
# -*- coding: utf-8 -*-
import click
import jsfiddle_factory
import os

MODULE_NAME = "jsfiddle_factory"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    for path in map(os.path.abspath, paths):
        os.chdir(path)
        factory = jsfiddle_factory.Factory(path)
        factory.detox()
        factory.init()
        factory.update_resources()
        factory.build_html()
        factory.create_readme()

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
