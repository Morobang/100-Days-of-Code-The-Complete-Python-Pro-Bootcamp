# Day 40 — Markdown Parser — SOLUTIONS
import re, os

def convert_line(line):
    line = line.strip()
    for i in range(6,0,-1):
        if line.startswith('#'*i+' '):
            return f'<h{i}>{line[i+1:].strip()}</h{i}>'
    if line.startswith('- '):
        line = '<li>' + line[2:] + '</li>'
    else:
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.*?)\*',       r'<em>\1</em>',         line)
        line = re.sub(r'`(.*?)`',           r'<code>\1</code>',     line)
    return line

def convert_markdown(text):
    lines = text.split('\n')
    html_lines = []; in_list = False
    for line in lines:
        converted = convert_line(line)
        if converted.startswith('<li>'):
            if not in_list: html_lines.append('<ul>'); in_list = True
            html_lines.append(converted)
        else:
            if in_list: html_lines.append('</ul>'); in_list = False
            if not converted:
                html_lines.append('')
            elif not converted.startswith('<h'):
                html_lines.append(f'<p>{converted}</p>')
            else:
                html_lines.append(converted)
    if in_list: html_lines.append('</ul>')
    return '\n'.join(html_lines)

def convert_file(input_path, output_path):
    with open(input_path) as f: md = f.read()
    html = convert_markdown(md)
    with open(output_path,'w') as f: f.write(html)

def wrap_html(body, title='Document'):
    return f'<!DOCTYPE html>\n<html>\n<head><title>{title}</title></head>\n<body>\n{body}\n</body>\n</html>'
