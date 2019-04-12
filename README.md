<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/jsfiddle-factory.svg?longCache=True)](https://pypi.org/project/jsfiddle-factory/)
[![](https://img.shields.io/pypi/v/jsfiddle-factory.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-factory/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/jsfiddle-factory.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/jsfiddle-factory.py/)

#### Installation
```bash
$ [sudo] pip install jsfiddle-factory
```

#### How it works
+   detox folder names - replace spaces, etc
+   init `demo.css`, `demo.js`, `demo.html`, `demo.details` in every empty dir
+   update `demo.details` `resources` from `resources.txt` (if exists)
+   create `build.html` for every jsfiddle dir
+   create `README.md` for every jsfiddle dir

#### Classes
class|`__doc__`
-|-
`jsfiddle_factory.Factory` |attrs: `path`. methods: `detox()`, `init()`, `build()`, `readme()`, `update_resources()`

#### Executable modules
usage|`__doc__`
-|-
`python -m jsfiddle_factory path ...` |detox, init, update resources, create `build.html` and `README.md`
`python -m jsfiddle_factory.readme path ...` |create build.html for every jsfiddle folder
`python -m jsfiddle_factory.detox path ...` |clean up folder names
`python -m jsfiddle_factory.init path ...` |init `demo.css`, `demo.js`,`demo.html`,`demo.details` in every empty dir
`python -m jsfiddle_factory.readme path ...` |create README.md files for every jsfiddle folder

#### Examples
```bash
$ python -m jsfiddle_factory .
```

#### Related projects
+   [`jsfiddle-build.py` - build `build.html` file from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>