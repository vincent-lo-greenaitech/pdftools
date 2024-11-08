import click


class PagesType(click.ParamType):
    name = 'pages'

    def convert(self, value: str, param, ctx) -> list[int] | None:
        try:
            return self._parse_value(value)
        except ValueError:
            self.fail(f'Unknown page format: {value}', param, ctx)

    def _parse_value(self, value: str) -> list[int]:
        tokens = value.split(',')
        result = []
        for token in tokens:
            if '-' in token:
                start, end = token.split('-')
                result += [i for i in range(int(start), int(end) + 1)]
            else:
                result += [int(token)]
        return result
