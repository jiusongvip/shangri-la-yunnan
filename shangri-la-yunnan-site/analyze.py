import re, html

def extract_text(html_content):
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Homepage
with open('dist/index.html', 'r', encoding='utf-8') as f:
    raw = f.read()
h_text = extract_text(raw)

words = h_text.split()
sentences = [s.strip() for s in re.split(r'[.!?]+', h_text) if s.strip()]
syllables = sum(len(re.findall(r'[aeiouy]+', w.lower())) or 1 for w in words)

word_count = len(words)
sent_count = len(sentences)
avg_sent_len = word_count / max(sent_count, 1)
flesch = 206.835 - 1.015 * avg_sent_len - 84.6 * (syllables / max(word_count, 1))

print(f'Word count: {word_count}')
print(f'Sentence count: {sent_count}')
print(f'Avg sentence length: {avg_sent_len:.1f} words')
print(f'Flesch Reading Ease: {flesch:.1f}')

# Headings
h1 = len(re.findall(r'</h1>', raw))
h2 = len(re.findall(r'</h2>', raw))
h3 = len(re.findall(r'</h3>', raw))
h4 = len(re.findall(r'</h4>', raw))
print(f'H1:{h1} H2:{h2} H3:{h3} H4:{h4}')

# Links
internal = len(re.findall(r'href="/[a-z]', raw))
external = len(re.findall(r'href="https?://(?!shangrila-yunnan)', raw))
print(f'Internal links: {internal}, External: {external}')

# E-E-A-T signals
has_prices = bool(re.search(r'\d+\s*(RMB|yuan)', h_text))
has_dates = bool(re.search(r'(built in|opening hours|departs at|opens at)', h_text))
has_stats = bool(re.search(r'\d+[,\d]*\s*(km|m\b|people|hours|days|years)', h_text))
has_about = bool(re.search(r'about|our story|who we are', h_text.lower()))
has_contact = bool(re.search(r'contact|reach out', h_text.lower()))
has_citations = bool(re.search(r'(Source|Reference|According to|Cited)', h_text))
print(f'Prices: {has_prices}, Dates: {has_dates}, Stats: {has_stats}')
print(f'About: {has_about}, Contact: {has_contact}, Citations: {has_citations}')

# About page
try:
    with open('dist/about/index.html', 'r', encoding='utf-8') as f:
        about = extract_text(f.read())
    about_words = len(about.split())
    print(f'About page words: {about_words}')
except:
    print('About page: NOT FOUND')
