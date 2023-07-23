# helltaker

## Requirements 

Since we are developing using [rye](https://github.com/mitsuhiko/rye/), we highly recommend building with [rye](https://github.com/mitsuhiko/rye/) as well. While it might work with the system's Python and pip, it could be unreliable depending on the versions of Python and the dependencies.

Rye can be installed from [here](https://rye-up.com/)

Resolve dependencies with rye:

```shell
$ rye sync
```

## Run

```shell
$ rye run python3.11 src/helltaker/main.py
```
