import re
import lxml
from lxml import html
import requests
from bs4 import BeautifulSoup
import pandas as pd

def brandaniethical(brandlist):
    """
    Get fashion brands' animal ethical usage information. provide information of whether the brand use fur, angora, down feather, shearling, karakul, exotic animal skin and hair, wool use including ‘mulesing’, and leather 
    Also check whether brands use these material align with standards.
    
    Parameters
    ----------
    brandlist : list
      A list of brands name that consumers want to know their condition of animal usage
    
    Returns
    -------
    pandas.dataframe
      The dataframe of brands ethical consumption of animal material which include usage of fur, angora, down feather, shearling, karakul, exotic animal skin and hair, wool use including ‘mulesing’, and leather. Also check whether brands use these material align with standards.
      
    Examples
    --------
    >>> from brandaniethical import brandaniethical 
    >>> fashion_animaterial(['cos','theory','lululemon','nike', 'skechers'])
	company	animal_score	update	fur	angora	leather	wool	shearling	karakul	down	feather	exotic animal hair	exotic animal skin	down_RDS	wool_mulesing
0	cos	3 out of 5	Last Updated: July 2020	0	0	1	1	0	0	1	0	1	0	1	1
1	theory	2 out of 5	Last Updated: December 2019	0	0	1	1	0	0	1	0	1	0	0	0
2	lululemon	2 out of 5	Last Updated: July 2020	0	0	1	1	0	0	1	0	1	0	1	0
3	nike	2 out of 5	Last Updated: July 2020	0	0	1	1	0	0	1	0	1	0	0	0
4	skechers	2 out of 5	Last Updated: August 2020	0	0	1	1	0	0	0	0	0	0	0	0
    """
    brandlist = [b.lower() for b in brandlist]
    ani_reg = '[^.]* animal [^.]*\.'
    use_reg = '[^.]* (uses) [^.]*\.'
    date_reg = '(Last Updated: )(\w*)'
    web = 'https://directory.goodonyou.eco/'
    animal_score = []
    ani_rate= []
    company = []
    update = []
    def brandani(brandlist):
        df_gfy=pd.DataFrame()
        for brand in brandlist:
            goypage = requests.get(web +'brand/'+ brand)
            soup = BeautifulSoup(goypage.content, 'html.parser')
            try:
                animal_score.append(str(soup.find_all("span", {"class": "StyledText-sc-1sadyjn-0 ccIhDL"})[2].string))
                ani_rate.append([string for string in soup.stripped_strings if re.search(ani_reg, string)][0])
                update.append([string for string in soup.stripped_strings if re.search(date_reg, string)][0]) 
            except (IndexError, TypeError, NameError, KeyError):
                print(f'please check company name of {brand}')
                pass
            else:
                df_gfy['company'] = pd.Series(brandlist)
                df_gfy['animal_score'] = pd.Series(animal_score)
                df_gfy['ani_rate'] = pd.Series(ani_rate)
                df_gfy['update'] = pd.Series(update)
                pd.set_option('display.max_colwidth', None)
        return df_gfy
    global dfydf
    dfydf = brandani(brandlist)
            #check animal material usage
    try:
        
        dfydf['ani_material'] = [re.search(use_reg, i).group(0) for i in dfydf['ani_rate']]

    except (IndexError, TypeError, NameError, KeyError):
        print(f'no animal material information')
        

    else:
        fabric = ['fur','angora', 'leather', 'wool', 'shearling', 'karakul', 'down', 'feather', 'exotic animal hair', 'exotic animal skin']
        for f in fabric:
            dfydf[f]=dfydf['ani_material'].str.contains(f)
                #check if use down whether down accredited by the Responsible Down Standar
        RDS_reg = 'It uses down accredited by the Responsible Down Standar'
        dfydf['down_RDS'] = dfydf['ani_rate'].str.contains(RDS_reg)
        dfydf.loc[dfydf['down_RDS']==True,'down'] = True
                #check if use wool whether wool includes mulesing
        dfydf['wool_mulesing'] = dfydf['ani_rate'].str.contains('mules')
        dfydf.loc[dfydf['wool_mulesing']==True,'wool'] = True
        df_aniusage = dfydf.loc[:,dfydf.columns!='ani_material']
        df_material = df_aniusage.replace(True,1)
        df_material = df_material.replace(False,0)
        
        return df_material.loc[:,df_material.columns!='ani_rate']
       