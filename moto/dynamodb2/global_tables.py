from collections import namedtuple

from moto.dynamodb2.models import Table


DynamoDBGlobalTable = namedtuple('DynamoDBGlobalTable', ['table', 'regions'])


class DynamoDBGlobalTablesBackend:
    def __init__(self):
        self.tables = {}

    def create_global_table(self, table: Table, regions):
        self.tables[table.name] = DynamoDBGlobalTable(table, regions)
