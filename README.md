# Scisort - Sort files optimized for science

WIP

## Installation

Scisort requires Python 3.6 or later.

```sh
pip install scisort
```

## Getting started

### Traditional sorting

```python
from pathlib import Path

def show_dir(p):
    for f in sorted(Path(p).iterdir()):
        if f.is_file():
            print(f)
        else:
            show_dir(f)

```

```python
>>> show_dir("example/example_makita")
LICENSE.txt
README.md
data/Bos_2018.csv
jobs.sh
output/simulation/Bos_2018/descriptives/data_stats_Bos_2018.json
output/simulation/Bos_2018/descriptives/wordcloud_Bos_2018.png
output/simulation/Bos_2018/descriptives/wordcloud_irrelevant_Bos_2018.png
output/simulation/Bos_2018/descriptives/wordcloud_relevant_Bos_2018.png
output/simulation/Bos_2018/metrics_sim_Bos_2018_0.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_1640.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3154.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3518.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3519.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3721.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_4612.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_4699.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_559.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_5673.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_6.json
output/simulation/Bos_2018/plot_recall_sim_Bos_2018.png
output/simulation/Bos_2018/state_files/sim_Bos_2018_0.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_1640.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3154.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3518.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3519.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3721.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_4612.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_4699.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_559.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_5673.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_6.asreview
output/tables/data_descriptives.csv
output/tables/data_descriptives.xlsx
output/tables/data_metrics.csv
output/tables/data_metrics.xlsx
scripts/get_plot.py
scripts/merge_descriptives.py
scripts/merge_metrics.py
```
<!--
Normal sorting
```
sorted(files)
```
 -->
<!--
print(json.dumps(sorted(files), indent=4))

 -->
<!--
Results in
```
[
    "README.md",
    "data",
    "installation.R",
    "requirements.txt",
    "scripts",
    "tests"
]
``` -->

The order is not intuitive.

## Scisort sorting

<!-- print(json.dumps(sorted(files, key=scisort.scisort_keygen), indent=4))
[
    "README.md",
    "installation.R",
    "requirements.txt",
    "data",
    "scripts",
    "tests"
] -->

```python
import scisort

sorted(files, key=scisort.scisort_keygen)
```

Same code as in the previous example, but now with a different sort key.
```python
import scisort
from pathlib import Path

def show_dir(p):
    for f in sorted(Path(p).iterdir(), key=scisort.scisort_keygen):
        if f.is_file():
            print(f)
        else:
            show_dir(f)

```

```python
>>> show_dir("example/example_makita")
README.md
LICENSE.txt
data/Bos_2018.csv
jobs.sh
output/simulation/Bos_2018/descriptives/data_stats_Bos_2018.json
output/simulation/Bos_2018/descriptives/wordcloud_Bos_2018.png
output/simulation/Bos_2018/descriptives/wordcloud_irrelevant_Bos_2018.png
output/simulation/Bos_2018/descriptives/wordcloud_relevant_Bos_2018.png
output/simulation/Bos_2018/metrics_sim_Bos_2018_0.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_6.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_559.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_1640.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3154.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3518.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3519.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_3721.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_4612.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_4699.json
output/simulation/Bos_2018/metrics_sim_Bos_2018_5673.json
output/simulation/Bos_2018/plot_recall_sim_Bos_2018.png
output/simulation/Bos_2018/state_files/sim_Bos_2018_0.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_6.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_559.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_1640.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3154.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3518.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3519.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_3721.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_4612.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_4699.asreview
output/simulation/Bos_2018/state_files/sim_Bos_2018_5673.asreview
output/tables/data_descriptives.csv
output/tables/data_descriptives.xlsx
output/tables/data_metrics.csv
output/tables/data_metrics.xlsx
scripts/get_plot.py
scripts/merge_descriptives.py
scripts/merge_metrics.py

```

```python
[
    "README.md",
    "installation.R",
    "requirements.txt",
    "data",
    "scripts",
    "tests"
]
```

## License

[MIT](/LICENSE)

## Contact

Scisort is developed and maintained by Jonathan de Bruin ([jonathandebruinos@gmail.com](email:jonathandebruinos@gmail.com)).
