from pathlib import Path
from html import escape
from html.parser import HTMLParser
from urllib.parse import quote, urlsplit
import json
import re
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT
DIST = ROOT / 'docs'
REPO = 'https://github.com/zhangrenchuan/chicken-soup-for-the-soul'
CHARSET = 'utf-8'
TOKENS = ['HTML', 'CSS', 'JS', 'WEB', 'jQuery', 'JS+', 'Node.js', 'HTTP', 'AngularJS', 'ES', 'React', 'DOM', 'Mobile', 'Vue', 'Vuex']


class ArticleHTML(HTMLParser):
    tags = set('a blockquote br caption code dd div dl dt em h1 h2 h3 h4 h5 h6 hr img li ol p pre s span strong table tbody td th thead tr ul'.split())

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.output = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.tags:
            return
        safe = []
        for name, value in attrs:
            if not value:
                continue
            if name in ('href', 'src'):
                if value.startswith('www.'):
                    value = 'https://' + value
                parsed = urlsplit(value)
                if parsed.scheme.lower() not in ('', 'http', 'https', 'mailto'):
                    continue
                if not parsed.scheme and not parsed.netloc and parsed.path:
                    if tag == 'img':
                        self.output.append('<span>［原文图片不可用］</span>')
                        return
                    continue
                if name == 'src' and value.startswith('http://'):
                    value = 'https://' + value[7:]
            elif name not in ('alt', 'id', 'title', 'class', 'colspan', 'rowspan'):
                continue
            safe.append(f' {name}="{escape(value, quote=True)}"')
        self.output.append('<' + tag + ''.join(safe) + '>')

    def handle_endtag(self, tag):
        if tag in self.tags and tag not in ('br', 'hr', 'img'):
            self.output.append(f'</{tag}>')

    def handle_data(self, data):
        self.output.append(data.replace('<', '&lt;'))

    def handle_entityref(self, name):
        self.output.append(f'&{name};')

    def handle_charref(self, name):
        self.output.append(f'&#{name};')


def link(url, label, extra=''):
    return f'<a href="{escape(url)}"{extra}>{escape(label)}</a>'


def write_page(path, title, content, root='', search=False):
    assets = f'{root}site.css'
    home = f'{root}index.html'
    script = f'<script src="{root}search.js" defer></script>' if search else ''
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="按章节查找和阅读前端开发笔记，从 HTML、CSS 和 JavaScript 入门。">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; img-src 'self' https:; base-uri 'none'; form-action 'none'">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{assets}">
{script}
</head>
<body>
<a href="#main" class="skip">跳到正文</a>
<header class="top"><div class="wrap"><a class="brand" href="{home}"><span class="mark" aria-hidden="true">&lt;/&gt;</span>前端学习笔记</a>
<nav aria-label="主导航">{link(home+'#catalog', '章节目录')}</nav></div></header>
{content}
<footer class="wrap foot">原作者 {link(REPO, 'zhangrenchuan')} · {link(root+'LICENSE.txt', '原仓库许可')}</footer>
</body></html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding=CHARSET)


def parse_index():
    chapters = []
    for line in (SOURCE / 'README.md').read_text(encoding=CHARSET).splitlines():
        heading = re.fullmatch(r'### \d+\. (.+)', line)
        row = re.fullmatch(r'- \[(.+)\]\((.+\.md)\)', line)
        if heading:
            chapters.append({'title': heading[1], 'url': f'chapter-{len(chapters)+1:02}.html', 'articles': []})
        elif row:
            chapter = chapters[-1]
            title, relative_path = row.groups()
            index = len(chapter['articles']) + 1
            number = len(chapters)
            body = (SOURCE / relative_path).read_text(encoding=CHARSET)
            intro, detail = re.match(r'# .*?\n\n## 先弄懂这件事\n\n([^\n]+)\n\n(.*)', body, re.S).groups()
            chapter['articles'].append({'title': title, 'url': f'notes/{number:02}-{index:02}.html',
                                        'intro': intro, 'detail': detail, 'path': relative_path})
    return chapters


def render_markdown(items):
    ruby = """require 'json'
opts = RDoc::Options.new
texts = JSON.parse(STDIN.read)
puts JSON.generate(texts.map { |text| RDoc::Markdown.parse(text).accept(RDoc::Markup::ToHtml.new(opts)) })
"""
    process = subprocess.run(['ruby', '-rrdoc', '-rrdoc/markdown', '-rrdoc/markup/to_html', '-e', ruby],
                             input=json.dumps(items, ensure_ascii=False), capture_output=True, text=True, check=True)
    for rendered in json.loads(process.stdout):
        parser = ArticleHTML()
        parser.feed(rendered)
        yield ''.join(parser.output)


