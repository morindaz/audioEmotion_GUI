# coding=utf-8
'''
批量生成54个文件夹
'''

import os
aa = []
lines = ['Acceptance', 'Admiration', 'Aggressiveness', 'Angry', 'Annoyance', 'Anticipation', 'Apprehension', 'Awe',
       'Boastfulness', 'Boredom', 'Bravery', 'Calm', 'Conflict', 'Contempt', 'Cowardice', 'Deceptiveness',
       'Defiance', 'Depression', 'Desire', 'Disapproval', 'Disgust', 'Distraction', 'Embarrassed', 'Envy',
       'Fatigue', 'Fear', 'Gratitude', 'Grievance', 'Harmony', 'Hate', 'Insincerity', 'Insult', 'Interest', 'Joy',
       'Love', 'Neglect', 'Optimism', 'Passiveness', 'Pensiveness', 'Pessimism', 'Pride', 'Puzzlement', 'Remorse',
       'Sadness', 'Serenity', 'Shame', 'Sincerity', 'Submission', 'Surprise', 'Suspicion', 'Tension', 'Trust',
       'Uneasiness', 'vitality']
for line in lines:
    cmd = "md "+line
    os.system(cmd)
    aa.append(line)
print aa