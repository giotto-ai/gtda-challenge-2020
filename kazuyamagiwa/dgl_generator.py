#%%
import networkx as nx
import numpy as np
import h5py
from dgl.data import MiniGCDataset

#%%
# Generate a dataset with 1200 samples.  Each graph is of size [10, 20]
dataset = MiniGCDataset(1200, 10, 20)

#%%
def converter(data):
    """
    Read data from dataset, convert to numpy adjacency matrix, and return matrix and label
    """
    graph, label = data
    graph = graph.to_networkx()
    adj = nx.to_numpy_matrix(graph)
    lab = int(label.numpy())
    return adj, lab

#%%
# Write dataset to hdf5 file

output_file = 'GDataset.h5'
h5file = h5py.File(output_file, 'w')

for i in range(0, 1200, 1):
    print(i)

    mat = converter(dataset[i])[0]
    digit = converter(dataset[i])[1]

    dir = 'index_'+str(np.int(i))
    h5file.create_group(dir)
    h5file.create_dataset(dir+'/adjacency_matrix', data= mat, compression='gzip', compression_opts=9)
    h5file.create_dataset(dir+'/label', data= digit)
    h5file.flush()

h5file.flush()
h5file.close()

# %%
#h5file.close()

#%%
