import pandas as pd
import glob
# the path is the address of the folder which  your questionnaire CSV files are located there
path =r''
filenames = glob.glob(path + "/*.csv")
# the new format for extracted data
main=pd.read_csv('Copy of Data_extraction_template_Barrier1.csv')


w=0
for filename in filenames:
    data = pd.read_csv(filename)
    Interviewer=data['Unnamed: 1'][data.index[data['Note:']=='Name of interviewee (e.g. Name on the top right of page 1 of MCLIB 94#survey/name mentioned in the title)'].tolist()[0]]
    Community=data['Unnamed: 3'][data.index[data['Unnamed: 2']=='Community'].tolist()[0]]
    HH=data['Unnamed: 5'][data.index[data['Unnamed: 4']=='Household(HH) Code'].tolist()[0]]

    q15=' '
    if(data['Unnamed: 2'][data.index[data['Note:']=='Q15 impact of industrial development'].tolist()[0]]=='x'):
        q15='1'
    elif(data['Unnamed: 4'][data.index[data['Note:']=='Q15 impact of industrial development'].tolist()[0]]=='x'): 
        q15='0'
        
    q15_n=str(data['Unnamed: 2'][data.index[data['Note:']=='Q15 impact of industrial development'].tolist()[0]+1])
    
    
    q16=' '
    if(data['Unnamed: 2'][data.index[data['Note:']=='Q16 impact of recreational development'].tolist()[0]]=='x'):
        q16='1'
    elif(data['Unnamed: 4'][data.index[data['Note:']=='Q16 impact of recreational development'].tolist()[0]]=='x'): 
        q16='0'   
    q16_n=str(data['Unnamed: 2'][data.index[data['Note:']=='Q16 impact of recreational development'].tolist()[0]+1])
    
    

    Q17_zone= data['Unnamed: 2'][data.index[data['Note:']=='Q17 Zones Where You Used to Hunt'].tolist()[0]]
    Q17_zone_n= data['Unnamed: 4'][data.index[data['Note:']=='Q17 Zones Where You Used to Hunt'].tolist()[0]]
    
    q18=' '
    if(data['Unnamed: 2'][data.index[data['Note:']=='Q18 sick animals'].tolist()[0]]=='x'):
        q18='1'
    elif(data['Unnamed: 4'][data.index[data['Note:']=='Q18 sick animals'].tolist()[0]]=='x'): 
        q18='0'
        
    Q18_n=data['Unnamed: 6'][data.index[data['Note:']=='Q18 sick animals'].tolist()[0]]
    
    array=[]
    ii = data.index[data['Note:'] == "Q14 Barriers to harvesting"].tolist()[0]
    other_note=0
    v=data.index[data['Note:'] == "Q15 impact of industrial development"].tolist()[0]-1
    while (ii < v):
        jj= 0
        for item in data.loc[ii+1]:

            if(item=='x'or item=='x (logging)'):
                jj+=1
            
        array.append(jj)
        ii+=1
    other=''
    bb=0
    
    
    main.loc[w] = [Interviewer,Community,HH,q15,q15_n,q16,q16_n,Q17_zone, Q17_zone_n,q18,Q18_n,array[7],array[8],array[9],array[10],array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[11]
                   
                  ]
    w+=1
