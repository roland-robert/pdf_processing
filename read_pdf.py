import PyPDF2
import os
import shutil


dir_path = os.path.dirname(__file__)
INPUT_DIR = f'{dir_path}/data'
OUTPUT_DIR = f'{dir_path}/output_data'


def get_info_from_pdf(file_path):
    print('Reading : ', file_path)
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    try:
        firt_page = pdf_reader.pages[0]
        # Premiere ligne, 5 premieres colonnes
        title_key_word = firt_page.extract_text().split("\n")[0][:5]

        third_page = pdf_reader.pages[2] #page 3
        # ligne 3, entre col 10 et 15
        table_key_word = third_page.extract_text().split("\n")[2][10:15]
    except Exception as e:
        print('Pas assez de texte ou de pages')
        raise e

    pdf_file_obj.close()
    return title_key_word, table_key_word


def copy_and_rename(file_path: str, title_key_word: str, table_key_word: str):
    print('Copying and renaming : ', file_path)

    new_name = f'{title_key_word}_{table_key_word}.pdf'
    print('New name for :', file_path.split('/')[-1], 'is', new_name)
    print('Sending to : ', OUTPUT_DIR)
    shutil.copy2(file_path, f'{OUTPUT_DIR}/{new_name}')


def main_process():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            file_path = f'{INPUT_DIR}/{filename}'
            title_key_word, table_key_word = get_info_from_pdf(file_path)
            copy_and_rename(file_path, title_key_word, table_key_word)
            print()


if __name__ == '__main__':
    main_process()
