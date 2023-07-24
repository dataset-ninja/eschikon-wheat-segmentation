Dataset **EWS Dataset** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/w/X/ZQ/5dWY1mUW10f69AyaKrbvrSYNZljiypIvz2kMHetPfrhpdK1IQ7j25xRDYZ8yN0iA4lUmHZc2e63cLFbDb9BIXrpFh2vkX529vSsh04JqGHQT0gbyQDRzAnMDyyUS.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='EWS Dataset', dst_path='~/dtools/datasets/EWS Dataset.tar')
```
The data in original format can be 🔗[downloaded here](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/512332/EWS-Dataset.zip?sequence=2&isAllowed=y)