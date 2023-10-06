from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Conversão CSV para Parquet").getOrCreate()
sc = SparkContext.getOrCreate()

csv_caminho = r"C:\Users\arquivo.csv"
parquet_caminho = r"C:\Users\parquet"

tableschema = StructType([
    StructField('CAMPO_01', StringType(),nullable=True),
    StructField('CAMPO_02', IntegerType(),nullable=True),
    StructField('CAMPO_03', FloatType(),nullable=True),
    StructField('CAMPO_04', DataType(),nullable=True)
])

df = spark.read.csv(csv_caminho, header=True, sep=";", schema=tableschema)

df.write.mode("overwrite").parquet(parquet_caminho)

spark.stop()



