---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


```{code-cell} python3
from myst_nb import glue
import yaml
try:
    with open('_config.yml') as f:
        config = next(yaml.load_all(f, Loader=yaml.FullLoader))
except FileNotFoundError:
    print('No config file found')
# let's prime a bunch of variables
glue("replmd", config["other"]["replmd"])
```
