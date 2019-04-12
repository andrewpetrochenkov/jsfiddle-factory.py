#!/usr/bin/env python
import jsfiddle_build
import jsfiddle_github
import jsfiddle_generator
import jsfiddle_readme_generator
import getdirs
import getfiles
import os
import popd
import public
import yaml


@popd.popd
def _build(path):
    os.chdir(path)
    jsfiddle_build.Build().save("build.html")


@popd.popd
def _init(path):
    os.chdir(path)
    isempty = len(os.listdir(path)) == 0
    isfiddle = len(list(filter(os.path.exists, ["demo.css", "demo.js", "demo.html"]))) > 0
    if isempty or isfiddle:
        jsfiddle_generator.JSFiddleRepo().create()


@popd.popd
def _readme(path):
    os.chdir(path)
    jsfiddle_readme_generator.Readme().save("README.md")


@public.add
class Factory:
    """attrs: `path`. methods: `detox()`, `init()`, `build()`, `readme()`, `update_resources()`"""
    path = None

    def __init__(self, path=None):
        if not path:
            path = os.getcwd()
        self.path = path

    def build_html(self):
        files = getfiles.getfiles(self.path)
        matches = ["demo.html", "fiddle.html"]
        for f in filter(lambda f: os.path.basename(f) in matches, files):
            _build(os.path.dirname(f))

    def create_readme(self):
        files = getfiles.getfiles(self.path)
        matches = ["demo.html", "fiddle.html"]
        for f in filter(lambda f: os.path.basename(f) in matches, files):
            _readme(os.path.dirname(f))

    def init(self):
        for path in getdirs.getdirs(self.path):
            _init(path)

    def detox(self):
        renamed = True
        while renamed:
            renamed = False
            for path in getdirs.getdirs(self.path):
                relpath = os.path.relpath(path, os.getcwd())
                new_relpath = jsfiddle_github.sanitize(relpath)
                new_path = os.path.join(os.getcwd(), new_relpath)
                ishidden = relpath[0] == "." and "%s." % os.sep not in relpath
                if not ishidden and new_relpath != relpath:
                    os.rename(path, new_path)
                    print("%s -> %s" % (path, new_path))
                    renamed = True

    def update_resources(self):
        f = os.path.join(self.path, "resources.txt")
        if not os.path.exists(f):
            print("SKIP: %s NOT EXISTS" % f)
        resources = list(filter(None, open(f).read().splitlines()))
        files = getfiles.getfiles(self.path)
        matches = ["demo.details", "fiddle.manifest"]
        for f in filter(lambda f: os.path.basename(f) in matches, files):
            if os.path.exists(f):
                data = yaml.load(open(f, 'r'))
                if data.get("resources", []) != resources:
                    data["resources"] = resources
                    yaml.dump(data, open(f, 'w'), default_flow_style=False)
