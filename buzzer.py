#Written by Andi Dinata
'''
Here is Happy Birthday Song:
note= ['C3','C3','D3','C3','F3','E3','0',
        'C3','C3','D3','C3','G3','E3','0',
        'C3','C3','C4','A3','F3','F3','E3','D2','0',
        'AS3','AS3','A3','F3','G3','F3']

duration=[0.2,0.2,0.4,0.4,0.4,0.8,0.2,
        0.2,0.2,0.4,0.4,0.4,0.8,0.2,
        0.2,0.2,0.4,0.4,0.2,0.2,0.4,0.4,0.4,
        0.2,0.2,0.4,0.4,0.4,0.4]
'''

  "C2":"65",
        tone_list=[]
        for i in note:
            tone_list.append(int(tone[i]))
        print(tone_list)

        for p in tone_list: