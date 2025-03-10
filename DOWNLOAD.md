Dataset **EWS** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE0MDZfRVdTL2V3cy1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJZaytlL1VkU1NOckJTbXUvN3VWZmpXVCtEWk1Ua1ZLRmc2bkNyTXAvOUtNPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='EWS', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/512332/EWS-Dataset.zip?sequence=2&isAllowed=y).