from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "EWS"
PROJECT_NAME_FULL: str = "EWS: Eschikon Wheat Segmentation Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.Agricultural(),
    Research.Genetic(),
]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2021-11-30"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://doi.org/10.3929/ethz-b-000512332"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1680073
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/eschikon-wheat-segmentation"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/512332/EWS-Dataset.zip?sequence=2&isAllowed=y"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://doi.org/10.3389/fpls.2021.774068"
CITATION_URL: Optional[str] = "https://www.research-collection.ethz.ch/handle/20.500.11850/512332"
AUTHORS: Optional[List[str]] = [
    "Zenkl, Radek",
    "Kirchgessner, Norbert",
    "Roth, Lukas",
    "Hund, Andreas",
    "Walter, Achim",
    "Aasen, Helge",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "ETH Zurich, Switzerland",
    "Agroscope, Switzerland",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://ethz.ch/en.html",
    "https://www.agroscope.admin.ch/agroscope/en/home.html",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
