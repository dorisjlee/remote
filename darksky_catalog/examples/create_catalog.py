import pprint
import uuid

import darksky_catalog as dsc

catalog1 = dsc.DarkSkyCatalog(
    name = "Simple Test",
    authors = ["Your Name Here",],
    catalog_url = "http://localhost:8000/simulations/",
    datasets = [
      {'dataset_type': 'sdf_halo_catalog',
       'name': 'Halo Catalog One',
       'url': 'http://localhost:8000/simulations/hc1.sdf',
       'children': [],
       'authors': ['Your Name Here'],
       'uuid': uuid.uuid4().hex,
       'nhalos': 256*256*256,
       'sort_order': 'mass',
       'index_files': [],
       },
      {'dataset_type': 'sdf_halo_catalog',
       'name': 'Halo Catalog Two',
       'url': 'http://localhost:8000/simulations/hc2.sdf',
       'children': [],
       'authors': ['Your Name Here'],
       'uuid': uuid.uuid4().hex,
       'nhalos': 256*256*256,
       'sort_order': 'mass',
       'index_files': [],
       },
      ]
)

serialized1 = catalog1.serialized
print "Original:"
pprint.pprint(serialized1)

catalog2 = dsc.DarkSkyCatalog(**serialized1)
serialized2 = catalog2.serialized
print "Remade"
pprint.pprint(serialized2)

print "Identical:", serialized1 == serialized2
