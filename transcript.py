# -*- coding: utf-8 -*-

from pypinyin import pinyin, Style
import argparse
import os, sys

def transcript(line, trn_fp):
    #for line in in_fp.readlines():
    pys = pinyin(line, style=Style.TONE3)
    for i in range(len(pys)):
        if pys[i][0][0] == "，" or pys[i][0][0] == "、":
            pys[i][0] = ','
        elif pys[i][0][0] == '。':
            pys[i][0] = '.'
        elif pys[i][0][0] == "；":
            pys[i][0] = ';'
        elif pys[i][0][0] == "：":
            pys[i][0] = ':'
        elif pys[i][0][0] == "？":
            pys[i][0] = '?'
        elif pys[i][0][0] == "！":
            pys[i][0] = '!'
        elif pys[i][0][0] == "…":
            continue
        elif pys[i][0][0] == "《" or pys[i][0][0] == '》' or pys[i][0][0] == '（' or pys[i][0][0] == '）':
            continue
        elif pys[i][0][0] == '“' or pys[i][0][0] == '”' or pys[i][0][0] == '‘' or pys[i][0][0] == '’':
            continue
        elif pys[i][0][0] == '(' or pys[i][0][0] == ')' or pys[i][0][0] == '"' or pys[i][0][0] == '\'':
            continue
        elif pys[i][0][0] == ' ' or pys[i][0][0] == '/' or pys[i][0][0] == '<' or pys[i][0][0] == '>':
            continue

        if i != len(pys) - 1:
            trn_fp.write(pys[i][0] + ' ')
        else:
            trn_fp.write(pys[i][0])

def text_split(args):
    count = 0
    with open(args.text, encoding="gb2312") as f:
        for l in f.readlines():
            line = l.strip(' ').strip('\n')
            if (line != ''):
                print(line)
                names = args.output_dir.split('/')
                name = names[-2] if names[-1] == '' else names[-1]
                txt_file = os.path.join(args.output_dir, name + "_%03d" % count + ".txt")
                count += 1
                with open(txt_file, mode='w', encoding='utf-8') as txt_fp:
                    txt_fp.write(line)
                    trn_file = txt_file[:-4] + '.trn'
                    with open(trn_file, 'w') as trn_fp:
                        transcript(line, trn_fp)
                    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", default='text.txt')
    parser.add_argument("--output_dir", default='.')
    args = parser.parse_args()

    text_split(args)

if __name__ == '__main__':
    main()
