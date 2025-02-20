import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "files/input/shipping-data.csv"

df = pd.read_csv(file_path)

output_folder = "docs"
os.makedirs(output_folder, exist_ok=True)


def create_visual_for_shipping_per_warehouse(df):
    df_copy = df.copy()
    plt.figure(figsize=(8, 5))

    counts = df_copy.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse Block",
        ylabel="Record Count",
        color="tab:blue",
        fontsize=8
    )


    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(f"{output_folder}/shipping_per_warehouse.png")
    plt.close()


def create_visual_for_mode_of_shipment(df):
    df_copy = df.copy()
    plt.figure(figsize=(8, 5))

    counts = df_copy.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title="Mode of Shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"]
    )


    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(f"{output_folder}/mode_of_shipment.png")
    plt.close()


def create_visual_for_average_customer_rating(df):
    df_copy = df.copy()
    plt.figure(figsize=(8, 5))

    stats = df_copy[["Mode_of_Shipment", "Customer_rating"]].groupby("Mode_of_Shipment").describe()
    stats.columns = stats.columns.droplevel()
    stats = stats[["mean", "min", "max"]]

 
    plt.barh(
        y=stats.index.values,
        width=stats["max"].values - 1,
        left=stats["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8
    )


    colors = ["tab:green" if value >= 3.0 else "tab:orange" for value in stats["mean"].values]
    plt.barh(
        y=stats.index.values,
        width=stats["mean"].values - 1,
        left=stats["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )

    plt.title("Average Customer Rating by Mode of Shipment")
    plt.xlabel("Customer Rating")
    plt.ylabel("Mode of Shipment")

    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)

    plt.savefig(f"{output_folder}/average_customer_rating.png")
    plt.close()
    return colors

def create_visual_for_weight_distribution(df):
    df_copy = df.copy()
    plt.figure(figsize=(8, 5))

    df_copy.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white"
    )

    plt.gca().spines["left"].set_color("gray")
    plt.gca().spines["bottom"].set_color("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.xlabel("Weight in grams")
    plt.ylabel("Frequency")

    plt.savefig(f"{output_folder}/weight_distribution.png")
    plt.close()

create_visual_for_shipping_per_warehouse(df)
create_visual_for_mode_of_shipment(df)
create_visual_for_average_customer_rating(df)
create_visual_for_weight_distribution(df)

def pregunta_01():

    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Shipping Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #333; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; }
        .image-container { width: 45%; margin: 10px; }
        img { width: 100%; border: 1px solid #ddd; border-radius: 5px; padding: 5px; }
    </style>
</head>
<body>
    <h1>Shipping Dashboard</h1>
    <div class="container">
        <div class="image-container">
            <img src="shipping_per_warehouse.png" alt="Fig 1">
            <p>Shipping per Warehouse</p>
        </div>
        <div class="image-container">
            <img src="mode_of_shipment.png" alt="Fig 2">
            <p>Mode of Shipment</p>
        </div>
        <div class="image-container">
            <img src="average_customer_rating.png" alt="Fig 3">
            <p>Average Customer Rating</p>
        </div>
        <div class="image-container">
            <img src="weight_distribution.png" alt="Fig 4">
            <p>Weight Distribution</p>
        </div>
    </div>
</body>
</html>
"""
    output_path = os.path.join("docs", "index.html")
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("El archivo 'index.html' ha sido generado en la carpeta 'docs'.")

pregunta_01()
