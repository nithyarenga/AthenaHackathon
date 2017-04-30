import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features
import alchemy_conf as conf

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username=conf.alchemy_conf['username'],
    password=conf.alchemy_conf['password'])


def nl_processing(reqd_text):
    response = natural_language_understanding.analyze( text=reqd_text,
    features = [features.Entities(), features.Keywords(), features.Emotion(), features.Concepts(), features.Sentiment()])
    return json.dumps(response, indent=2)


if __name__ == "__main__":
    print(nl_processing("Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne."))
