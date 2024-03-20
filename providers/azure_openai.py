#LANGCHAIN ACCESS from : https://python.langchain.com/docs/integrations/llms/azure_openai
# The API version you want to use: set this to `2023-12-01-preview` for the released version.
# export OPENAI_API_VERSION=2023-12-01-preview
# # The base URL for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
# export AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
# # The API key for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource.
# export AZURE_OPENAI_API_KEY=<your Azure OpenAI API key>



from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

# Interface implementation methods
def load_embedding_model():
    print("load_azure_openai_embedding")
    # Get the OpenAI Embedding
    return AzureOpenAIEmbeddings(
        azure_deployment="skypoint-embeddings",
    )

def load_llm():
    print("load_azure_openai_model")
    # Get the Azure OpenAI Chat Model
    return AzureChatOpenAI(
        temperature=0.3,
        azure_deployment="skypoint-gpt-4",
        streaming=True,
        verbose=True
    )


# DIRECT ACCESS
# From this getting started guide: https://github.com/Azure/azure-openai-samples/blob/main/quick_start/v1/01_OpenAI_getting_started.ipynb
# import re
# import requests
# import sys
# import os
# from openai import AzureOpenAI
# import tiktoken
# from dotenv import load_dotenv
# load_dotenv()

# client = AzureOpenAI(
#   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
#   api_key=os.getenv("AZURE_OPENAI_KEY"),  
#   api_version="2024-02-15-preview"
# )

# # Select the General Purpose curie model for text
# model = os.getenv("CHAT_COMPLETION_NAME")
# # where model is listed here: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models

# # Create your first prompt
# text_prompt = "Should oxford commas always be used?"

# response = client.chat.completions.create(
#   model=model,
#   messages = [{"role":"system", "content":"You are a helpful assistant."},
#                {"role":"user","content":text_prompt},])

# response.choices[0].message.content

# import numpy as np
# model=os.getenv("EMBEDDING_MODEL_NAME")
# def cosine_similarity(query_embedding, embeddings, distance_metric='cosine'):
#     if distance_metric == 'cosine':
#         distances = np.dot(embeddings, query_embedding) / (np.linalg.norm(embeddings) * np.linalg.norm(query_embedding))
#         distances = 1 - distances  
#     else:
#         raise ValueError("Métrica de distância não suportada. Utilize 'cosine'.")

#     return distances

# text = 'the quick brown fox jumped over the lazy dog'
# client.embeddings.create(input=[text], model=model).data[0].embedding

# compare several words
# automobile_embedding    = client.embeddings.create(input='automobile', model=model).data[0].embedding
# vehicle_embedding       = client.embeddings.create(input='vehicle', model=model).data[0].embedding
# dinosaur_embedding      = client.embeddings.create(input='dinosaur', model=model).data[0].embedding
# stick_embedding         = client.embeddings.create(input='stick', model=model).data[0].embedding

# print(cosine_similarity(automobile_embedding, vehicle_embedding))
# print(cosine_similarity(automobile_embedding, dinosaur_embedding))
# print(cosine_similarity(automobile_embedding, stick_embedding))

