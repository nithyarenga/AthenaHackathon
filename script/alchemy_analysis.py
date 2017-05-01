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
    return response


if __name__ == "__main__":
#    print(nl_processing("Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne."))
    print(nl_processing("Ever since I started seeing these people I have gotten better. It was slow at first(several months before results) because it took some time for me to build trust to be able to share my experiences in a vulnerable and truthful manner (for those that haven't been in therapy, it can be a real bitch to REALLY open yourself up to a stranger and hope they don't tear you apart and judge you, which counselors damn near never do, but the fear is there all the same). But after a lot of time, talking, and drugs (I am currently on depression, sleep, and mood meds and I haven't felt this normal since I left the military, which brings me to my next point)."))
