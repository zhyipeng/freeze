FUND_HAD_CONCERNED = 20001


ERROR_PHRASES = {
    FUND_HAD_CONCERNED: '该基金已经关注了噢'
}


class BusinessException(Exception):
    default_error_code = "9000"
    default_error_message = "系统错误"

    def __init__(self, err_code=None, err_msg=None, err_data=None):
        self.err_code = err_code or self.default_error_code
        self.err_msg = err_msg or ERROR_PHRASES.get(
            err_code, self.default_error_message)

        self.err_data = err_data

    def __unicode__(self):
        return self.err_msg


def handle_validation_error_msg(detail):
    if isinstance(detail, dict):
        for key, msg_list in detail.items():
            if msg_list[0]['code'] == 'invalid':
                return msg_list[0]['message']

            else:
                return f'{key}: {msg_list[0]["message"]}'

    elif isinstance(detail, list):
        return detail[0]['message']