# import pandas as pd
# cnn_daily_articles = ['BREMEN, Germany -- Carlos Alberto, who scored in FC Porto\'s Champions League final victory against Monaco in 2004, has joined Bundesliga club Werder Bremen for a club record fee of 7.8 million euros ($10.7 million). Carlos Alberto enjoyed success at FC Porto under Jose Mourinho. "I\'m here to win titles with Werder," the 22-year-old said after his first training session with his new club. "I like Bremen and would only have wanted to come here." Carlos Alberto started his career with Fluminense, and helped them to lift the Campeonato Carioca in 2002. In January 2004 he moved on to FC Porto, who were coached by José Mourinho, and the club won the Portuguese title as well as the Champions League. Early in 2005, he moved to Corinthians, where he impressed as they won the Brasileirão,but in 2006 Corinthians had a poor season and Carlos Alberto found himself at odds with manager, Emerson Leão. Their poor relationship came to a climax at a Copa Sul-Americana game against Club Atlético Lanús, and Carlos Alberto declared that he would not play for Corinthians again while Leão remained as manager. Since January this year he has been on loan with his first club Fluminense. Bundesliga champions VfB Stuttgart said on Sunday that they would sign a loan agreement with Real Zaragoza on Monday for Ewerthon, the third top Brazilian player to join the German league in three days. A VfB spokesman said Ewerthon, who played in the Bundesliga for Borussia Dortmund from 2001 to 2005, was expected to join the club for their pre-season training in Austria on Monday. On Friday, Ailton returned to Germany where he was the league\'s top scorer in 2004, signing a one-year deal with Duisburg on a transfer from Red Star Belgrade. E-mail to a friend .',
#                         '(CNN) -- Football superstar, celebrity, fashion icon, multimillion-dollar heartthrob. Now, David Beckham is headed for the Hollywood Hills as he takes his game to U.S. Major League Soccer. CNN looks at how Bekham fulfilled his dream of playing for Manchester United, and his time playing for England. The world\'s famous footballer has begun a five-year contract with the Los Angeles Galaxy team, and on Friday Beckham will meet the press and reveal his new shirt number. This week, we take an in depth look at the life and times of Beckham, as CNN\'s very own "Becks," Becky Anderson, sets out to examine what makes the man tick -- as footballer, fashion icon and global phenomenon. It\'s a long way from the streets of east London to the Hollywood Hills and Becky charts Beckham\'s incredible rise to football stardom, a journey that has seen his skills grace the greatest stages in world soccer. She goes in pursuit of the current hottest property on the sports/celebrity circuit in the U.S. and along the way explores exactly what\'s behind the man with the golden boot. CNN will look back at the life of Beckham, the wonderfully talented youngster who fulfilled his dream of playing for Manchester United, his marriage to pop star Victoria, and the trials and tribulations of playing for England. We\'ll look at the highs (scoring against Greece), the lows (being sent off during the World Cup), the Man. U departure for the Galacticos of Madrid -- and now the Home Depot stadium in L.A. We\'ll ask how Beckham and his family will adapt to life in Los Angeles -- the people, the places to see and be seen and the celebrity endorsement. Beckham is no stranger to exposure. He has teamed with Reggie Bush in an Adidas commercial, is the face of Motorola, is the face on a PlayStation game and doesn\'t need fashion tips as he has his own international clothing line. But what does the star couple need to do to become an accepted part of Tinseltown\'s glitterati? The road to major league football in the U.S.A. is a well-worn route for some of the world\'s greatest players. We talk to some of the former greats who came before him and examine what impact these overseas stars had on U.S. soccer and look at what is different now. We also get a rare glimpse inside the David Beckham academy in L.A, find out what drives the kids and who are their heroes. The perception that in the U.S.A. soccer is a "game for girls" after the teenage years is changing. More and more young kids are choosing the European game over the traditional U.S. sports. E-mail to a friend .',
#                         'LOS ANGELES, California (CNN) -- Youssif, the 5-year-old burned Iraqi boy, rounded the corner at Universal Studios when suddenly the little boy hero met his favorite superhero. Youssif has always been a huge Spider-Man fan. Meeting him was "my favorite thing," he said. Spider-Man was right smack dab in front of him, riding a four-wheeler amid a convoy of other superheroes. The legendary climber of buildings and fighter of evil dismounted, walked over to Youssif and introduced himself. Spidey then gave the boy from a far-away land a gentle hug, embracing him in his iconic blue and red tights. He showed Youssif a few tricks, like how to shoot a web from his wrist. Only this time, no web was spun. "All right Youssif!" Spider-Man said after the boy mimicked his wrist movement. Other superheroes crowded around to get a closer look. Even the Green Goblin stopped his villainous ways to tell the boy hi. Youssif remained unfazed. He didn\'t take a liking to Spider-Man\'s nemesis. Spidey was just too cool. "It was my favorite thing," the boy said later. "I want to see him again." He then felt compelled to add: "I know it\'s not the real Spider-Man." This was the day of dreams when the boy\'s nightmares were, at least temporarily, forgotten. He met SpongeBob, Lassie and a 3-year-old orangutan named Archie. The hairy, brownish-red primate took to the boy, grabbing his hand and holding it. Even when Youssif pulled away, Archie would inch his hand back toward the boy\'s and then snatch it. See Youssif enjoy being a boy again » . The boy giggled inside a play area where sponge-like balls shot out of toy guns. It was a far different artillery than what he was used to seeing in central Baghdad, as recently as a week ago. He squealed with delight and raced around the room collecting as many balls as he could. He rode a tram through the back stages at Universal Studios. At one point, the car shook. Fire and smoke filled the air, debris cascaded down and a big rig skidded toward the vehicle. The boy and his family survived the pretend earthquake unscathed. "Even I was scared," the dad said. "Well, I wasn\'t," Youssif replied. The father and mother grinned from ear to ear throughout the day. Youssif pushed his 14-month-old sister, Ayaa, in a stroller. "Did you even need to ask us if we were interested in coming here?" Youssif\'s father said in amazement. "Other than my wedding day, this is the happiest day of my life," he said. Just a day earlier, the mother and father talked about their journey out of Iraq and to the United States. They also discussed that day nine months ago when masked men grabbed their son outside the family home, doused him in gas and set him on fire. His mother heard her boy screaming from inside. The father sought help for his boy across Baghdad, but no one listened. He remembers his son\'s two months of hospitalization. The doctors didn\'t use anesthetics. He could hear his boy\'s piercing screams from the other side of the hospital. Watch Youssif meet his doctor and play with his little sister » . The father knew that speaking to CNN would put his family\'s lives in jeopardy. The possibility of being killed was better than seeing his son suffer, he said. "Anything for Youssif," he said. "We had to do it." They described a life of utter chaos in Baghdad. Neighbors had recently given birth to a baby girl. Shortly afterward, the father was kidnapped and killed. Then, there was the time when some girls wore tanktops and jeans. They were snatched off the street by gunmen. The stories can be even more gruesome. The couple said they had heard reports that a young girl was kidnapped and beheaded --and her killers sewed a dog\'s head on the corpse and delivered it to her family\'s doorstep. "These are just some of the stories," said Youssif\'s mother, Zainab. Under Saddam Hussein, there was more security and stability, they said. There was running water and electricity most of the time. But still life was tough under the dictator, like the time when Zainab\'s uncle disappeared and was never heard from again after he read a "religious book," she said. Sitting in the parking lot of a Target in suburban Los Angeles, Youssif\'s father watched as husbands and wives, boyfriends and girlfriends, parents and their children, came and went. Some held hands. Others smiled and laughed. "Iraq finished," he said in what few English words he knows. He elaborated in Arabic: His homeland won\'t be enjoying such freedoms anytime soon. It\'s just not possible. Too much violence. Too many killings. His two children have only seen war. But this week, the family has seen a much different side of America -- an outpouring of generosity and a peaceful nation at home. "It\'s been a dream," the father said. He used to do a lot of volunteer work back in Baghdad. "Maybe that\'s why I\'m being helped now," the father said. At Universal Studios, he looked out across the valley below. The sun glistened off treetops and buildings. It was a picturesque sight fit for a Hollywood movie. "Good America, good America," he said in English. E-mail to a friend . CNN\'s Arwa Damon contributed to this report.'
# ]

