# Scisort - Sort files optimized for science

WIP

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

- README not on top
- Numbered files naively sorted `output/simulation/Bos_2018/metrics_sim_Bos_2018_XXX.json`

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

## Scisort sorting

```python
import scisort

sorted(files, key=scisort.scisort_keygen)
```

```python
['README.md',
 'LICENSE.txt',
 'data',
 'data/Bos_2018.csv',
 'scripts',
 'scripts/get_plot.py',
 'scripts/merge_descriptives.py',
 'scripts/merge_metrics.py',
 'output',
 'output/simulation',
 'output/simulation/Bos_2018',
 'output/simulation/Bos_2018/descriptives',
 'output/simulation/Bos_2018/descriptives/data_stats_Bos_2018.json',
 'output/simulation/Bos_2018/descriptives/wordcloud_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_irrelevant_Bos_2018.png',
 'output/simulation/Bos_2018/descriptives/wordcloud_relevant_Bos_2018.png',
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
 'output/tables/data_metrics.xlsx',
 'jobs.sh']
```

## License

[MIT](/LICENSE)

## Contact

Scisort is developed and maintained by Jonathan de Bruin ([jonathandebruinos@gmail.com](email:jonathandebruinos@gmail.com)).
