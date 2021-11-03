tokens = []

def construct_tokens():
    with open('enterprise_key.token') as f:
        cachetokens = f.readlines()
    for t in cachetokens: tokens.append(t.strip('\n'))


def evaluate_from_token(enterprise_token):
    construct_tokens()
    if enterprise_token in tokens:
        print('Passed. \tEnterprise Mode')
        return 'Enterprise'
    else:
        print('General')
        return 'General Mode'