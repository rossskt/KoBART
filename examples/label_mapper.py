import pandas as pd

class FAQLabelMapper():
    def __init__(self, filepath='faq/faq_label_map.tsv'):
        label_df = pd.read_csv(filepath, sep='\t', header=None)
        self._to_label = dict()
        self._to_index = dict()
        for index, label in label_df.to_dict('split')['data']:
            self._to_label[index] = label
            self._to_index[label] = index
    
    def to_label(self, index):
        label = self._to_label.get(index, '')
        if not label:
            raise Exception('The index doesn\'t exist: ' + str(index))
        return label
    
    def to_index(self, label):
        index = self._to_index.get(label, -1)
        if index < 0:
            raise Exception('The label doesn\'t exist: ' + label)
        return index

