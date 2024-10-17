import click


class PagesType(click.ParamType):
    name = 'pages'

    def convert(self, value, param, ctx):
        if ',' in value:
            return [int(page) for page in value.split(',')]

        if '-' in value:
            start, end = value.split('-')
            return list(range(int(start), int(end) + 1))

        self.fail(f'Unknown page format: {value}', param, ctx)