def home_page(chapters):
    cards = []
    results = []
    for token, chapter in zip(TOKENS, chapters):
        title = escape(chapter['title'])
        cards.append(f'<a class="card" href="{chapter["url"]}"><span class="token">{token}</span>'
                     f'<strong>{title}</strong><span class="meta">{len(chapter["articles"])} 篇笔记</span></a>')
        for item in chapter['articles']:
            key = escape((' '.join((item['title'], chapter['title'], item['intro']))).lower(), quote=True)
            results.append(f'<li data-search="{key}"><a href="{item["url"]}">{escape(item["title"])}'
                           f'<span class="meta">{title}</span></a></li>')
    content = f"""<main id="main">
<section class="hero"><div class="wrap"><div class="decoration" aria-hidden="true"></div>
<h1>从写出第一个网页开始</h1>
<p>从 HTML、CSS 和 JavaScript 到网络请求与组件开发。按章节学习，也可以直接找想看的主题。</p>
<a class="start" href="{chapters[0]['articles'][0]['url']}">开始学 HTML</a>
</div></section>
<section class="wrap home" id="catalog" aria-labelledby="catalog-title">
<div class="section-head"><div><h2 id="catalog-title">章节目录</h2>
<div class="count" id="status" role="status">15 个章节 · 117 篇笔记</div></div>
<label class="search" for="find"><span>搜索笔记</span><input id="find" type="search" placeholder="例如：闭包、CSS、Vue"></label></div>
<div class="grid" id="chapters">{''.join(cards)}</div>
<ul class="results" id="results" hidden>{''.join(results)}</ul>
</section></main>"""
    write_page(DIST / 'index.html', '前端学习笔记', content, search=True)


def article_pages(chapters):
    articles = [item for chapter in chapters for item in chapter['articles']]
    rendered = iter(render_markdown([text for item in articles for text in (item['intro'], item['detail'])]))
    for chapter in chapters:
        title = chapter['title']
        items = chapter['articles']
        rows = ''.join('<li>'+link(item['url'], item['title'])+'</li>' for item in items)
        content = (f'<main class="wrap" id="main"><nav class="crumb" aria-label="当前位置">{link("index.html", "首页")} / 章节</nav>'
                   f'<h1 class="chapter-title">{escape(title)}</h1><p class="meta">{len(items)} 篇笔记</p><ol class="chapter-list">{rows}</ol></main>')
        write_page(DIST / chapter['url'], f'{title} · 前端学习笔记', content)
        for i, item in enumerate(items):
            intro, detail = next(rendered), next(rendered)
            article_title = item['title']
            siblings = ''.join(link(other['url'].split('/')[-1], other['title'],
                                    ' aria-current="page"' if other is item else '') for other in items)
            previous = link(items[i-1]['url'].split('/')[-1], '上一篇 · '+items[i-1]['title']) if i else ''
            following = link(items[i+1]['url'].split('/')[-1], '下一篇 · '+items[i+1]['title']) if i+1 < len(items) else ''
            original = link(REPO+'/blob/master/'+quote(item['path']), '查看原文')
            content = f"""<main class="wrap" id="main">
<nav class="crumb" aria-label="当前位置">{link('../index.html','首页')} / {link('../'+chapter['url'],title)}</nav>
<div class="reader"><nav class="side" aria-label="本章文章"><strong>{escape(title)}</strong>{siblings}</nav>
<article class="paper"><h1>{escape(article_title)}</h1>
<section class="intro"><h2>先弄懂这件事</h2>{intro}</section>{detail}
<p class="meta">{original}</p>
<nav class="pager" aria-label="文章翻页">{previous}{following}</nav></article></div></main>"""
            write_page(DIST / item['url'], f'{article_title} · 前端学习笔记', content, root='../')


if __name__ == '__main__':
    chapters = parse_index()
    assert len(chapters) == 15 and sum(len(c['articles']) for c in chapters) == 117
    home_page(chapters)
    article_pages(chapters)
    shutil.copyfile(SOURCE / 'LICENSE.txt', DIST / 'LICENSE.txt')
