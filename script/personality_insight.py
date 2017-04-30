import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
import os
import personality_insight_conf as conf
import uuid
from copy import deepcopy

std_module = {
   "content": "",
   "contenttype": "text/plain",
   "created": 0,
   "id": "",
   "language": "en"
   }

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username=conf.personality_insight_conf['username'],
    password=conf.personality_insight_conf['password'])


def get_personality(profile_json):
    profile = personality_insights.profile(profile_json, content_type='application/json',
                                            raw_scores=False, consumption_preferences=False)
    return json.dumps(profile, indent=2)

def create_dataset(timeline_data):
   profile_json = {'contentItems': []}
   for ind in timeline_data:
      ind_block = deepcopy(std_module)
      ind_block['id'] = str(uuid.uuid1())
      ind_block.update(ind)
      profile_json['contentItems'].append(ind_block)
   return profile_data


def personaility_analysis(timeline_data):
   profile_data = create_dataset(timeline_data)
   return(get_personality(json.dumps(profile_data, ensure_ascii=False)))

if __name__ == "__main__":
   profile_json = {
       "contentItems": [
          {
             "content": "Wow, I liked @TheRock before, now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass",
             "contenttype": "text/plain",
             "created": 1447639154000,
             "id": "666073008692314113",
             "language": "en"
          },
          {
             "content": ".@TheRock how did you Know to listen to your gut and Not go back to football? #Masterclass",
             "contenttype": "text/plain",
             "created": 1447638226000,
             "id": "666069114889179136",
             "language": "en"
          },
          {
             "content": ".@TheRock moving back in with your parents so humbling. \" on the other side of your pain is something good if you can hold on\" #masterclass",
             "contenttype": "text/plain",
             "created": 1447638067000,
             "id": "666068446325665792",
             "language": "en"
          },
          {
             "content": "Wow aren't you loving @TheRock and his candor? #Masterclass",
             "contenttype": "text/plain",
             "created": 1447637459000,
             "id": "666065895932973057",
             "language": "en"
          },
          {
             "content": "RT @patt_t: @TheRock @Oprah @RichOnOWN @OWNTV this interview makes me like you as a fellow human even more for being so real.",
             "contenttype": "text/plain",
             "created": 1447637030000,
             "id": "666064097562247168",
             "language": "en"
          },
          {
             "content": "\"Be You\".. That's the best advice ever @TheRock #MastersClass",
             "contenttype": "text/plain",
             "created": 1447636205000,
             "id": "666060637181644800",
             "language": "en"
          },
          {
             "content": "Supersoulers let's lift our spirits pray and hold Paris in the Light\ud83d\ude4f\ud83c\udffe",
             "contenttype": "text/plain",
             "created": 1447602477000,
             "id": "665919171062927360",
             "language": "en"
          },
          {
             "content": "RT @DeepakChopra: What I learned in week 1: Become What You Believe 21-Day Meditation Experience - https:\/\/t.co\/kqaMaMqEUp #GoogleAlerts",
             "contenttype": "text/plain",
             "created": 1447098990000,
             "id": "663807393063538688",
             "language": "en"
          },
          {
             "content": "Watching Bryan Stevenson on #SuperSoulSunday! \"You are not the worst mistake you ever made\".\nAren't we glad  about that.",
             "contenttype": "text/plain",
             "created": 1446998643000,
             "id": "663386507856736257",
             "language": "en"
          },
          {
             "content": ".@CherylStrayed  BRAVE ENOUGH my new favorite thing! Gonna buy a copy for all my girls. #Perfectgift https:\/\/t.co\/gz1tnv8t8K",
             "contenttype": "text/plain",
             "created": 1446915955000,
             "id": "663039689360695296",
             "language": "en"
          },
          {
             "content": "Stevie Wonder singing \"Happy Birthday to you!\" to my dear  mariashriver. A phenomenal woman and\u2026 https:\/\/t.co\/Ygm5eDIs4f",
             "contenttype": "text/plain",
             "created": 1446881193000,
             "id": "662893888080879616",
             "language": "en"
          },
          {
             "content": "It\u2019s my faaaaavorite time of the Year!  For the first time you can shop the list on @amazon! https:\/\/t.co\/a6GMvVrhjN https:\/\/t.co\/sJlQMROq5U",
             "contenttype": "text/plain",
             "created": 1446744186000,
             "id": "662319239844380672",
             "language": "en"
          },
          {
             "content": "Incredible story \"the spirit of the Lord is on you\" thanks for sharing @smokey_robinson #Masterclass",
             "contenttype": "text/plain",
             "created": 1446428929000,
             "id": "660996956861280256",
             "language": "en"
          },
          {
             "content": "Wasnt that incredible story about @smokey_robinson 's dad leaving his family at 12. #MasterClass",
             "contenttype": "text/plain",
             "created": 1446426630000,
             "id": "660987310889041920",
             "language": "en"
          },
          {
             "content": "Gayle, Charlie, Nora @CBSThisMorning  Congratulations!  #1000thshow",
             "contenttype": "text/plain",
             "created": 1446220097000,
             "id": "660121050978611205",
             "language": "en"
          },
          {
             "content": "I believe your home should rise up to meet you. @TheEllenShow you nailed it with HOME.  Tweethearts, grab a copy! https:\/\/t.co\/iFMnpRAsno",
             "contenttype": "text/plain",
             "created": 1446074433000,
             "id": "659510090748182528",
             "language": "en"
          },
          {
             "content": "Can I get a Witness?!\u270b\ud83c\udffe https:\/\/t.co\/tZ1QyAeSdE",
             "contenttype": "text/plain",
             "created": 1445821114000,
             "id": "658447593865945089",
             "language": "en"
          },
          {
             "content": ".@TheEllenShow you're a treasure.\nYour truth set a lot of people free.\n#Masterclass",
             "contenttype": "text/plain",
             "created": 1445821003000,
             "id": "658447130026188800",
             "language": "en"
          },
          {
             "content": "Hope you all are enjoying @TheEllenShow on #MasterClass.",
             "contenttype": "text/plain",
             "created": 1445820161000,
             "id": "658443598313181188",
             "language": "en"
          },
          {
             "content": ".@GloriaSteinem, shero to women everywhere, on how far we\u2019ve come and how far we need to go. #SuperSoulSunday 7p\/6c.\nhttps:\/\/t.co\/3e7oxXW02J",
             "contenttype": "text/plain",
             "created": 1445811545000,
             "id": "658407457438363648",
             "language": "en"
          },
          {
             "content": "RT @TheEllenShow: I told a story from my @OWNTV's #MasterClass on my show. Normally I\u2019d save it all for Sunday, but @Oprah made me. https:\/\u2026",
             "contenttype": "text/plain",
             "created": 1445804181000,
             "id": "658376572521459712",
             "language": "en"
          },
          {
             "content": ".@TheEllenShow is a master teacher of living her truth &amp; living authentically as herself. #MasterClass tonight 8\/7c.\nhttps:\/\/t.co\/iLT2KgRsSw",
             "contenttype": "text/plain",
             "created": 1445804072000,
             "id": "658376116575449088",
             "language": "en"
          },
          {
             "content": ".@SheriSalata , @jonnysinc @part2pictures . Tears of joy and gratitude to you and our entire #BeliefTeam We DID IT!! My heart is full.\ud83d\ude4f\ud83c\udffe\ud83d\ude4f\ud83c\udffe",
             "contenttype": "text/plain",
             "created": 1445734755000,
             "id": "658085377140363264",
             "language": "en"
          },
          {
             "content": "Donna and Bob saw the tape of their story just days before she passed. They appreciated it. #RIPDonna",
             "contenttype": "text/plain",
             "created": 1445734097000,
             "id": "658082618819280896",
             "language": "en"
          }
       ]
    }


   profile_data = [
      {'created': 1447639154000, 'content': "Wow, I liked @TheRock before, now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass"},
      {'created': 1447638226000, 'content': "@TheRock how did you Know to listen to your gut and Not go back to football? #Masterclass"},
      {'created': 1447638067000, 'content': "@TheRock moving back in with your parents so humbling. \" on the other side of your pain is something good if you can hold on\" #masterclass"},
      {'created': 1447637459000, 'content': "Wow aren\'t you loving @TheRock and his candor? #Masterclass"},
      {'created': 1447637030000, 'content': "RT @patt_t: @TheRock @Oprah @RichOnOWN @OWNTV this interview makes me like you as a fellow human even more for being so real."},
      {'created': 1447636205000, 'content': "\"Be You\".. That's the best advice ever @TheRock #MastersClass"},
      {'created': 1447602477000, 'content': "Supersoulers let's lift our spirits pray and hold Paris in the Light\ud83d\ude4f\ud83c\udffe"},
      {'created': 1447098990000, 'content': "Watching Bryan Stevenson on #SuperSoulSunday! \"You are not the worst mistake you ever made\".\nAren't we glad  about that."},
   ]
   profile_data = create_dataset(profile_data)
   print(profile_json)
   raw_input('Check')
   print(get_personality(json.dumps(profile_json, ensure_ascii=False)))
