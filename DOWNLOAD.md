Dataset **EWS** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/e/8N/0EvPlQkq0tdPEDuEr3HbT4qLNoO2Ps52zG0S5AdXsntgUXuJeNd5d2nRkvYV1aAJYkydiWEdCzgWNm570HgtytdIE1VeZ4Bd7p8dIyTEXcYSA3R1FQSmFmatWiDr.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='EWS', dst_path='~/dtools/datasets/EWS.tar')
```
The data in original format can be 🔗[downloaded here](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/512332/EWS-Dataset.zip?sequence=2&isAllowed=y)