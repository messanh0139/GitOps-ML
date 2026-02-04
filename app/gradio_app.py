import joblib
import gradio as gr
import pandas as pd

# Charger le modèle
model = joblib.load("model/model.joblib")

feature_names = [
    "distance_from_home",
    "distance_from_last_transaction",
    "ratio_to_median_purchase_price",
    "repeat_retailer",
    "used_chip",
    "used_pin_number",
    "online_order"
]

def predict(
    distance_from_home,
    distance_from_last_transaction,
    ratio_to_median_purchase_price,
    repeat_retailer,
    used_chip,
    used_pin_number,
    online_order
):
    data = pd.DataFrame([[
        float(distance_from_home),
        float(distance_from_last_transaction),
        float(ratio_to_median_purchase_price),
        float(repeat_retailer),
        float(used_chip),
        float(used_pin_number),
        float(online_order)
    ]], columns=feature_names)

    # Prédiction brute
    prediction = float(model.predict(data)[0]) 
    
    pred_str = f"{prediction:.1f}"

    # Texte explicatif
    if prediction == 1.0:
        message = " Cette transaction est frauduleuse"
    else:
        message = " Cette transaction n'est pas frauduleuse"

    return pred_str, message


iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Distance from home"),
        gr.Number(label="Distance from last transaction"),
        gr.Number(label="Ratio to median purchase price"),
        gr.Number(label="Repeat retailer"),
        gr.Number(label="Used chip"),
        gr.Number(label="Used PIN number"),
        gr.Number(label="Online order")
    ],
    outputs=[
        gr.Number(label="Prédiction"),
        gr.Textbox(label="Interprétation")
    ],
    title="Application de détection et de prédiction de fraudes",
    description="Application développée par **KODJO Messanh Yaovi**.\n\n"
        "Veuillez saisir les détails de la transaction ci-dessus pour prédire si elle est frauduleuse ou non."
)

if __name__ == "__main__":
    iface.launch()
