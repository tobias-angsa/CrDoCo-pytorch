import numpy as np

from seg.utils.serialization import json_load
from seg.dataset.base_dataset import BaseDataset

#DEFAULT_INFO_PATH = './data/cityscapes/data.json'


class RealTrashDataset(BaseDataset):

    def __init__(self, 
                 root, 
                 list_path, 
                 set='val',
                 max_iters=None,
                 crop_size=(412, 412), 
                 mean=(128, 128, 128),
                 load_labels=False,
                 info_path=None, 
                 labels_size=None):

        super().__init__(root, list_path, set, max_iters, crop_size, labels_size, mean)

        self.load_labels = load_labels
        '''
        self.info = json_load(info_path)
        self.class_names = np.array(self.info['label'], dtype=np.str)
        self.mapping = np.array(self.info['label2train'], dtype=np.int)
        self.map_vector = np.zeros((self.mapping.shape[0],), dtype=np.int64)

        for source_label, target_label in self.mapping:
            self.map_vector[source_label] = target_label
        '''

    def get_metadata(self, name):
        img_file = self.root / 'images' / name
        #label_name = name.replace('leftImg8bit', 'gtFine_labelIds')
        #label_file = self.root / 'semantic_labels' / label_name
        return img_file#, label_file

    '''
    def map_labels(self, input_):
        return self.map_vector[input_.astype(np.int64, copy=False)]
    '''

    def __getitem__(self, index):
        img_file, name = self.files[index]
        #label = self.get_labels(label_file)
        #label = self.map_labels(label).copy()
        image = self.get_image(img_file)
        image = self.preprocess(image)
        return image.copy(), np.array(image.shape), name