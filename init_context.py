import os
import pset
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import findspark

def init_context():
    findspark.init('C:\Program Files\Spark')
    os.environ['PYSPARK_PYTHON'] =r'C:\Users\room102sys2\AppData\Local\Programs\Python\Python39'
    app_name = input("Give the app name:")
    sp = SparkSession.builder.appName(app_name).getOrCreate()
    sc = sp.sparkContext
    if sc and sp:
        return sc,sp
    else:
        return False, False

