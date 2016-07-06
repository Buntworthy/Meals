import pickle


class DataStoreDict:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()

    def get_entry(self, index):
        if index in self.main_index:
            return self.main_index[index]
        else:
            return None

    def add_entry(self, title, tags):
        # TODO check badly formatted entry
        index = self.add_title(title, tags)
        # Use all the title words as tags too
        full_tags = ' '.join((tags, title)).split()
        self.update_index(index, full_tags, self.tag_index)
        self.update_index(index, title.split(), self.title_index)

    def check_index(self, index):
        if index not in self.main_index:
            raise ValueError('Unrecognised index')

    def delete_entry(self, index):
        self.check_index(index)
        del self.main_index[index]

    def add_title(self, title, tags):
        this_count = self.main_index['count'] + 1
        self.main_index[this_count] = (this_count, title, tags)
        self.main_index['count'] = this_count
        return this_count

    def search_titles(self, search_terms):
        return self.search(search_terms, self.title_index)

    def search_tags(self, search_terms):
        return self.search(search_terms, self.tag_index)

    def save_data(self):
        with open(self.filename, 'wb') as save_file:
            pickle.dump((self.main_index, self.tag_index, self.title_index),
                        save_file)

    def load_data(self):
        try:
            with open(self.filename, 'rb') as save_file:
                (self.main_index,
                 self.tag_index,
                 self.title_index) = pickle.load(save_file)
        except FileNotFoundError as e:
            # Start a new filename
            print('Starting new data file')
            self.main_index = {'count': 0}
            self.tag_index = {}
            self.title_index = {}
        except BaseException as e:
            raise e

    def add_tag(self, index, tags):
        self.check_index(index)
        self.update_index(index, tags, self.tag_index)
        (index, title, original_tags) = self.main_index[index]
        original_tags = ' '.join((original_tags, ' '.join(tags)))
        self.main_index[index] = (index, title, original_tags)

    def remove_tag(self, index, tags):
        self.check_index(index)
        (index, title, original_tags) = self.main_index[index]
        for tag in tags:
            self.tag_index[tag].remove(index)
            original_tags = original_tags.replace(tag, '').strip()
        self.main_index[index] = (index, title, original_tags)

    @staticmethod
    def update_index(index, tags, table):
        for tag in tags:
            if tag in table:
                table[tag].append(index)
            else:
                table[tag] = [index, ]

    @staticmethod
    def search(search_terms, index):
        list_of_sets = []
        for key in search_terms:
            if key in index:
                list_of_sets.append(set(index[key]))

        if list_of_sets:
            # Intersect all the sets
            return set.intersection(*list_of_sets)
        else:
            return []

            # TODO display all method
