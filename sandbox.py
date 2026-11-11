import random
import polars as pl

# df = pl.scan_parquet("data/taxi/yellow*.parquet")
# sum_per_vendor = df.group_by("VendorID").agg(
#     pl.col("total_amount").sum(), pl.col("trip_distance").sum()
# )

# income_per_dist_per_vendor = sum_per_vendor.select(
#     "VendorID",
#     income_per_dist=pl.col("total_amount") / pl.col("trip_distance"),
# )

# top_3 = income_per_dist_per_vendor.sort(by="income_per_dist", descending=True).head(3)

# print(top_3.collect())
lf_products = pl.LazyFrame(
    {
        "id": [x for x in range(1, 4, 1)],
        "name": ["Shoe", "bag", "playstation"],
        "weight": [23, 15, 100],
    }
)

lf_orders = pl.LazyFrame(
    {
        "id": [x for x in range(1, 11, 1)],
        "product_id": [random.randint(1, 3) for _ in range(10)],
        "quantity": [random.randint(20, 50) for _ in range(10)],
    }
)
lf_join = lf_orders.join(other=lf_products, left_on="product_id", right_on="id")
lf_join = lf_join.select(
    [
        col
        for col in lf_join.collect_schema().names
        if not col.lower().startswith("prod")
    ],
    total_weight=pl.col("quantity") * pl.col("weight"),
)
# print(lf_join.sort("id").collect())

penguins = pl.read_csv("data/penguins.csv")

dbase = pl.read_database_uri(
    """
SELECT * 
FROM Technolgies
""",
    uri="postgresql://db_apiasv_user:Ao9xbbav3I69nWpFDxQ7YmbICzSYGuFx@dpg-d8bm7gojo6nc73e6hdhg-a.frankfurt-postgres.render.com/db_apiasv",
)
print(dbase)
