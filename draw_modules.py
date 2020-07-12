import matplotlib.pyplot as graphPlotter

TWEET_DETAIL_FILE = "tweet_data.txt"

def is_word_in_text(word,text):
    if (re.search(word.lower(),text.lower())):
        return True
    return False

def fill_language_dict(lang_list):
    language_dict = {}
    for lang in lang_list:
        language_dict[str(lang)] = 0
    return language_dict

def update_lang_dict(lang):
    language_dict[lang]+=1

def parse_tweets(language_dict):
    raw_data_file = open(TWEET_DETAIL_FILE,'r') # Raw data
    for line in raw_data_file:
        try:
            for word in language_dict.keys():
                if is_word_in_text(word,str(line)):
                    update_lang_dict(word)
        except:
            continue
    raw_data_file.close()
    return language_dict

def draw_graph(language_dict):
    names = list(language_dict.keys())
    values = list(language_dict.values())
    #Fancy Plotting
    x_pos = list(range(len(values)))
    width = 0.1
    ax = graphPlotter.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    graphPlotter.bar(x_pos, names, width,alpha=1,color='palegreen')
    prg_langs = values
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('Programming Languages', fontsize=15)
    ax.set_xticks([p + 0.1 * width for p in x_pos])
    ax.set_xticklabels(prg_langs,fontsize=15)
    graphPlotter.show()

def main():
    languages_parsed = list(str(input("Enter languages to be parsed\n Space spaerated.")).lower().split())
    lang_dict = fill_language_dict(languages_parsed)
    lang_dict = parse_tweets(lang_dict)
    draw_graph(lang_dict)

if __name__ == '__main__':
    main()
