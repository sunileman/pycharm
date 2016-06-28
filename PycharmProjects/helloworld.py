import os
import sys

# Path for spark source folder
os.environ['SPARK_HOME']="/usr/local/spark"

# Append pyspark  to Python Path
sys.path.append("/usr/local/spark/python")
sys.path.append("/usr/local/spark/python/lib/py4j-0.9-src.zip")


try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print ("Successfully imported Spark Modules")

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)