# cnn_daily_article_highlights = ['Werder Bremen pay a club record $10.7 million for Carlos Alberto .\nThe Brazilian midfielder won the Champions League with FC Porto in 2004 .\nSince January he has been on loan with his first club, Fluminense .',
#                                 'Beckham has agreed to a five-year contract with Los Angeles Galaxy .\nNew contract took effect July 1, 2007 .\nFormer English captain to meet press, unveil new shirt number Friday .\nCNN to look at Beckham as footballer, fashion icon and global phenomenon .',
#                                 'Boy on meeting Spider-Man: "It was my favorite thing"\nYoussif also met SpongeBob, Lassie and an orangutan at Universal Studios .\nDad: "Other than my wedding day, this is the happiest day of my life"' 
# ]

# cnn_df = pd.DataFrame({"articles":cnn_daily_articles, "highligths":cnn_daily_article_highlights})

# cnn_df.head()  

# article1_embedding    = client.embeddings.create(input=cnn_df.articles.iloc[0], model=model).data[0].embedding
# article2_embedding    = client.embeddings.create(input=cnn_df.articles.iloc[1], model=model).data[0].embedding
# article3_embedding    = client.embeddings.create(input=cnn_df.articles.iloc[2], model=model).data[0].embedding

# print(cosine_similarity(article1_embedding, article2_embedding))
# print(cosine_similarity(article1_embedding, article3_embedding))