from torch.utils.data import Dataset

import os

class WaymoDetectionDataset(Dataset):

    def __init__(self, split_set='train', num_points=40000,
                 use_color=False, use_height=False, augment=False):

        # TODO if you have loading errors probably look here first!
        self.data_path = os.path.join('/work/data', 'waymo_train_dataset')

        # TODO implement logic for split sets other than train
        self.scan_names = list(set([file for file in  os.listdir() if 'npy' in file]))

        self.num_points = num_points
        self.use_color = use_color
        self.use_height = use_height
        self.augment = augment
