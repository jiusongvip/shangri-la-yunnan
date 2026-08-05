import re, os

food_links = {
    'matsutake-mushrooms': ['yak-hotpot', 'yak-butter-tea', 'tibetan-barley-wine'],
    'morning-chanting': ['yak-butter-tea', 'tsampa'],
    'tibetan-barley-wine': ['tsampa', 'yak-hotpot', 'yak-butter-tea'],
    'tsampa': ['yak-butter-tea', 'tibetan-barley-wine', 'yak-hotpot'],
    'yak-butter-tea': ['tsampa', 'tibetan-barley-wine', 'morning-chanting'],
    'yak-hotpot': ['tibetan-barley-wine', 'matsutake-mushrooms', 'tsampa'],
}

food_names = {
    'matsutake-mushrooms': 'Matsutake Mushrooms',
    'morning-chanting': 'Morning Chanting',
    'tibetan-barley-wine': 'Tibetan Barley Wine',
    'tsampa': 'Tsampa',
    'yak-butter-tea': 'Yak Butter Tea',
    'yak-hotpot': 'Yak Hotpot',
}

for slug, links in food_links.items():
    path = os.path.join('src', 'pages', 'food', f'{slug}.astro')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    link_html = ''
    for link_slug in links:
        name = food_names[link_slug]
        link_tmpl = f'      <a href="/food/{link_slug}" class="rounded-full bg-white border border-slate-200 px-4 py-1.5 text-sm text-slate-700 hover:border-emerald-300 hover:text-emerald-700 transition-colors">{name}</a>\n'
        link_html += link_tmpl
    
    related = '  <div class="mt-12 rounded-2xl bg-slate-50 p-6">\n'
    related += '    <p class="text-sm font-semibold text-emerald-700">Also Try &raquo;</p>\n'
    related += '    <div class="mt-3 flex flex-wrap gap-2">\n'
    related += link_html
    related += '    </div>\n  </div>\n\n</DetailLayout>'
    
    content = content.replace('</DetailLayout>', related)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'{slug}: done')
