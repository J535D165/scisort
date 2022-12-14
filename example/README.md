# Create example folder structures

The following sections provide examples of project (interesting) project structures. Download the
files and list them with the following Python code:

```python
from pathlib import Path
files = list(map(str,Path(".").glob("**/*")))
```

## Makita (`example_makita`)

Install ASReview and ASReview Makita
```sh
pip install asreview-makita
```

Build a simulation project and run the jobs.
```sh
mkdir -p example/example_makita/data
curl https://raw.githubusercontent.com/asreview/systematic-review-datasets/master/datasets/Bos_2018/output/Bos_2018.csv --output example/example_makita/data/Bos_2018.csv
cd example/example_makita/
asreview makita template arfi
touch LICENSE.txt
sh jobs.sh
```

## 10.5281/zenodo.4161444 (With Datahugger)

Install datahugger (`pip install datahugger`)

```
datahugger 10.5281/zenodo.4161444 example_GISANS/
unzip data.zip dwba_model_package.zip
```
