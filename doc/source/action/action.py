import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, SentimentOptions


def main(dict):
    try:
        model_id=""
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2018-04-05',
            iam_apikey="",
            url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')        
        resposta = natural_language_understanding.analyze(
            text=dict['texto'],
            features=Features(
                entities=EntitiesOptions(emotion=True, sentiment=True, model=model_id),
                sentiment=SentimentOptions()),
                ).get_result()
        retorno = {}

        # Salvar as entidades no retorno
        if 'entities' in resposta:
            for i in range(len(resposta['entities'])):
                retorno[resposta['entities'][i]['type']] = resposta['entities'][i]['text']

        # Salvar o sentimento no retorno
        if 'sentiment' in resposta:
            retorno['sentiment'] = resposta['sentiment']['document']['label']

        dict['err'] = False
        dict['resposta'] = retorno
        return dict

    except:
        dict['err'] = True
        dict['resposta'] = "Erro na chamada ao NLU."
        return dict
