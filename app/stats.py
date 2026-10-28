import pandas as pd

def compute_stats(csv_path):
    # Read CSV
    df = pd.read_csv(csv_path)

    stats = {}
    # Transform string to real date
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])

    stats["total_workouts"] = df["start_time"].nunique()

    # Build workout Table 
    workouts = df.drop_duplicates(subset="start_time") #drop_duplicates() erstellt direkt eine Tabelle
    workouts = workouts[["title", "start_time", "end_time"]]
    workouts["duration"] = workouts["end_time"] - workouts["start_time"]

    # Calculate metrics
    seconds_per_workout = workouts["duration"].dt.total_seconds()
    minutes_per_workout = seconds_per_workout / 60
    hours_per_workout = minutes_per_workout / 60
    stats["total_duration_hours"] = round(hours_per_workout.sum(),2)

    stats["favorite_hour"] = workouts["start_time"].dt.hour.value_counts().index[0] #am häufigsten ein Workout gestartet

    # Workouts per month und best month
    workouts_per_month = workouts["start_time"].dt.month.value_counts().sort_index()
    stats["best_month"] = workouts_per_month.idxmax()

    # Top 5 Excersises
    stats["top_exercises"]= df["exercise_title"].value_counts().head(5)
    print(stats)

    # Personal Records
    stats["personal_records"] =df.groupby("exercise_title")["weight_kg"].max().sort_values(ascending=False).head(5)

    # Total Volume
    df["volume"] = df["weight_kg"] * df["reps"]
    stats["total_volume_kg"] = df["volume"].sum()
    return stats
