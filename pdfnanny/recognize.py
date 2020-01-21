import fasttext


def get_lang(model_path, text):
    """
    Returns the recognized text language

    in:     path to the model,
            text to analyze
    out:    map representing the text's language
    """
    model = fasttext.load_model(model_path)

    predictions = []
    for page in text:
        page_prediction = []
        for sentence in page.split("\n"):
            result = model.predict(sentence)
            lang = result[0]
            lang = lang[0][9:]
            page_prediction.append(lang)
        predictions.append(page_prediction)
    return predictions
