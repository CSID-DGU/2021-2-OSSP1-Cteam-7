from DataSpider import peek_dataset
from tqdm import tqdm

def one_shot_inf(bert_model):
    doc = input('Please enter doc content:')
    keywords = bert_model.extract_keywords(doc)
    print(f'Extract result: {keywords}')
    return


def batch_inf(bert_model, enterprise_user):
    if not enterprise_user:
        print('ACCESS DENIED')
    dataset_dir = input('Enter Dataset dir')
    detail_mode = False
    if len(dataset_dir) != 0:
        question_data = peek_dataset(dataset_path=dataset_dir,detailed=detail_mode)
    else:
        question_data = peek_dataset(detailed=detail_mode)
    
    with open('Output/question_DB.csv', 'a+') as o:
        for dindex, d in enumerate(question_data):
            for index, question in enumerate(d):
                keyword_str = ''
                #print(f'Inferencing {d}:{index} - {question}')
                print(f'\rInferencing {dindex}:{index}', end='')
                keywords = bert_model.extract_keywords(question)
                for keyword in keywords:
                    keyword_str = keyword_str + str(keyword) + ','
                o.writelines(f'{question}splitsign{keyword_str}\n')
    print('\nDone.\n\n')
    return


def retrieve_one_shot():
    return


def retrieve_batch(enterprise_user):
    if not enterprise_user:
        print('ACCESS DENIED')
    return