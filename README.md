[![scisort_repocard.svg](https://github.com/J535D165/scisort/raw/main/scisort_repocard.svg)](github.com/j535d165/scisort)

# Scisort - Sort files optimized for science

Scisort is a fundamental package for sorting files in scientific repositories.
It's is typically useful for data respositories and other tools. For end
users, the tool [`scitree`](https://github.com/J535D165/scitree) is an
example of a tool for printing a sorted tree.

## Philosophy of scisort

- Read the README first, therefore I'm on top
- Before you install or use the content, I open the LICENSE.
- Files first, folders second
- Numbered files are [naturally sorted](https://en.wikipedia.org/wiki/Natural_sort_order)
- We love reproducible project structures
- We ignore, what git ignores


## Installation

Scisort requires Python 3.6 or later.

```sh
pip install scisort
```

## Getting started

### Traditional sorting

Consider the following project folder structure. It's a mixture of files and
folders. The folder is sorted on the file or folder name. Some reasons why
this sort is not intuitive:


```
files = ['LICENSE.txt',
 'README.md',
 'data',
 'data/Bos_2018.csv',
 'jobs.sh',
 'output',
 'output/simulation',
 'output/simulation/Bos_2018',
 'output/simulation/Bos_2018/descriptives',
 'output/simulation/Bos_2018/descriptives/data_stats_Bos_2018.json',
 'output/simulation/Bos_2018/descriptives/wordcloud_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_irrelevant_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_relevant_Bos_2018.png',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_0.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_1640.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3154.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3518.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3519.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3721.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_4612.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_4699.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_559.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_5673.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_6.json',
 'output/simulation/Bos_2018/plot_recall_sim_Bos_2018.png',
 'output/simulation/Bos_2018/state_files',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_0.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_1640.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3154.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3518.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3519.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3721.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_4612.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_4699.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_559.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_5673.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_6.asreview',
 'output/tables',
 'output/tables/data_descriptives.csv',
 'output/tables/data_descriptives.xlsx',
 'output/tables/data_metrics.csv',
 'output/tables/data_metrics.xlsx',
 'scripts',
 'scripts/get_plot.py',
 'scripts/merge_descriptives.py',
 'scripts/merge_metrics.py']
```

The files and folders are real research output created with `ASReview-makita`
(see [examples](examples)).

## Scisort sorting

Scisort integrates with Python's `sorted` by supplying the sort key.

```python
from scisort import scisort_keygen

sorted(files, key=scisort_keygen)
```

```python
['README.md',
 'LICENSE.txt',
 'jobs.sh',
 'data',
 'data/Bos_2018.csv',
 'scripts',
 'scripts/get_plot.py',
 'scripts/merge_descriptives.py',
 'scripts/merge_metrics.py',
 'output',
 'output/simulation',
 'output/simulation/Bos_2018',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_0.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_6.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_559.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_1640.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3154.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3518.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3519.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_3721.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_4612.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_4699.json',
 'output/simulation/Bos_2018/metrics_sim_Bos_2018_5673.json',
 'output/simulation/Bos_2018/plot_recall_sim_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives',
 'output/simulation/Bos_2018/descriptives/wordcloud_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_irrelevant_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_relevant_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/data_stats_Bos_2018.json',
 'output/simulation/Bos_2018/state_files',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_0.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_6.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_559.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_1640.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3154.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3518.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3519.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_3721.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_4612.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_4699.asreview',
 'output/simulation/Bos_2018/state_files/sim_Bos_2018_5673.asreview',
 'output/tables',
 'output/tables/data_descriptives.csv',
 'output/tables/data_descriptives.xlsx',
 'output/tables/data_metrics.csv',
 'output/tables/data_metrics.xlsx']
```

### Third party support

Scisort also integrates with other libraries implementing sorting based on a key.

#### Pandas

```python
import pandas as pd

from scisort import scisort_keygen_pandas

pd.Series(files).sort_values(key=scisort_keygen_pandas)
```

#### Natsort

```python
import natsort as ns

ns.natsorted(files, key=scisort_keygen)
```

## License

[MIT](/LICENSE)

## Contact

Scisort is developed and maintained by Jonathan de Bruin ([jonathandebruinos@gmail.com](email:jonathandebruinos@gmail.com)).
