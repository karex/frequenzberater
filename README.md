# FrequenzBerater

Get lemma frequencies from the [NoWaC frequency list](https://www.hf.uio.no/iln/english/about/organization/text-laboratory/services/nowac-frequency.html) and append it your file. Dictionary cleaned and licensed under [CC BY-NC-SA 2.0](https://creativecommons.org/licenses/by-nc-sa/2.0/).

Usage:
```
py -3 freq.py input.tsv output.tsv
```

Input file is a tab-separated values file with the following columns: frekvens, lemma, ordklasse.
