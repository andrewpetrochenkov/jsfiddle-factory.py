#!/usr/bin/env python
"""create README.md files for every jsfiddle folder"""
# -*- coding: utf-8 -*-
import click
import jsfiddle_factory
import os

MODULE_NAME = "jsfiddle_factory.readme"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path ...' % MODULE_NAME


@click.command()
@click.argument('paths', nargs=-1, required=True)
def _cli(paths):
    for path in map(os.path.abspath, paths):
        os.chdir(path)
        jsfiddle_factory.Factory(path).create_readme()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
