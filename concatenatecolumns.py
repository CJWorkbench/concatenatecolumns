class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        newcol = wf_module.get_param_string('newcolumn')
        if newcol != '':
            cols = wf_module.get_param_string('colnames').split(',')
            cols = [c.strip() for c in cols]
            if cols != [] and cols != ['']:
                for c in cols:
                    if not c in table.columns:
                        wf_module.set_error('There is no column named %s' % c)
                        return table
                table[newcol] = table[cols].apply(lambda x: ' '.join([str(i) for i in x if str(i) != 'nan']), axis=1)
        wf_module.set_ready(notify=False)
        return table