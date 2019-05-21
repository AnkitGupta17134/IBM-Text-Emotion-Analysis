import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='QqhqLPufmUFVNLZaMvrkzvtKqHDVsfZDLF8cUNEHaaqL',
    url='https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2018-11-16')

response = natural_language_understanding.analyze(
    text='I Love IBM. There servies are cheap and the best so leave the rest.',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=2))).get_result()

print(json.dumps(response, indent=2))
