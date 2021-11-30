import init_context
import pset

sc,sp = init_context.init_context()
def read_data():
    if sc and sp :
        df = sp.read.format("json").option("header","true").option("mode","FAILFAST").option("inferSchema","True").load(pset.data_path)
        return df
