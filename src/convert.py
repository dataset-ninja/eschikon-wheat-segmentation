import supervisely as sly
import os
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_size
import shutil
import cv2

from tqdm import tqdm


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer...", total=fsize) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    datasets = [
        "/mnt/c/Users/German/Documents/EWS-Dataset/test",
        "/mnt/c/Users/German/Documents/EWS-Dataset/train",
        "/mnt/c/Users/German/Documents/EWS-Dataset/validation",
    ]

    def load_image_labels(image_path, labels_path):
        image_info = api.image.upload_path(dataset.id, os.path.basename(image_path), image_path)
        mask = cv2.imread(labels_path, cv2.IMREAD_GRAYSCALE)
        # cv2.imwrite(image_info.name, mask)
        thresh = 127
        im_bw = cv2.threshold(mask, thresh, 255, cv2.THRESH_BINARY)[1]
        mask = cv2.bitwise_not(im_bw)
        labels = []
        height = image_info.height
        width = image_info.width
        bitmap_annotation = sly.Bitmap(
            mask,
        )
        obj_class = meta.get_obj_class("Wheat")
        label = sly.Label(bitmap_annotation, obj_class)
        labels.append(label)
        ann = sly.Annotation(img_size=[height, width], labels=labels)
        api.annotation.upload_ann(image_info.id, ann)

    project = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta()

    obj_class = sly.ObjClass("Wheat", sly.Bitmap)
    meta = meta.add_obj_class(obj_class)
    api.project.update_meta(project.id, meta)

    for single_dataset in datasets:
        mask_path = sly.fs.list_files(single_dataset, valid_extensions=[".png"])
        dictionary = dict({})
        pbar = tqdm(desc=os.path.basename(single_dataset), total=len(mask_path) / 2)
        for path in mask_path:
            path_filename = sly.fs.get_file_name(path)
            path_parts = path_filename.rstrip().split("_")
            # print(path_parts)
            if len(path_parts) <= 5:
                dictionary[path] = path[:-4] + "_mask.png"

        dataset = api.dataset.create(project.id, os.path.basename(single_dataset))
        # upload masks to images
        for k, v in dictionary.items():
            try:
                load_image_labels(k, v)
                pbar.update(1)
            except Exception as e:
                print(e)
                pbar.update(1)
                continue
        pbar.close()
    print(f"Dataset {dataset.name} has been successfully created.")
    return project
