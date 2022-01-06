import pyspark

# Example of connecting to a Spark cluster
conf = pyspark.SparkConf()
conf.setMaster("spark://head_node:56887")
conf.set("spark.authenticate", True)
conf.set("spark.authenticate.secret", "secret-key")
sc1 = pyspark.SparkContext(conf=conf)
# End Spark cluster configuration

# sc = pyspark.SparkContext("local[*]")
# txt = sc.textFile("file:////Users/julio_briones/Documents/Dev/Python/Core/longer/exercises2/texting")
# print(txt.count())

# lines = txt.filter(lambda line: "python" in line.lower())
# print(lines.count())


"""
RDDs (resilient distributed datasets) parallelize. The following code creates an iterator of 10k elements and then
users parallelize() to distribute that data into 2 partitions:
"""
sc = pyspark.SparkContext("local[*]")
big_list = range(10000)
rdd = sc.parallelize(big_list, 2)
odds = rdd.filter(lambda x: x % 2 != 0)
print(odds.take(5))

