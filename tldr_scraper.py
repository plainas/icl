import requests

def group_lines_into_paragraphs(lines):
    paragraphs = []
    current_paragraph = []
    for line in lines:
        if len(line) == 0:
            if current_paragraph:
               paragraphs.append(current_paragraph)
               current_paragraph = []
        else:
            current_paragraph.append(line)

    if current_paragraph:
        paragraphs.append(current_paragraph)
    return paragraphs


def paragraphs_to_atum_snippets(paragraphs):
    """
    Requirements:
        * both the description and the command must be one line only
        * description must start with '>' and end with ':'
        * command most start and end with '`'
        * command must follow the description imediatly
    """
    snipets = []
    current_snippet = []
    for paragraph in paragraphs:
        if len(paragraph) != 1:
            # this is considered non valid input,
            # let's cancel a possible snippet and move on
            current_snippet = []
            continue
        elif len(paragraph[0]) < 3:
            # non valid input again
            current_snippet = []
            continue
        elif paragraph[0][0] == "-" and paragraph[0][-1] == ":":
            # if we find many of these in a row
            # the last one overwrites the previous
            current_snippet = [ paragraph[0][2:-1] ]
        elif paragraph[0][0] == "`" and paragraph[0][-1] == "`":
            if len(current_snippet) == 1:
                current_snippet.append(paragraph[0][1:-1])
                snipets.append(current_snippet)
                current_snippet = []
    return snipets


def parse_tldr_page(tldr_page_contents):
    raw_lines = tldr_page_contents.splitlines()
    lines = [l.strip() for l in raw_lines]
    paragraphs = group_lines_into_paragraphs(lines)
    snippets = paragraphs_to_atum_snippets(paragraphs)
    return snippets
    

remote_folders = [
    "https://api.github.com/repos/tldr-pages/tldr/contents/pages/common",
    "https://api.github.com/repos/tldr-pages/tldr/contents/pages/linux",
    "https://api.github.com/repos/tldr-pages/tldr/contents/pages/osx"
]

github_api_responses = [requests.get(url).json() for url in remote_folders]
flat_remote_file_list = [item for sublist in github_api_responses for item in sublist]
remote_tldr_pages_urls = [f['download_url'] for f in flat_remote_file_list]

#TODO: filter out those that don't end with .md

num_pages = len(remote_tldr_pages_urls)

all_commands = []
# This could be parelelized obviously
for i, url in enumerate(remote_tldr_pages_urls): 

    print("Processing page {} of {}...".format(i,num_pages), end='\r', flush=True)
    page_contents = requests.get(url).text
    snippets_from_page = parse_tldr_page(page_contents)
    all_commands.extend(snippets_from_page)


with open("tldr.txt","w+") as f:
    for snippet in all_commands:
        f.write("# {}\n".format(snippet[0]))
        f.write("{}\n\n".format(snippet[1]))