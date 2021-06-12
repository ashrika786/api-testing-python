from datetime import datetime


class Logger:

    @classmethod
    def log(cls, text, to_console=True, to_file=True, with_date=True):
        if to_console:
            print(text)
        if to_file:
            cls.write_to_file(text, with_date)

    @classmethod
    def log_request(cls, request_type, url, params, response_status_code):
        text = '\n'.join([
            f'Executed {request_type.__name__.upper()} request',
            f'URL: {url}',
            f'PARAMETERS: {params}',
            f'RESPONSE STATUS CODE: {response_status_code}'
        ])
        cls.log(text)

    @classmethod
    def log_assertion(cls, expression, result):
        text = '\n'.join([
            f'\nExecuted assertion:',
            f'EXPRESSION: {expression}',
            f'RESULT: {result}'
        ])
        cls.log(text)

    @classmethod
    def log_test_start(cls, test_function):
        cls.log(f'\n{"=" * 50}\n', to_console=False, with_date=False)
        text = f'TEST STARTED: {test_function.__name__}'
        cls.log(text)

    @classmethod
    def log_test_finish(cls, test_function, execution_time):
        text = '\n'.join([
            f'\nTEST FINISHED: {test_function.__name__}',
            f'TIME ELAPSED: {execution_time}'
        ])
        cls.log(text)

    @classmethod
    def write_to_file(cls, text, with_date):
        current_date_n_time = datetime.now()
        if with_date:
            text = '\n'.join([f'{current_date_n_time} - {l}' for l in text.split('\n')])
        with open('tests_output.log', 'a', encoding='utf-8') as f:
            f.write(text)
