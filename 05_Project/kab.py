def main():
    stop_words={'win','tin','din','akken','deg','ɣef','ten','nsen','nniḍen','nneɣ','werǧin','aṭas','akked','tid','wid','kan','acu','ala','ara','ur','ihi','ayagi','amzun','ula','wagi','d','ad','ulac','nsen','nezzeh','akken','ayen','ugar','drus','ulac','yiwen','ama'}

    verbs=[]
    nouns=[]
    others={}
    asenqedh={'.','?','!',':'}
    tizdit={'-'}
    nounprefixes1={'a','i'}
    nounprefixes2={'ta','ti'}
    nounsuffixes={'an','en','in'}
    verbsprefixes={'ttwa','tettwa','tettu','ttu'}
    for line in open("/home/ngotts/LING-L545/wiki.txt"):
        precedent=''
        line=line.lower()
        line=line.replace('.','')
        line=line.replace(',','')
        line=line.replace(';','')
        line=line.replace('?','')
        line=line.replace(':','')
        line=line.replace('!','')
        line=line.replace('-',' ')
        line=line.replace('  ',' ')

        for awal in line.split():
             awal = awal.strip()
             if (awal not in stop_words and len(awal)>2):
             #ette ligne c'est pour chercher les noms et adjectifs commençant par a, i, te et ti, et ta. ou bien les noms ayant subis un état d'annexion
                if (awal.startswith('tu') or (awal.startswith('ta') or awal.startswith('te') or awal.startswith('ti')) and precedent!='ad') or (((awal.startswith('a') or awal.startswith('i') or awal.startswith('u')  ) and (not awal.endswith('i') and not awal.endswith('u')  and not awal.endswith('a') and len (awal)<=3)) or ((awal.startswith('yi') or awal.startswith('u') or awal.startswith('a') or awal.startswith('i')) and len(awal)>3 and (awal not in stop_words) and  precedent!='ad')):
                 nouns.append(awal)
                else:
                 if (awal not in stop_words):
                  if (precedent=='ad'or precedent=='d' or precedent=='t' or precedent=='id') or (awal.startswith('tt') or awal.startswith('ye') or awal.startswith('ye') or awal.startswith('te') or awal.endswith('an') or awal.endswith('ant') or (awal.endswith('iɣ') or awal.endswith('in'))) :
                   verbs.append (awal)
             precedent=awal

    print("\nImyagen:\n")
    for verb in verbs:
        print(verb)

    print("\nIsmawen d yirbiben:\n")
    for noun in nouns:
        if (noun.startswith('a') or noun.startswith('i') or noun.startswith('u')):
            print(noun, ' amalay')
        else:
            print(noun, ' unti')
    pass

if __name__ == '__main__':
    main()