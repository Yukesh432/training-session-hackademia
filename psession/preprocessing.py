import pandas as pd

def preprocess_single_input(df, scaler, label_encoder, model):

    categorical_cols = df.select_dtypes(include=["object"]).columns
    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns

    categorical_data = df[categorical_cols].copy()
    numerical_data = df[numerical_cols].copy()

    # Encode shelf
    numerical_data["shelf"] = label_encoder.transform(numerical_data["shelf"])

    # Ensure numerical column order matches scaler training
    numerical_data = numerical_data[list(scaler.feature_names_in_)]

    # Scale
    numerical_data = pd.DataFrame(
        scaler.transform(numerical_data),
        columns=scaler.feature_names_in_
    )

    # One-hot encode categorical
    cat_data = pd.get_dummies(categorical_data, columns=["mfr", "type"])

    df_processed = pd.concat([numerical_data, cat_data], axis=1)

    # ---------------------------
    # Align with model columns
    # ---------------------------
    expected_cols = list(model.feature_names_in_)

    for col in expected_cols:
        if col not in df_processed.columns:
            df_processed[col] = 0

    df_processed = df_processed[expected_cols]

    return df_processed