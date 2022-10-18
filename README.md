<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/J535D165/scisort/raw/main/scisort_repocard_dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/J535D165/scisort/raw/main/scisort_repocard.svg">
  <img alt="Scisort - Sort files in science projects." src="https://github.com/J535D165/scisort/raw/main/scisort_repocard.svg">
</picture>

# Scisort - Sort files in research projects

Scisort is a Python package for sorting files in research projects and
scientific (data) repositories. Files and folders are sorted in such a way
that inspecting folders in research projects is more intuitive. See the
[philosophy of scisort](#philosophy-of-scisort) to understand the sorting algorithm.

--- 

Since scisort is a low-level API, most researchers, developers, and data
scientists may be more interested in [`scitree`](https://github.com/J535D165/scitree).
Scitree is a smart recursive directory listing program that makes use of scisort.

---

## Philosophy of scisort

Philosophy of scisort and [scitree](https://github.com/J535D165/scitree):

- Read the README first, therefore I'm on top
- Before I install or use the content, I open the [LICENSE](https://choosealicense.com/).
- Files first, folders second
- Numbered files are [naturally sorted](https://en.wikipedia.org/wiki/Natural_sort_order)
- I love [intuitive and reproducible project structures](https://doi.org/10.1371/journal.pcbi.1005510)
- Follow the order of execution where possible
- I ignore, what git ignores\*

*\* Only for [`scitree`](https://github.com/J535D165/scitree).*

For more information about the structure, see [scisort/scisort/keygen.py](https://github.com/J535D165/scisort/blob/main/scisort/keygen.py). 

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

### Scisort sorting

Scisort integrates with Python's `sorted` by supplying the sort key.

```python
from scisort import scisort_keygen

sorted(files, key=scisort_keygen())
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

Scisort also integrates with other libraries implementing sorting based on a
key.

#### Pandas

```python
import pandas as pd

from scisort import scisort_keygen_pandas

pd.Series(files).sort_values(key=scisort_keygen_pandas())
```

#### Natsort

```python
import natsort as ns

ns.natsorted(files, key=scisort_keygen())
```

## License

[MIT](/LICENSE)

## Contact

Feel free to reach out with questions, remarks, and suggestions. The
[issue tracker](/issues) is a good starting point. You can also email me at
[jonathandebruinos@gmail.com](mailto:jonathandebruinos@gmail.com).
