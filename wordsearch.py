import os
import re
import csv
import click
from docx import Document

def __search_file_for_matches(file_path, match_strs, ignore_case=False):
    try:
        document = Document(file_path)
    except:
        click.echo('Failed to open: %s' % file_path)
        return []

    matches = []
    flags = 0
    if ignore_case:
        flags = re.IGNORECASE
    for para in document.paragraphs:
        for match_phrase in match_strs:
            for match in re.finditer(match_phrase, para.text, flags):
                matches.append(match)

    return matches


def __write_to_csv(file_path, found_strs, out_file, chars):
    click.echo('Writing to file: %s' % out_file)
    with open(out_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for found in found_strs:
            click.echo('    %s,%s' % (file_path, found.re.pattern))
            start = found.start() - chars
            if start < 0:
                start = 0
            end = found.end() + chars
            if end > (len(found.string)):
                end = len(found.string)
            csvwriter.writerow([file_path, found.re.pattern, found.string[start:end]])


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--match', '-m', multiple=True, help='Phrase to search for in files')
@click.option('--output', '-o', type=click.Path(), default='wordsearch-ouptut.csv',
              help='Path and filename for the csv to create')
@click.option('--chars', '-c', default=30,
              help='Number of characters to include before and after a match (default:30)')
@click.option('--ignore-case', is_flag=True, default=False)
def main(path, match, output, chars, ignore_case):
    click.echo('Searching for doc and docx files in:')
    click.echo('    %s' % os.path.abspath(path))
    click.echo('Searching for the following phrases:')
    for str_to_match in match:
        click.echo('    %s' % str_to_match)

    click.echo('Writing output to:')
    click.echo('    %s' % os.path.abspath(output))

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.doc') or file.endswith('.docx'):
                file_path = os.path.abspath(os.path.join(root, file))
                matches = __search_file_for_matches(file_path, match, ignore_case)
                if matches:
                    __write_to_csv(file_path, matches, output, chars)


if __name__ == '__main__':
    main()
