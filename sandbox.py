import polars as pl

df = pl.scan_parquet("data/taxi/yellow*.parquet")
sum_per_vendor = df.group_by("VendorID").agg(
    pl.col("total_amount").sum(), pl.col("trip_distance").sum()
)

income_per_dist_per_vendor = sum_per_vendor.select(
    "VendorID",
    income_per_dist=pl.col("total_amount") / pl.col("trip_distance"),
)

top_3 = income_per_dist_per_vendor.sort(by="income_per_dist", descending=True).head(3)

print(top_3.collect())
