class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        w = ''
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in punct:
                        line = line.replace(i, '')
                w = w + line
                all_words.update({self.file_names: w.split()})
        return all_words

    def find(self, txt):
        dist = {}
        world = self.get_all_words()[self.file_names]
        for i in range(len(world)):
            if txt.lower() == world[i]:
                dist.update({self.file_names: i + 1})
                return dist

    def count(self, txt):
        dist = {}
        world = self.get_all_words()[self.file_names]
        dist.update({self.file_names: world.count(txt.lower())})
        return dist


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))