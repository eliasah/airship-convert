# Airship Convert

A proof of concept converter for [Apache Zeppelin](https://zeppelin.incubator.apache.org/) notebooks.

## Installation

```
git clone https://github.com/zero323/airship-convert.git
cd airship-convert
pip install .
```

## Usage

### Static document generation

```bash
usage: airship-convert render [-h] [--output-dir OUTPUT_DIR] [--format FORMAT]
                              [--default-lang DEFAULT_LANG]
                              paths [paths ...]

positional arguments:
  paths                 At least one path to the notebook directory (one that
                        contains note.json file).

optional arguments:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Directory to put output files.
  --format FORMAT       Pandoc supported output format.
  --default-lang DEFAULT_LANG
                        Language to be used if there is no interpreter
                        annotation.
```

### Code extraction

```bash
usage: airship-convert extract [-h] [--output-dir OUTPUT_DIR]
                               [--language {scala,python}]
                               paths [paths ...]

positional arguments:
  paths                 At least one path to the notebook directory (one that
                        contains note.json file).

optional arguments:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
                        Directory to put output files.
  --language {scala,python}
                        Which language should be extracted.
```

Powered by:

- [`pypandoc`](https://github.com/bebraw/pypando) - A wrapper for [Pandoc](http://johnmacfarlane.net/pandoc/).
- [`toolz`](https://github.com/pytoolz/toolz) - A functional standard library for Python.
