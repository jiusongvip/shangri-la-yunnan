import os

slugs = ['matsutake-mushrooms','morning-chanting','tibetan-barley-wine','tsampa','yak-butter-tea','yak-hotpot']

for slug in slugs:
    path = os.path.join('src','pages','food',f'{slug}.astro')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    idx = content.find('Also Try')
    if idx == -1:
        print(f'{slug}: NOT FOUND')
        continue
    
    div_start = content.rfind('<div class="mt-12', 0, idx)
    end = content.find('</DetailLayout>', div_start)
    
    new_content = content[:div_start] + '\n' + content[end:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'{slug}: removed')
