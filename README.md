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
  paths

optional arguments:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
  --format FORMAT
  --default-lang DEFAULT_LANG
```

### Code extraction

```bash
usage: airship-convert extract [-h] [--output-dir OUTPUT_DIR]
                               [--language LANGUAGE]
                               paths [paths ...]

positional arguments:
  paths

optional arguments:
  -h, --help            show this help message and exit
  --output-dir OUTPUT_DIR
  --language {scala,python}
```
