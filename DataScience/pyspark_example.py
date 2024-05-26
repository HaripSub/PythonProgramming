from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Example PySpark Program") \
    .getOrCreate()

# Read CSV file into DataFrame
input_file = "person_data.csv"
df = spark.read.csv(input_file, header=True, inferSchema=True)

# Show the DataFrame content
print("Original DataFrame:")
df.show(5)

# Select distinct cities
distinct_cities = df.select("location").distinct().orderBy("location")

# Collect the distinct city names
distinct_city_names = [row.location for row in distinct_cities.collect()]

# Print the distinct city names
print("Distinct city names:")
for city in distinct_city_names:
    print(city)

# Oldest living in Washington
df_senior_washington = df.filter(df.location == "Washington").orderBy(df["age"].desc())

# Show the filtered and sorted DataFrame
print("Top 5 Oldest citizens living in Washington")
df_senior_washington.show(5)

# Group by city and count the number of people in each city
person_city_counts = df.groupBy("location").count().orderBy("count", ascending=False)

# Show the count of people in each city
print("Count of people living in each city:")
person_city_counts.show()

# count of people with age 20-30 living in San Francisco
person_sans_fransisco_count = df.filter(
    (df.age >= 20) & (df.age <= 30) & (df.location.contains("San Francisco"))).count()

# Show the count of people with age 20-30 living in San Francisco
print("Number of people with age 20-30 living in San Francisco:", person_sans_fransisco_count)

# Count of senior citizens living in each city
count_senior_citizens = df.filter((df.age > 60)).groupBy("location").count().orderBy("count", ascending=False)
print("Count of senior citizens living in each city:")
count_senior_citizens.show()

# Count of teenagers living in each city
count_teenagers = df.filter((df.age >= 13) & (df.age <= 19)).groupBy("location").count().orderBy("count",
                                                                                                 ascending=False)
print("Count of teenagers living in each city:")
count_teenagers.show()

# Teenagers living in LosAngles ordered by the age
teenagers_Los_Angeles = df.filter((df.age >= 13) & (df.age <= 19) & (df.location == "Los Angeles")).orderBy("name")
print(" Teenagers living in LosAngles:")
teenagers_Los_Angeles.show()

spark.stop()
