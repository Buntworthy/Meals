import cmd


# Meal idea index

# add "Root vegetable crumble" swede pumpkin roux vegetarian cheddar nuts winter
# search "vegetable crumble" # Search in the title
# search vegetarian winter # AND search in tags
# tag 1 new_tag # Add a new tag to a search result

# Titles stored in a dict e.g.
#   1: (1, "First title", [tag1 tag2 tag3])
#   2: (2, "Second title", [tag1 tag3])
#   count: 2

# Tags stored in a dict, e.g.
#   tag1: [1, 3, 6]
#   tag2: [3, 4]
#   tag3: [1, 3, 5, 6]

# Title words also stored in a dict
#   title_word1: [1, 6]
#   title_word2: [1, 4]
#   title_word3: [3, 5, 6]
from datastore import DataStoreDict


class MealIndex(cmd.Cmd):
    intro = 'Meal index 1.0'
    prompt = 'mi> '
    file = None

    def __init__(self, data):
        super(MealIndex, self).__init__()
        self.data = data

    def do_add(self, arg):
        'Add an entry: add Red onion and fennel tart, vegetarian pastry'
        (title, tags) = arg.lower().split(',')
        self.data.add_entry(title, tags)

    def do_search(self, arg):
        'Search the index by tag: search pastry'
        # TODO display all if no search terms
        # TODO search for plurals
        # TODO display by index
        # TODO sort by number? Or random?
        search_terms = arg.lower().split()
        self.current_search = self.data.search_tags(search_terms)

        if len(self.current_search) is 0:
            print('[-] - No results found')
        else:
            print('\n')
            print('Results:')
            print('-------------')
            for result_index in self.current_search:
                result = self.data.get_entry(result_index)
                self.display(result)
        print('\n')

    def do_search_title(self, arg):
        'Search the index by title: search_title fennel tart'
        search_terms = arg.lower().split()
        self.current_search = self.data.search_titles(search_terms)

    # TODO other editing operations

    def display(self, result):
        # TODO add padding for larger numbers
        (index, title, tags) = result
        display_line = '[{}]'.format(index) + ' - ' + \
                       '{:.70}'.format(title)
        print(display_line)

    def do_add_tag(self, arg):
        self.update_tags(arg, self.data.add_tag)

    def do_remove_tag(self, arg):
        self.update_tags(arg, self.data.remove_tag)

    def do_close(self, arg):
        self.data.save_data()
        return True

    def do_EOF(self, line):
        return True

    @staticmethod
    def update_tags(arg, method):
        args = arg.split()
        index = int(args[0])
        tags = args[1:]
        try:
            method(index, tags)
        except ValueError:
            print('Index not recognised')


def main():
    data = DataStoreDict('meal_index.p')
    index = MealIndex(data)
    index.cmdloop()


if __name__ == '__main__':
    main()
