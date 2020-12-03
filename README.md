<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/jsfiddle-factory.svg?maxAge=3600)](https://pypi.org/project/jsfiddle-factory/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/jsfiddle-factory.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/jsfiddle-factory.py/actions)

### Installation
```bash
$ [sudo] pip install jsfiddle-factory
```

#### How it works
+   detox folder names - replace spaces, etc
+   init `demo.css`, `demo.js`, `demo.html`, `demo.details` in every empty dir
+   update `demo.details` `resources` from `resources.txt` (if exists)
+   create `build.html` for every jsfiddle dir
+   create `README.md` for every jsfiddle dir

#### Examples
```bash
$ python -m jsfiddle_factory .
```

#### Related
+   [`jsfiddle-build.py` - build `build.html` from jsfiddle files](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-factory.py` - jsfiddles mass production](https://pypi.org/project/jsfiddle-build/)
+   [`jsfiddle-generator.py` - jsfiddle files generator](https://pypi.org/project/jsfiddle-generator/)
+   [`jsfiddle-github.py` - jsfiddle github integration helper](https://pypi.org/project/jsfiddle-github/)
+   [`jsfiddle-readme-generator.py` - generate jsfiddle `README.md`](https://pypi.org/project/jsfiddle-readme-generator/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
