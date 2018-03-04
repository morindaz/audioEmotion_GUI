#coding=utf-8
import os
import xml.dom.minidom
import pickle
import re
import csv
import numpy as np
#import highQualVid
#from cut_function import cut_type

def VidClip(start,end,video,typedir):
    if start < 0:
        start = 0
    start_long = int(start*100)
    end_long = int(end*100)
    duration = end - start
    name = video +'_'+ str(start_long) +'to'+ str(end_long) +'_'+ typedir +'.wav'
    #name = video +'_'+ str(start) +'to'+ str(end) +'_'+ typedir +'.mp4'
    #print(name)
    INPUT_DIR = 'E:\\morindaz\\C0005\\'
    # INPUT_DIR = '/Users/Seria/Desktop/Luck/microExpression/front_mp4/'
    VID_DIR = 'C:\\Users\\Mypc\\Desktop\\morindaz\\mm\\'
    # VID_DIR = '/Users/Seria/Desktop/Luck/microExpression/video_mp4/'
    if not os.path.exists(VID_DIR + typedir + '/' + name):
        os.system('ffmpeg -i ' + INPUT_DIR + video + '.wav -ss ' \
                    + str(start) + ' -t ' + str(duration) + ' ' + VID_DIR \
                    + typedir + '/' + name)


emo_type = ['1. Love','2. Optimism','3. Admiration','4. Gratitude','5. Desire',
        '6. Sincerity','7. vitality','8. Trust','9. Acceptance','10. Harmony',
        '11. Serenity','12. Calm','13. Boastfulness','14. Pride','15. Bravery',
        '16. Defiance','17. Contempt','18. Deceptiveness','19. Insincerity','20. Annoyance',
        '21. Envy','22. Suspicion','23. Pessimism','24. Disapproval','25. Pensiveness',
        '26. Conflict','27. Insult','28. Neglect','29. Fatigue','30. Tension',
        '31. Passiveness','32. Boredom','33. Distraction','34. Apprehension','35. Uneasiness',
        '36. Remorse','37. Shame','38. Embarrassed','39. Puzzlement','40. Cowardice',
        '41. Awe','42. Anticipation','43. Interest','44. Hate','45. Depression',
        '46. Grievance','47. Aggressiveness','48. Submission','49. Joy','50. Angry',
        '51. Disgust','52. Sadness','53. Fear','54. Surprise']

# record the footage errors
OUT_DIR = 'C:\\Users\\Mypc\\Desktop\\morindaz\\mm\\'
#SCORE_DIR = '/Users/Seria/Desktop/Luck/microExpression/score/'
error_log = open(OUT_DIR+'error_log.txt', 'w')
#qualifiers = open(SCORE_DIR+'qualifiers.txt', 'r')
# make directories
p=re.compile(r'[a-zA-Z]+', re.I)
for etype in emo_type:
    emotion=p.findall(etype)
    CLIP_DIR = OUT_DIR+emotion[0]
    if not os.path.exists(CLIP_DIR):
        os.system('mkdir '+CLIP_DIR)

ANNOT_DIR = 'E:\\morindaz\\C0005\\'

for _, _, files in os.walk(ANNOT_DIR):
    for filename in files:
        if filename.split('.')[-1] != 'anvil':
            continue

        dom = xml.dom.minidom.parse(ANNOT_DIR + filename)
        tracks = dom.getElementsByTagName('track')

        # questions
        if len(tracks) == 0:
            print(filename + ' empty_tag')
            continue
        questions_dom = tracks[0].getElementsByTagName('el')
        
        filename_init = ' '
        for q in questions_dom:
            questions = {}
            try:
                #-------------------|
                questions['filename'] = filename.split('.')[:-1][0]
                questions['start'] = q.getAttribute('start')
                questions['end'] = q.getAttribute('end')
                questions['type'] = q.getElementsByTagName('attribute')[0].firstChild.data
                #-------------------|
            except Exception as e:
                print(filename, e)
            
            #print(questions)
            if 'type' not in questions.keys():
                error_log.write(questions['filename']+': '+questions['start']\
                                +' to '+questions['end']+'\n')
            else:
                q_type=p.findall(questions['type'])
                vid = questions['filename']
                #if vid[:-4] == 
                #print(vid);
                VidClip(float(questions['start']), float(questions['end']), \
                    vid, q_type[0])
error_log.close()